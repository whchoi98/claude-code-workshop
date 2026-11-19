# -*- coding: utf-8 -*-
"""통계표 자료(JSON)를 Excel 파일로 만든다. 계산은 모두 Excel 수식으로 남긴다."""
import datetime
import unicodedata

from contracts import TOKEN, is_number

FORMAT = {
    "int": "#,##0",
    "decimal1": "#,##0.0",
    "decimal2": "#,##0.00",
    "percent": "0.0%",
    "won": u'#,##0"원"',
    "text": "@",
}
# SUBTOTAL 을 쓰면 표에 필터를 걸었을 때 요약 줄이 보이는 줄만 다시 계산한다.
TOTAL = {"sum": 109, "average": 101, "max": 104, "min": 105}
TOTAL_NAME = {"sum": u"합계", "average": u"평균", "max": u"최댓값", "min": u"최솟값"}
HEAD_ROW = 4
INK, MUTED, LINE = "1F2430", "6A7180", "D9DCE3"


def _width(value):
    return sum(2 if unicodedata.east_asian_width(ch) in "WF" else 1 for ch in str(value))


def _default_format(col, values):
    if col["type"] == "text":
        return "text"
    if col["type"] == "formula":
        return "decimal1"
    return "int" if all(float(v).is_integer() for v in values) else "decimal1"


