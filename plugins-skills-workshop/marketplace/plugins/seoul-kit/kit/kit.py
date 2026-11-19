#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""seoul-kit 명령줄 도구.

자료(JSON) 하나를 받아 규칙에 맞는지 검사하고 산출물 하나를 만든다.

  python3 kit.py board work/현황판.json     HTML 현황판
  python3 kit.py sheet work/통계표.json     Excel 통계표
  python3 kit.py deck  work/브리핑.json     PowerPoint 브리핑
  python3 kit.py check board work/x.json    검사만
  python3 kit.py rules board                규칙표 보기
  python3 kit.py example board              예시 자료 보기
  python3 kit.py serve                      결과 보관함 켜기
  python3 kit.py doctor                     필요한 라이브러리 확인
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import shelf  # noqa: E402
from contracts import CONTRACTS, FUNCTIONS, validate  # noqa: E402

EXT = {"board": ".html", "sheet": ".xlsx", "deck": ".pptx"}
NAME = {"board": u"현황판", "sheet": u"통계표", "deck": u"브리핑"}
NAME_OBJ = {"board": u"현황판을", "sheet": u"통계표를", "deck": u"브리핑을"}
NEEDS = {"sheet": ("openpyxl", "openpyxl"), "deck": ("pptx", "python-pptx")}


def say(text):
    sys.stdout.write(text + "\n")


def load(path):
    try:
        with open(path, encoding="utf-8") as handle:
            return json.load(handle), None
    except FileNotFoundError:
        return None, u"%s 파일이 없습니다." % path
    except json.JSONDecodeError as error:
        return None, u"%s 를 읽을 수 없습니다(%d번째 줄 근처). 쉼표나 따옴표가 빠지지 않았는지 보세요." % (
            path,
            error.lineno,
        )


def report(kind, path, errs):
    say(u"[검사 실패] %s 자료 %s 에서 고칠 곳 %d군데" % (NAME[kind], path, len(errs)))
    for line in errs:
        say(u"  - " + line)
    say(u"자료 파일의 값만 고친 뒤 같은 명령을 다시 실행하세요. 규칙은 kit.py rules %s 로 볼 수 있습니다." % kind)


def missing(kind):
    if kind not in NEEDS:
        return None
    module, package = NEEDS[kind]
    try:
        __import__(module)
        return None
    except ImportError:
        return package


def build_board(spec, out_path):
    with open(os.path.join(HERE, "board_template.html"), encoding="utf-8") as handle:
        page = handle.read()

    def island(value):
        return json.dumps(value, ensure_ascii=False, indent=1).replace("<", "\\u003c")

    page = page.replace("__CONTRACT__", island(CONTRACTS["board"]), 1).replace("__DATA__", island(spec), 1)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(page)
    return {"cards": len(spec["cards"]), "rows": len(spec["table"]["rows"])}


def make(kind, args):
    spec, problem = load(args.spec)
    if problem:
        say(u"[중단] " + problem)
        return 2
    errs = validate(kind, spec)
    if errs:
        report(kind, args.spec, errs)
        return 2
    package = missing(kind)
    if package:
        say(u"[중단] %s 만들려면 %s 라이브러리가 필요합니다. 진행자에게 알리거나 다음을 실행하세요: python3 -m pip install --user %s" % (NAME_OBJ[kind], package, package))
        return 3
    stem = os.path.splitext(os.path.basename(args.spec))[0]
    out_path = args.out or os.path.join(args.dir, stem + EXT[kind])
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    if kind == "board":
        info = build_board(spec, out_path)
    elif kind == "sheet":
        import sheet

        info = sheet.build(spec, out_path)
    else:
        import deck

        info = deck.build(spec, out_path)
    say(u"[완료] %s 만들었습니다: %s" % (NAME_OBJ[kind], out_path))
    say(u"  내용: " + json.dumps(info, ensure_ascii=False))
    out_dir = os.path.dirname(os.path.abspath(out_path))
    shelf.refresh(out_dir)
    if not args.no_serve:
        _ok, message = shelf.serve(out_dir, args.port)
        say(u"  " + message)
    return 0


