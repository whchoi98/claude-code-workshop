# -*- coding: utf-8 -*-
"""세 산출물(현황판, 통계표, 브리핑)의 규칙표.

규칙은 이 파일 한 곳에만 둔다. 검사기(rules.py)와 현황판 HTML 안의
JavaScript 검사기가 모두 이 표를 읽는다.
"""
import re

from rules import check, is_number, table_shape


def S(limit, **more):
    node = {"type": "string", "max": limit}
    node.update(more)
    return node


def N(**more):
    node = {"type": "number"}
    node.update(more)
    return node


def LIST(items, low, high):
    return {"type": "array", "items": items, "min": low, "max": high}


def OBJ(required, **fields):
    return {"type": "object", "required": required, "fields": fields}


SIGNAL = S(6, enum=["green", "yellow", "red", "none"])
DECIMALS = N(integer=True, min=0, max=2)
SOURCES = LIST(OBJ(["name"], name=S(40), detail=S(60), url=S(300, url=True)), 1, 6)

# ── 1. 현황판 (HTML) ─────────────────────────────────────────────
BOARD = OBJ(
    ["title", "asOf", "cards", "table", "insights", "sources"],
    title=S(30),
    subtitle=S(50),
    asOf=S(30),
    legend=OBJ(["green", "yellow", "red"], green=S(8), yellow=S(8), red=S(8)),
    cards=LIST(
        OBJ(
            ["label", "value", "signal"],
            label=S(18),
            value=N(),
            unit=S(6, min=0),
            decimals=DECIMALS,
            signal=SIGNAL,
            note=S(36),
        ),
        2,
        6,
    ),
    table=OBJ(
        ["caption", "columns", "rows"],
        caption=S(30),
        columns=LIST(
            OBJ(
                ["label", "type"],
                label=S(12),
                type=S(6, enum=["text", "number"]),
                unit=S(6, min=0),
                decimals=DECIMALS,
                bar={"type": "boolean"},
            ),
            2,
            7,
        ),
        rows=LIST(LIST({"type": "cell", "max": 24}, 2, 7), 2, 15),
    ),
    insights=LIST(S(60), 1, 3),
    sources=SOURCES,
)

# ── 2. 통계표 (Excel) ────────────────────────────────────────────
FORMATS = ["int", "decimal1", "decimal2", "percent", "won", "text"]
TOTALS = ["sum", "average", "max", "min", "none"]
VISUALS = ["scale", "bar", "none"]
FUNCTIONS = ["SUM", "AVERAGE", "MAX", "MIN", "ROUND", "IF", "RANK", "ABS", "COUNT"]

SHEET = OBJ(
    ["title", "sheets", "sources"],
    title=S(40),
    subtitle=S(60),
    asOf=S(30),
    sheets=LIST(
        OBJ(
            ["name", "columns", "rows"],
            name=S(20),
            columns=LIST(
                OBJ(
                    ["label", "type"],
                    label=S(16),
                    type=S(7, enum=["text", "number", "formula"]),
                    format=S(8, enum=FORMATS),
                    formula=S(120),
                    total=S(7, enum=TOTALS),
                    visual=S(5, enum=VISUALS),
                ),
                2,
                12,
            ),
            rows=LIST(LIST({"type": "cell", "max": 40}, 1, 12), 1, 200),
            chart=OBJ(
                ["type", "x", "series"],
                type=S(6, enum=["line", "bar", "column"]),
                title=S(30),
                x=S(16),
                series=LIST(S(16), 1, 4),
            ),
            notes=LIST(S(80), 0, 3),
        ),
        1,
        4,
    ),
    sources=SOURCES,
)

# ── 3. 브리핑 (PowerPoint) ───────────────────────────────────────
THEMES = ["ink", "forest", "sunset", "ocean"]
NOTES = S(400)
DECK = OBJ(
    ["title", "slides", "sources"],
    title=S(40),
    subtitle=S(60),
    presenter=S(30),
    date=S(20),
    theme=S(6, enum=THEMES),
    slides=LIST(
        {
            "type": "oneOf",
            "key": "type",
            "options": {
                "numbers": OBJ(
                    ["title", "takeaway", "items"],
                    title=S(36),
                    takeaway=S(60),
                    items=LIST(
                        OBJ(
                            ["label", "value"],
                            label=S(16),
                            value=S(10),
                            unit=S(6, min=0),
                            note=S(30),
                            signal=SIGNAL,
                        ),
                        2,
                        4,
                    ),
                    notes=NOTES,
                ),
                "table": OBJ(
                    ["title", "takeaway", "columns", "rows"],
                    title=S(36),
                    takeaway=S(60),
                    columns=LIST(
                        OBJ(
                            ["label", "type"],
                            label=S(12),
                            type=S(6, enum=["text", "number"]),
                            decimals=DECIMALS,
                        ),
                        2,
                        6,
                    ),
                    rows=LIST(LIST({"type": "cell", "max": 24}, 2, 6), 2, 8),
                    notes=NOTES,
                ),
                "chart": OBJ(
                    ["title", "takeaway", "chart", "categories", "series"],
                    title=S(36),
                    takeaway=S(60),
                    chart=S(6, enum=["column", "bar", "line", "pie"]),
                    categories=LIST(S(12), 2, 24),
                    series=LIST(
                        OBJ(["name", "values"], name=S(16), values=LIST(N(), 2, 24)),
                        1,
                        3,
                    ),
                    unit=S(12),
                    notes=NOTES,
                ),
                "bullets": OBJ(
                    ["title", "bullets"],
                    title=S(36),
                    takeaway=S(60),
                    bullets=LIST(S(70), 2, 5),
                    notes=NOTES,
                ),
            },
        },
        2,
        8,
    ),
    sources=SOURCES,
)