def build(spec, out_path):
    from openpyxl import Workbook
    from openpyxl.chart import BarChart, LineChart, Reference
    from openpyxl.formatting.rule import ColorScaleRule, DataBarRule
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
    from openpyxl.worksheet.table import Table, TableStyleInfo

    book = Workbook()
    book.remove(book.active)
    book.properties.title = spec["title"]
    book.properties.creator = "seoul-kit"

    for index, sheet in enumerate(spec["sheets"]):
        ws = book.create_sheet(sheet["name"])
        columns = sheet["columns"]
        rows = sheet["rows"]
        letters = {col["label"]: get_column_letter(i + 1) for i, col in enumerate(columns)}
        first, last = HEAD_ROW + 1, HEAD_ROW + len(rows)

        ws["A1"] = spec["title"]
        ws["A1"].font = Font(size=16, bold=True, color=INK)
        ws.row_dimensions[1].height = 28
        ws["A2"] = u" · ".join(x for x in (spec.get("subtitle"), spec.get("asOf")) if x)
        ws["A2"].font = Font(size=10, color=MUTED)

        def translate(formula, row):
            def swap(match):
                letter = letters[match.group(1)]
                if match.group(2):
                    return "$%s$%d:$%s$%d" % (letter, first, letter, last)
                return "%s%d" % (letter, row)

            return TOKEN.sub(swap, formula)

        value_index = [i for i, col in enumerate(columns) if col["type"] != "formula"]
        widths = [_width(col["label"]) + 4 for col in columns]
        for c, col in enumerate(columns):
            head = ws.cell(row=HEAD_ROW, column=c + 1, value=col["label"])
            head.font = Font(bold=True, color="FFFFFF")
            head.fill = PatternFill("solid", fgColor=INK)
            head.alignment = Alignment(
                horizontal="left" if col["type"] == "text" else "right", vertical="center"
            )
        ws.row_dimensions[HEAD_ROW].height = 22

        for r, row in enumerate(rows):
            line = first + r
            for c, col in enumerate(columns):
                cell = ws.cell(row=line, column=c + 1)
                if col["type"] == "formula":
                    cell.value = translate(col["formula"], line)
                    shown = "0,000.0"
                else:
                    cell.value = row[value_index.index(c)]
                    shown = cell.value
                picked = col.get("format") or _default_format(
                    col, [x[value_index.index(c)] for x in rows] if col["type"] == "number" else []
                )
                cell.number_format = FORMAT[picked]
                if col["type"] != "text":
                    cell.alignment = Alignment(horizontal="right")
                    shown = "{:,}".format(shown) if is_number(shown) else shown
                widths[c] = max(widths[c], _width(shown) + 3)

        ref = "A%d:%s%d" % (HEAD_ROW, get_column_letter(len(columns)), last)
        table = Table(displayName="T%d" % (index + 1), ref=ref)
        table.tableStyleInfo = TableStyleInfo(name="TableStyleLight1", showRowStripes=True)
        ws.add_table(table)

        totals = [(c, col) for c, col in enumerate(columns) if col.get("total", "none") != "none"]
        tail = last
        if totals:
            tail = last + 1
            kinds = set(col["total"] for _c, col in totals)
            label = TOTAL_NAME[kinds.pop()] if len(kinds) == 1 else u"요약"
            edge = Border(top=Side(style="medium", color=INK))
            for c in range(len(columns)):
                cell = ws.cell(row=tail, column=c + 1)
                cell.border = edge
                cell.font = Font(bold=True, color=INK)
            ws.cell(row=tail, column=1, value=label)
            for c, col in totals:
                letter = get_column_letter(c + 1)
                cell = ws.cell(row=tail, column=c + 1)
                cell.value = "=SUBTOTAL(%d,%s%d:%s%d)" % (TOTAL[col["total"]], letter, first, letter, last)
                cell.number_format = ws.cell(row=first, column=c + 1).number_format
                cell.alignment = Alignment(horizontal="right")
            if label == u"요약":
                mixed = u", ".join(u"%s %s" % (col["label"], TOTAL_NAME[col["total"]]) for _c, col in totals)
                sheet = dict(sheet, notes=list(sheet.get("notes", [])) + [u"요약 줄: " + mixed])

        for c, col in enumerate(columns):
            letter = get_column_letter(c + 1)
            area = "%s%d:%s%d" % (letter, first, letter, last)
            if col.get("visual") == "scale":
                ws.conditional_formatting.add(
                    area,
                    ColorScaleRule(start_type="min", start_color="FFFFFF", end_type="max", end_color="F2A65A"),
                )
            elif col.get("visual") == "bar":
                ws.conditional_formatting.add(
                    area, DataBarRule(start_type="min", end_type="max", color="6E8FF0", showValue=True)
                )
            ws.column_dimensions[letter].width = min(max(widths[c], 9), 44)

        line = tail + 2
        for note in sheet.get("notes", []):
            ws.cell(row=line, column=1, value=note).font = Font(size=10, color=MUTED)
            line += 1

        chart_spec = sheet.get("chart")
        if chart_spec:
            chart = LineChart() if chart_spec["type"] == "line" else BarChart()
            if chart_spec["type"] == "bar":
                chart.type = "bar"
            elif chart_spec["type"] == "column":
                chart.type = "col"
            chart.title = chart_spec.get("title")
            chart.height, chart.width = 9.5, 19
            labels = [col["label"] for col in columns]
            for name in chart_spec["series"]:
                col_no = labels.index(name) + 1
                chart.add_data(
                    Reference(ws, min_col=col_no, min_row=HEAD_ROW, max_row=last), titles_from_data=True
                )
            for series in chart.series:
                series.smooth = False
            x_no = labels.index(chart_spec["x"]) + 1
            chart.set_categories(Reference(ws, min_col=x_no, min_row=first, max_row=last))
            ws.add_chart(chart, "%s%d" % (get_column_letter(len(columns) + 2), HEAD_ROW))

        ws.freeze_panes = "B%d" % first
        ws.sheet_view.showGridLines = False
        ws.page_setup.orientation = "landscape"
        ws.page_setup.fitToWidth = 1
        ws.page_setup.fitToHeight = 0
        ws.sheet_properties.pageSetUpPr.fitToPage = True

    src = book.create_sheet(u"출처")
    src["A1"] = u"출처"
    src["A1"].font = Font(size=16, bold=True, color=INK)
    for c, label in enumerate([u"자료", u"자세히", u"주소"]):
        head = src.cell(row=3, column=c + 1, value=label)
        head.font = Font(bold=True, color="FFFFFF")
        head.fill = PatternFill("solid", fgColor=INK)
    for r, source in enumerate(spec["sources"]):
        src.cell(row=4 + r, column=1, value=source["name"])
        src.cell(row=4 + r, column=2, value=source.get("detail"))
        if source.get("url"):
            link = src.cell(row=4 + r, column=3, value=source["url"])
            link.hyperlink = source["url"]
            link.font = Font(color="3457D5", underline="single")
    foot = 6 + len(spec["sources"])
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    src.cell(row=foot, column=1, value=u"만든 시각: %s" % stamp).font = Font(size=10, color=MUTED)
    src.cell(
        row=foot + 1, column=1, value=u"합계와 비율은 Excel 수식입니다. 값을 고치면 함께 바뀝니다."
    ).font = Font(size=10, color=MUTED)
    for letter, key in (("A", "name"), ("B", "detail"), ("C", "url")):
        longest = max(_width(source.get(key) or "") for source in spec["sources"])
        src.column_dimensions[letter].width = min(max(longest + 4, 14), 70)
    src.sheet_view.showGridLines = False
    # 수식은 값 없이 저장되므로, 파일을 열 때 Excel 이 전부 다시 계산하게 한다.
    book.calculation.fullCalcOnLoad = True

    book.save(out_path)
    return {"sheets": [s["name"] for s in spec["sheets"]] + [u"출처"]}
