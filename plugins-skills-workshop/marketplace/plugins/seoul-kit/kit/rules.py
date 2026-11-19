# -*- coding: utf-8 -*-
"""규칙표(contracts.py)에 맞는지 검사하는 작은 검사기.

표준 라이브러리만 쓴다. 같은 규칙표를 board_template.html 안의
JavaScript 검사기도 읽으므로, 규칙 종류를 늘릴 때는 두 곳을 함께 고친다.
"""
import math
import re

CONTROL = re.compile(u"[\u0000-\u001f\u007f\u2028\u2029]")


def is_number(value):
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(value)
    )


def _join(path, key):
    return "%s.%s" % (path, key) if path else key


def _check_string(value, node, path, errs):
    if not isinstance(value, str):
        errs.append(u"%s: 글자로 적어야 합니다" % path)
        return
    if "enum" in node:
        if value not in node["enum"]:
            errs.append(
                u"%s: %s 가운데 하나여야 합니다(지금 「%s」)"
                % (path, ", ".join(node["enum"]), value)
            )
        return
    if CONTROL.search(value) or value != value.strip():
        errs.append(u"%s: 줄바꿈과 앞뒤 빈칸은 넣을 수 없습니다" % path)
    size = len(value)
    low = node.get("min", 1)
    if size < low:
        errs.append(u"%s: 비워 둘 수 없습니다" % path)
    if size > node["max"]:
        errs.append(
            u"%s: %d자 이하여야 합니다(지금 %d자)" % (path, node["max"], size)
        )
    if node.get("url") and not re.match(r"^https?://[^\s]+$", value):
        errs.append(u"%s: http:// 또는 https:// 로 시작하는 주소여야 합니다" % path)


def _check_number(value, node, path, errs):
    if not is_number(value):
        errs.append(u"%s: 따옴표 없는 숫자여야 합니다" % path)
        return
    if node.get("integer") and int(value) != value:
        errs.append(u"%s: 소수점 없는 숫자여야 합니다" % path)
    if "min" in node and value < node["min"]:
        errs.append(u"%s: %s 이상이어야 합니다" % (path, node["min"]))
    if "max" in node and value > node["max"]:
        errs.append(u"%s: %s 이하여야 합니다" % (path, node["max"]))


def _check_object(value, node, path, errs, extra_key=None):
    if not isinstance(value, dict):
        errs.append(u"%s: 중괄호 { } 로 묶은 묶음이어야 합니다" % (path or u"자료"))
        return
    fields = node["fields"]
    for key in value:
        if key not in fields and key != extra_key:
            errs.append(
                u"%s: 쓸 수 없는 항목입니다(쓸 수 있는 항목: %s)"
                % (_join(path, key), ", ".join(fields))
            )
    for key in node.get("required", []):
        if key not in value:
            errs.append(u"%s: 꼭 있어야 하는 항목입니다" % _join(path, key))
    for key, sub in fields.items():
        if key in value:
            check(value[key], sub, _join(path, key), errs)


def check(value, node, path, errs):
    """value 가 node 규칙에 맞는지 보고, 어긋난 곳을 errs 에 한국어로 쌓는다."""
    kind = node["type"]
    if kind == "object":
        _check_object(value, node, path, errs)
    elif kind == "oneOf":
        key = node["key"]
        if not isinstance(value, dict) or value.get(key) not in node["options"]:
            errs.append(
                u"%s: %s 가운데 하나여야 합니다"
                % (_join(path, key), ", ".join(node["options"]))
            )
            return
        _check_object(value, node["options"][value[key]], path, errs, extra_key=key)
    elif kind == "array":
        if not isinstance(value, list):
            errs.append(u"%s: 대괄호 [ ] 로 묶은 목록이어야 합니다" % path)
            return
        if len(value) < node.get("min", 0) or len(value) > node.get("max", 10 ** 6):
            errs.append(
                u"%s: %d개에서 %d개 사이여야 합니다(지금 %d개)"
                % (path, node.get("min", 0), node.get("max", 10 ** 6), len(value))
            )
        for index, item in enumerate(value):
            check(item, node["items"], "%s[%d]" % (path, index), errs)
    elif kind == "string":
        _check_string(value, node, path, errs)
    elif kind == "number":
        _check_number(value, node, path, errs)
    elif kind == "boolean":
        if not isinstance(value, bool):
            errs.append(u"%s: true 또는 false 여야 합니다" % path)
    elif kind == "cell":
        if is_number(value):
            return
        _check_string(value, {"max": node.get("max", 40), "min": 1}, path, errs)
    else:
        raise ValueError("unknown rule type: %s" % kind)


def table_shape(columns, rows, path, errs):
    """표의 줄마다 칸 수와 칸의 종류(글자, 숫자)가 머리글과 맞는지 본다."""
    if not isinstance(columns, list) or not isinstance(rows, list):
        return
    for r, row in enumerate(rows):
        if not isinstance(row, list):
            continue
        if len(row) != len(columns):
            errs.append(
                u"%s.rows[%d]: 칸이 %d개여야 합니다(지금 %d개)"
                % (path, r, len(columns), len(row))
            )
            continue
        for c, col in enumerate(columns):
            if not isinstance(col, dict):
                continue
            where = u"%s.rows[%d][%d]" % (path, r, c)
            if col.get("type") == "number" and not is_number(row[c]):
                errs.append(
                    u"%s: 「%s」 열은 따옴표 없는 숫자여야 합니다" % (where, col.get("label"))
                )
            if col.get("type") == "text" and not isinstance(row[c], str):
                errs.append(
                    u"%s: 「%s」 열은 따옴표로 묶은 글자여야 합니다" % (where, col.get("label"))
                )