def describe(node, name, depth, lines):
    pad = "  " * depth
    kind = node["type"]
    if kind == "object":
        if name:
            lines.append(u"%s%s: 묶음" % (pad, name))
        for key, sub in node["fields"].items():
            mark = u"" if key in node.get("required", []) else u" (없어도 됨)"
            describe(sub, key + mark, depth + (1 if name else 0), lines)
    elif kind == "oneOf":
        lines.append(u"%s%s: 묶음. %s 값에 따라 항목이 다름" % (pad, name, node["key"]))
        for option, sub in node["options"].items():
            lines.append(u"%s  %s = %s 일 때" % (pad, node["key"], option))
            describe(sub, "", depth + 2, lines)
    elif kind == "array":
        lines.append(u"%s%s: 목록 %d~%d개" % (pad, name, node.get("min", 0), node["max"]))
        describe(node["items"], u"각 항목", depth + 1, lines)
    elif kind == "string":
        if "enum" in node:
            lines.append(u"%s%s: %s 가운데 하나" % (pad, name, " | ".join(node["enum"])))
        else:
            extra = u", 주소" if node.get("url") else u""
            extra += u", 빈 글 가능" if node.get("min") == 0 else u""
            lines.append(u"%s%s: 글자 %d자 이하%s" % (pad, name, node["max"], extra))
    elif kind == "number":
        bounds = []
        if node.get("integer"):
            bounds.append(u"정수")
        if "min" in node:
            bounds.append(u"%s 이상" % node["min"])
        if "max" in node:
            bounds.append(u"%s 이하" % node["max"])
        lines.append(u"%s%s: 숫자%s" % (pad, name, u" (" + ", ".join(bounds) + ")" if bounds else u""))
    elif kind == "boolean":
        lines.append(u"%s%s: true 또는 false" % (pad, name))
    elif kind == "cell":
        lines.append(u"%s%s: 글자(%d자 이하) 또는 숫자" % (pad, name, node.get("max", 40)))


def main():
    parser = argparse.ArgumentParser(description="seoul-kit: 자료(JSON)로 현황판, 통계표, 브리핑을 만든다")
    sub = parser.add_subparsers(dest="command")
    for kind in ("board", "sheet", "deck"):
        one = sub.add_parser(kind, help=NAME[kind] + u" 만들기")
        one.add_argument("spec")
        one.add_argument("-o", "--out")
        one.add_argument("--dir", default="out")
        one.add_argument("--port", type=int, default=8000)
        one.add_argument("--no-serve", action="store_true")
    for name in ("check",):
        one = sub.add_parser(name, help=u"검사만 하기")
        one.add_argument("kind", choices=list(EXT))
        one.add_argument("spec")
    for name in ("rules", "example"):
        one = sub.add_parser(name)
        one.add_argument("kind", choices=list(EXT))
    one = sub.add_parser("serve", help=u"결과 보관함 켜기")
    one.add_argument("--dir", default="out")
    one.add_argument("--port", type=int, default=8000)
    sub.add_parser("doctor", help=u"필요한 라이브러리 확인")
    args = parser.parse_args()

    if args.command in EXT:
        return make(args.command, args)
    if args.command == "check":
        spec, problem = load(args.spec)
        if problem:
            say(u"[중단] " + problem)
            return 2
        errs = validate(args.kind, spec)
        if errs:
            report(args.kind, args.spec, errs)
            return 2
        say(u"[통과] %s 자료가 규칙에 맞습니다." % NAME[args.kind])
        return 0
    if args.command == "rules":
        lines = [u"%s 자료 규칙" % NAME[args.kind]]
        describe(CONTRACTS[args.kind], "", 0, lines)
        if args.kind in ("board", "deck"):
            lines.append(u"표: 줄마다 칸 수가 columns 와 같아야 하고, number 열은 따옴표 없는 숫자, text 열은 글자.")
        if args.kind == "sheet":
            lines.append(u"rows: 수식 열(type formula)을 뺀 나머지 열의 값만 순서대로 적는다.")
            lines.append(u"formula: = 로 시작. [열 이름] 은 같은 줄의 칸, [열 이름:전체] 는 그 열 전체. 함수는 %s 만." % ", ".join(FUNCTIONS))
            lines.append(u"시트 이름 「출처」는 자동으로 만들어지므로 쓰지 않는다.")
        if args.kind == "deck":
            lines.append(u"chart: series 마다 values 개수가 categories 와 같아야 한다. pie 는 계열 하나.")
            lines.append(u"표지와 출처 장은 자동으로 붙는다. slides 에는 본문 장만 적는다.")
        say("\n".join(lines))
        return 0
    if args.command == "example":
        with open(os.path.join(HERE, "examples", args.kind + ".json"), encoding="utf-8") as handle:
            say(handle.read().rstrip())
        return 0
    if args.command == "serve":
        ok, message = shelf.serve(args.dir, args.port)
        say(message)
        return 0 if ok else 1
    if args.command == "doctor":
        say(u"Python %s" % sys.version.split()[0])
        bad = 0
        for kind in ("sheet", "deck"):
            package = missing(kind)
            say(u"  %s: %s" % (NAME[kind], u"준비됨" if not package else u"%s 없음 (python3 -m pip install --user %s)" % (package, package)))
            bad += 1 if package else 0
        say(u"  현황판: 준비됨 (추가 설치 없음)")
        return 1 if bad else 0
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