CONTRACTS = {"board": BOARD, "sheet": SHEET, "deck": DECK}

TOKEN = re.compile(u"\\[([^\\[\\]:]+)(:전체)?\\]")
SHEET_NAME_BAD = re.compile(r"[\[\]:*?/\\]")


def _sheet_extra(spec, errs):
    names = []
    for s, sheet in enumerate(spec.get("sheets", [])):
        if not isinstance(sheet, dict):
            continue
        path = "sheets[%d]" % s
        name = sheet.get("name")
        if isinstance(name, str):
            if SHEET_NAME_BAD.search(name) or name == u"출처":
                errs.append(
                    u"%s.name: [ ] : * ? / \\ 는 쓸 수 없고, 「출처」는 자동으로 만드는 시트 이름입니다"
                    % path
                )
            if name in names:
                errs.append(u"%s.name: 시트 이름이 겹칩니다(「%s」)" % (path, name))
            names.append(name)
        columns = [c for c in sheet.get("columns", []) if isinstance(c, dict)]
        labels = [c.get("label") for c in columns]
        for label in set(labels):
            if labels.count(label) > 1:
                errs.append(u"%s.columns: 열 이름이 겹칩니다(「%s」)" % (path, label))
        values = [c for c in columns if c.get("type") != "formula"]
        table_shape(values, sheet.get("rows", []), path, errs)
        numeric = [c.get("label") for c in columns if c.get("type") != "text"]
        for c, col in enumerate(columns):
            where = "%s.columns[%d]" % (path, c)
            if col.get("type") == "formula":
                _formula(col.get("formula"), labels, where, errs)
            elif "formula" in col:
                errs.append(u"%s.formula: type 이 formula 인 열에만 씁니다" % where)
            if col.get("type") == "text" and (
                col.get("total", "none") != "none" or col.get("visual", "none") != "none"
            ):
                errs.append(u"%s: 글자 열에는 total 과 visual 을 쓸 수 없습니다" % where)
        chart = sheet.get("chart")
        if isinstance(chart, dict):
            if chart.get("x") not in labels:
                errs.append(u"%s.chart.x: 「%s」 열이 없습니다" % (path, chart.get("x")))
            for name in chart.get("series", []):
                if name not in numeric:
                    errs.append(
                        u"%s.chart.series: 「%s」은 숫자 열이나 수식 열 이름이어야 합니다" % (path, name)
                    )


def _formula(text, labels, where, errs):
    if not isinstance(text, str) or not text.startswith("="):
        errs.append(u"%s.formula: = 로 시작하는 수식이 있어야 합니다" % where)
        return
    for label, _whole in TOKEN.findall(text):
        if label not in labels:
            errs.append(u"%s.formula: 「%s」 열이 없습니다" % (where, label))
    rest = TOKEN.sub("1", text)
    if not re.match(r"^=[0-9A-Z+\-*/^().,%<>= ]*$", rest):
        errs.append(
            u"%s.formula: 숫자, 사칙 연산, 괄호, [열 이름], [열 이름:전체] 와 허용한 함수만 쓸 수 있습니다"
            % where
        )
        return
    for name in re.findall(r"[A-Z]+", rest):
        if name not in FUNCTIONS:
            errs.append(
                u"%s.formula: %s 함수는 쓸 수 없습니다(쓸 수 있는 함수: %s)"
                % (where, name, ", ".join(FUNCTIONS))
            )


def _deck_extra(spec, errs):
    for i, slide in enumerate(spec.get("slides", [])):
        if not isinstance(slide, dict):
            continue
        path = "slides[%d]" % i
        if slide.get("type") == "table":
            table_shape(slide.get("columns"), slide.get("rows"), path, errs)
        if slide.get("type") == "chart":
            size = len(slide.get("categories", []))
            for s, series in enumerate(slide.get("series", [])):
                if isinstance(series, dict) and len(series.get("values", [])) != size:
                    errs.append(
                        u"%s.series[%d].values: categories 와 같은 %d개여야 합니다"
                        % (path, s, size)
                    )
            if slide.get("chart") == "pie" and len(slide.get("series", [])) != 1:
                errs.append(u"%s.series: pie 는 계열이 하나여야 합니다" % path)


def validate(kind, spec):
    """규칙에 어긋난 곳을 한국어 문장 목록으로 돌려준다. 빈 목록이면 통과."""
    errs = []
    check(spec, CONTRACTS[kind], "", errs)
    if errs or not isinstance(spec, dict):
        return errs
    if kind == "board":
        table = spec["table"]
        table_shape(table["columns"], table["rows"], "table", errs)
    elif kind == "sheet":
        _sheet_extra(spec, errs)
    elif kind == "deck":
        _deck_extra(spec, errs)
    return errs


__all__ = ["CONTRACTS", "FUNCTIONS", "TOKEN", "validate", "is_number"]
