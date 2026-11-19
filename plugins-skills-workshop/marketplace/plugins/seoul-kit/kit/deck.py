# -*- coding: utf-8 -*-
"""브리핑 자료(JSON)를 PowerPoint 파일로 만든다. 표와 차트는 PowerPoint 에서 고칠 수 있는 진짜 표와 차트다."""
import datetime

from contracts import is_number

THEMES = {
    "ink": {"dark": "14171F", "accent": "3D6BFF", "soft": "EEF2FF", "third": "9DB2FF"},
    "forest": {"dark": "12332B", "accent": "1F9D6B", "soft": "E8F5EF", "third": "9AD3BC"},
    "sunset": {"dark": "3A1F1A", "accent": "E4572E", "soft": "FDEEE8", "third": "F2B8A6"},
    "ocean": {"dark": "0F2A43", "accent": "0E8FB3", "soft": "E6F4F9", "third": "9FD5E5"},
}
SIGNAL = {"green": "1E9E5A", "yellow": "E2A400", "red": "D8443C"}
FONT = u"맑은 고딕"
MUTED, LINE, WHITE = "6A7180", "D9DCE3", "FFFFFF"
W, H, M = 13.333, 7.5, 0.7
BODY_TOP, BODY_H = 2.4, 4.3


def build(spec, out_path):
    from pptx import Presentation
    from pptx.chart.data import CategoryChartData
    from pptx.dml.color import RGBColor
    from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
    from pptx.enum.shapes import MSO_SHAPE
    from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
    from pptx.oxml.ns import qn
    from pptx.util import Inches, Pt

    theme = THEMES[spec.get("theme", "ink")]
    dark, accent, soft = theme["dark"], theme["accent"], theme["soft"]
    palette = [accent, dark, theme["third"]]
    align_of = {"left": PP_ALIGN.LEFT, "right": PP_ALIGN.RIGHT, "center": PP_ALIGN.CENTER}
    anchor_of = {"top": MSO_ANCHOR.TOP, "middle": MSO_ANCHOR.MIDDLE, "bottom": MSO_ANCHOR.BOTTOM}

    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(W), Inches(H)
    prs.core_properties.title = spec["title"]
    prs.core_properties.author = spec.get("presenter", "seoul-kit")
    blank = prs.slide_layouts[6]

    def rgb(code):
        return RGBColor.from_string(code)

    def style(run, size, color, bold=False):
        font = run.font
        font.size, font.bold, font.name = Pt(size), bold, FONT
        font.color.rgb = rgb(color)
        # python-pptx 는 영문 글꼴만 지정하므로 한글 글꼴(a:ea)을 직접 붙인다.
        props = run._r.get_or_add_rPr()
        for old in props.findall(qn("a:ea")):
            props.remove(old)
        props.find(qn("a:latin")).addnext(props.makeelement(qn("a:ea"), {"typeface": FONT}))

    def text(slide, x, y, w, h, parts, align="left", anchor="top"):
        """parts 는 (글, 크기, 색, 굵게) 묶음의 목록. 한 줄에 이어 붙인다."""
        box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
        frame = box.text_frame
        frame.word_wrap = True
        frame.margin_left = frame.margin_right = frame.margin_top = frame.margin_bottom = 0
        frame.vertical_anchor = anchor_of[anchor]
        para = frame.paragraphs[0]
        para.alignment = align_of[align]
        for value, size, color, bold in parts:
            style_run = para.add_run()
            style_run.text = value
            style(style_run, size, color, bold)
        return box

    def shape(slide, kind, x, y, w, h, fill):
        item = slide.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
        item.fill.solid()
        item.fill.fore_color.rgb = rgb(fill)
        item.line.fill.background()
        item.shadow.inherit = False
        return item

    def number_text(value, decimals=None):
        if not is_number(value):
            return str(value)
        if decimals is None:
            decimals = 0 if float(value).is_integer() else 1
        return "{:,.{d}f}".format(value, d=decimals)

    slides = spec["slides"]
    total = len(slides) + 2

    # 표지
    cover = prs.slides.add_slide(blank)
    shape(cover, MSO_SHAPE.RECTANGLE, 0, 0, W, H, dark)
    for i, name in enumerate(["red", "yellow", "green"]):
        shape(cover, MSO_SHAPE.OVAL, M + i * 0.36, 0.78, 0.22, 0.22, SIGNAL[name])
    text(cover, M, 2.05, W - 2 * M, 1.9, [(spec["title"], 46, WHITE, True)], anchor="bottom")
    shape(cover, MSO_SHAPE.RECTANGLE, M, 4.18, 1.3, 0.07, accent)
    if spec.get("subtitle"):
        text(cover, M, 4.42, W - 2 * M, 0.9, [(spec["subtitle"], 22, theme["third"], False)])
    by = u"  ·  ".join(x for x in (spec.get("presenter"), spec.get("date")) if x)
    if by:
        text(cover, M, 6.35, W - 2 * M, 0.4, [(by, 15, WHITE, False)])

    def frame(slide, no, title, takeaway=None):
        text(slide, M, 0.5, 2, 0.3, [("%02d" % no, 14, accent, True)])
        text(slide, M, 0.8, W - 2 * M, 0.7, [(title, 30, dark, True)], anchor="middle")
        if takeaway:
            shape(slide, MSO_SHAPE.RECTANGLE, M, 1.66, 0.09, 0.46, accent)
            text(slide, M + 0.26, 1.64, W - 2 * M - 0.26, 0.5, [(takeaway, 18, dark, False)], anchor="middle")
        shape(slide, MSO_SHAPE.RECTANGLE, M, 6.95, W - 2 * M, 0.012, LINE)
        text(slide, M, 7.04, 8, 0.3, [(spec["title"], 10, MUTED, False)])
        text(slide, W - M - 2, 7.04, 2, 0.3, [("%d / %d" % (no + 1, total), 10, MUTED, False)], align="right")

    def numbers(slide, item):
        cards = item["items"]
        gap = 0.3
        width = (W - 2 * M - gap * (len(cards) - 1)) / len(cards)
        for i, card in enumerate(cards):
            x = M + i * (width + gap)
            box = shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, x, BODY_TOP + 0.1, width, 3.7, soft)
            box.adjustments[0] = 0.06
            if card.get("signal") in SIGNAL:
                shape(slide, MSO_SHAPE.OVAL, x + width - 0.62, BODY_TOP + 0.42, 0.26, 0.26, SIGNAL[card["signal"]])
            text(slide, x + 0.36, BODY_TOP + 0.42, width - 1.1, 0.4, [(card["label"], 16, MUTED, True)])
            # 한글은 한 글자가 글자 크기만큼, 숫자와 영문은 그 절반 남짓을 차지한다고 보고 한 줄에 들어가게 줄인다.
            units = sum(1.0 if ord(ch) > 0x2E7F else 0.62 for ch in card["value"])
            room = (width - 0.72) * 72 - (len(card.get("unit", "")) + 1) * 16
            size = int(max(26, min(60 if len(cards) <= 3 else 46, room / units)))
            parts = [(card["value"], size, dark, True)]
            if card.get("unit"):
                parts.append((" " + card["unit"], 20, MUTED, True))
            text(slide, x + 0.36, BODY_TOP + 1.0, width - 0.6, 1.5, parts, anchor="middle")
            if card.get("note"):
                text(slide, x + 0.36, BODY_TOP + 2.75, width - 0.7, 0.8, [(card["note"], 14, dark, False)])

    def table(slide, item):
        columns, rows = item["columns"], item["rows"]
        height = min(BODY_H, 0.52 * (len(rows) + 1))
        holder = slide.shapes.add_table(
            len(rows) + 1, len(columns), Inches(M), Inches(BODY_TOP + 0.1), Inches(W - 2 * M), Inches(height)
        )
        grid = holder.table
        grid.first_row, grid.horz_banding = True, False
        weights = [2.2 if col["type"] == "text" else 1.4 for col in columns]
        for c, col in enumerate(columns):
            grid.columns[c].width = Inches((W - 2 * M) * weights[c] / sum(weights))

        def fill_cell(cell, value, size, color, bold, back, right):
            cell.fill.solid()
            cell.fill.fore_color.rgb = rgb(back)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.margin_left = cell.margin_right = Inches(0.16)
            para = cell.text_frame.paragraphs[0]
            para.alignment = PP_ALIGN.RIGHT if right else PP_ALIGN.LEFT
            run = para.add_run()
            run.text = value
            style(run, size, color, bold)

        for c, col in enumerate(columns):
            fill_cell(grid.cell(0, c), col["label"], 14, WHITE, True, dark, col["type"] == "number")
        for r, row in enumerate(rows):
            back = WHITE if r % 2 == 0 else soft
            for c, col in enumerate(columns):
                value = number_text(row[c], col.get("decimals")) if col["type"] == "number" else row[c]
                fill_cell(grid.cell(r + 1, c), value, 15, dark, c == 0, back, col["type"] == "number")

    def chart(slide, item):
        kinds = {
            "column": XL_CHART_TYPE.COLUMN_CLUSTERED,
            "bar": XL_CHART_TYPE.BAR_CLUSTERED,
            "line": XL_CHART_TYPE.LINE_MARKERS,
            "pie": XL_CHART_TYPE.PIE,
        }
        data = CategoryChartData()
        data.categories = item["categories"]
        for series in item["series"]:
            data.add_series(series["name"], series["values"])
        holder = slide.shapes.add_chart(
            kinds[item["chart"]], Inches(M), Inches(BODY_TOP + 0.05), Inches(W - 2 * M), Inches(BODY_H), data
        )
        plot_chart = holder.chart
        plot_chart.font.size, plot_chart.font.name = Pt(12), FONT
        plot_chart.font.color.rgb = rgb(MUTED)
        plot = plot_chart.plots[0]
        many = len(item["series"]) > 1
        plot_chart.has_legend = many or item["chart"] == "pie"
        if plot_chart.has_legend:
            plot_chart.legend.position = XL_LEGEND_POSITION.BOTTOM
            plot_chart.legend.include_in_layout = False
        if item["chart"] == "pie":
            shades = [accent, dark, theme["third"], "8A93A6", "C9CED8", "E2A400", "1E9E5A", "D8443C"]
            for p in range(len(item["categories"])):
                point = plot.series[0].points[p]
                point.format.fill.solid()
                point.format.fill.fore_color.rgb = rgb(shades[p % len(shades)])
            plot.has_data_labels = True
            plot.data_labels.show_percentage, plot.data_labels.show_value = True, False
            plot.data_labels.number_format, plot.data_labels.number_format_is_linked = "0%", False
            plot.data_labels.font.size = Pt(12)
        else:
            axis = plot_chart.value_axis
            axis.has_major_gridlines = True
            axis.major_gridlines.format.line.color.rgb = rgb("E3E6EC")
            axis.format.line.fill.background()
            axis.tick_labels.number_format, axis.tick_labels.number_format_is_linked = "#,##0", False
            plot_chart.category_axis.format.line.color.rgb = rgb(LINE)
            for s, series in enumerate(plot.series):
                color = rgb(palette[s % len(palette)])
                if item["chart"] == "line":
                    series.format.line.color.rgb = color
                    series.format.line.width = Pt(2.75)
                    series.smooth = False
                    series.marker.format.fill.solid()
                    series.marker.format.fill.fore_color.rgb = color
                    series.marker.format.line.color.rgb = color
                else:
                    series.format.fill.solid()
                    series.format.fill.fore_color.rgb = color
            if item["chart"] != "line":
                plot.gap_width = 70
            if not many and len(item["categories"]) <= 10:
                plot.has_data_labels = True
                plot.data_labels.number_format, plot.data_labels.number_format_is_linked = "#,##0.##", False
                plot.data_labels.font.size = Pt(11)
        if item.get("unit"):
            text(slide, W - M - 3, 2.18, 3, 0.25, [(u"단위: " + item["unit"], 11, MUTED, False)], align="right")

    def bullets(slide, item):
        lines = item["bullets"]
        top = BODY_TOP if item.get("takeaway") else 1.9
        step = min(1.1, (6.6 - top) / len(lines))
        for i, line in enumerate(lines):
            y = top + 0.15 + i * step
            dot = shape(slide, MSO_SHAPE.OVAL, M, y, 0.46, 0.46, accent)
            frame_ = dot.text_frame
            frame_.margin_left = frame_.margin_right = frame_.margin_top = frame_.margin_bottom = 0
            frame_.vertical_anchor = MSO_ANCHOR.MIDDLE
            frame_.paragraphs[0].alignment = PP_ALIGN.CENTER
            run = frame_.paragraphs[0].add_run()
            run.text = str(i + 1)
            style(run, 14, WHITE, True)
            text(slide, M + 0.72, y - 0.06, W - 2 * M - 0.72, 0.6, [(line, 20, dark, False)], anchor="middle")

    draw = {"numbers": numbers, "table": table, "chart": chart, "bullets": bullets}
    for i, item in enumerate(slides):
        slide = prs.slides.add_slide(blank)
        frame(slide, i + 1, item["title"], item.get("takeaway"))
        draw[item["type"]](slide, item)
        if item.get("notes"):
            slide.notes_slide.notes_text_frame.text = item["notes"]

    # 출처
    last = prs.slides.add_slide(blank)
    frame(last, len(slides) + 1, u"출처")
    for i, source in enumerate(spec["sources"]):
        y = 1.9 + i * 0.78
        name = [(source["name"], 16, dark, True)]
        if source.get("detail"):
            name.append((u"   " + source["detail"], 14, MUTED, False))
        text(last, M, y, W - 2 * M, 0.36, name)
        if source.get("url"):
            text(last, M, y + 0.36, W - 2 * M, 0.3, [(source["url"], 11, accent, False)])
    stamp = spec.get("date") or datetime.date.today().isoformat()
    text(last, M, 6.55, W - 2 * M, 0.3, [(u"만든 날: %s" % stamp, 11, MUTED, False)])

    prs.save(out_path)
    return {"slides": total}
