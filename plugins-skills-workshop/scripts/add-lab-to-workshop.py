#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""서울 데이터 실습 페이지를 기존 핸즈온 랩(ccw-hands-on-lab)의 캡스톤 M7로 넣는다.

    python3 scripts/add-lab-to-workshop.py            # ../ccw-hands-on-lab 에 넣는다
    python3 scripts/add-lab-to-workshop.py <랩 폴더>   # 다른 위치에 넣는다

하는 일
  1. 랩 폴더의 모든 페이지 사이드바에서 「캡스톤 · 프로젝트 선택」 묶음의 마지막 항목(M7)으로 넣고 개수를 고친다.
  2. lab/ 의 페이지를 기존 페이지와 같은 사이드바, 상단 바, 하단 이동 링크로 바꿔 랩 폴더에 쓴다.
  3. 페이지별 CSS와 예시 이미지를 랩 폴더의 assets/ 로 복사한다.
  4. 포털(index.html)의 Capstone Missions 카드에 MISSION 7을 넣는다.

여러 번 실행해도 같은 결과가 나온다. 랩 페이지를 원본에서 다시 생성해 항목이 사라졌을 때 다시 실행하면 된다.
예전 배치(별도 묶음 「업무 활용 실습」, 포털의 Business Hands-on Lab 섹션)가 남아 있으면 지운다.
원본은 lab/ 의 페이지다. 내용을 고칠 때는 lab/ 의 페이지를 고치고 이 스크립트를 다시 실행한다.
"""
import io
import os
import re
import shutil
import sys

PAGE = "ClaudeCode_Day1_SeoulData_HandsOnLab"
TITLE = u"서울 데이터로 만드는 세 가지 보고"
GROUP = u"캡스톤 · 프로젝트 선택"
NUMBER = "M7"
IDENTITY = "Seoul Data"
NAV_TITLE = u"Seoul Data · 세 가지 보고"
OLD_GROUP = u"업무 활용 실습"
REFERENCE_PAGE = "ClaudeCode_Capstone_Setup.html"

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = os.path.join(HERE, "lab")
LAB = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(os.path.dirname(HERE), "ccw-hands-on-lab")

CHECK = (
    '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 4 4L19 6"/></svg>'
)
NAV_ITEM = (
    u'<li data-nav-entry data-search="{group} {number} {nav_title} {title} 현황판 통계표 브리핑">'
    u'<a class="chapter-link" href="{page}.html" data-chapter-link="{page}" data-core-chapter="false" title="{title}"{current}>'
    u'<span class="nav-number">{number}</span><span class="nav-title">{nav_title}</span>'
    u'<span class="read-indicator">{check}</span></a></li>'
)
GROUP_RE = re.compile(
    u'(<section class="nav-group" data-nav-group><h2><span>%s</span><span>)\\d+(개</span></h2><ol>)(.*?)(</ol></section>)' % re.escape(GROUP),
    re.S,
)
OLD_GROUP_RE = re.compile(
    u'<section class="nav-group" data-nav-group><h2><span>%s</span>.*?</section>' % re.escape(OLD_GROUP), re.S
)
ITEM_RE = re.compile(r'<li data-nav-entry data-search="[^"]*"><a class="chapter-link" href="%s\.html".*?</a></li>' % PAGE, re.S)

CARD = u"""<a class="card" href="{page}.html">
<span class="mnum">MISSION 7</span>
<span class="identity">{identity}</span>
<h3>{title}</h3>
<p class="desc"><b>업무 활용 트랙.</b> 개발자가 아니어도 따라 합니다. seoul-kit 플러그인과 서울 MCP로 실시간 서울 데이터를 가져와 HTML 현황판, Excel 통계표, PowerPoint 브리핑을 차례로 만듭니다. 코드를 쓰지 않고 말로 시키고 말로 고칩니다.</p>
<p class="finale">피날레: <b>같은 방식을 내 팀 지표에 적용하고, 내 Skill 한 줄로 세 결과를 만듭니다.</b></p>
<span class="foot"><span>120분 / 준비 + 미션 4</span><span class="go">시작 →</span></span>
</a>
""".format(page=PAGE, identity=IDENTITY, title=TITLE)
CARD_RE = re.compile(r'<a class="card" href="%s\.html">.*?</a>\n' % PAGE, re.S)
CARD_ANCHOR = '</div>\n</section>\n<section class="wrap" id="references">'
OLD_SECTION_RE = re.compile(r'<section class="wrap" id="bizlab">.*?</section>\n', re.S)
OLD_TOC_ITEM = '<li><a href="#section-biz" data-toc-link>Business Hands-on Lab</a></li>'
OLD_META = (u"Capstone 4 + Reference 3 + 업무 활용 랩 1</strong>", u"Capstone 4 + Reference 3</strong>")


def read(path):
    with io.open(path, encoding="utf-8") as handle:
        return handle.read()


def write(path, text):
    with io.open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def place_nav(text, current):
    """사이드바 HTML에서 예전 배치를 지우고 캡스톤 묶음 끝에 항목을 넣는다. 묶음이 없으면 None."""
    text = OLD_GROUP_RE.sub("", text)
    text = ITEM_RE.sub("", text)
    found = GROUP_RE.search(text)
    if not found:
        return None
    item = NAV_ITEM.format(
        group=GROUP, number=NUMBER, nav_title=NAV_TITLE, title=TITLE, page=PAGE, check=CHECK,
        current=' aria-current="page"' if current else "",
    )
    items = found.group(3) + item
    group = found.group(1) + str(items.count("<li data-nav-entry")) + found.group(2) + items + found.group(4)
    return text[: found.start()] + group + text[found.end():]


def block(pattern, text, name):
    found = re.search(pattern, text, re.S)
    if not found:
        sys.exit(u"[중단] %s 에서 %s 을 찾지 못했습니다. 랩 페이지 구조가 바뀌었는지 확인하세요." % (REFERENCE_PAGE, name))
    return found.group(0)


def swap(pattern, replacement, text, name):
    out, count = re.subn(pattern, lambda _m: replacement, text, count=1, flags=re.S)
    if count != 1:
        sys.exit(u"[중단] 원본 페이지에서 %s 을 찾지 못했습니다." % name)
    return out


def build_page(reference):
    """원본 페이지의 본문에 기존 랩 페이지의 사이드바, 상단 바, 이동 링크, 바닥글을 입힌다."""
    page = read(os.path.join(SOURCE, PAGE + ".html"))
    aside = block(r'<aside id="course-nav".*?</aside>', reference, u"사이드바").replace(' aria-current="page"', "")
    aside = place_nav(aside, True)
    if aside is None:
        sys.exit(u"[중단] 사이드바에서 「%s」 묶음을 찾지 못했습니다." % GROUP)

    topbar = block(r'<header class="topbar">.*?</header>', reference, u"상단 바")
    topbar, count = re.subn(
        r'(<nav class="breadcrumb"[^>]*>.*?<span aria-hidden="true">/</span><span>)[^<]*(</span></nav>)',
        lambda m: m.group(1) + u"%s · %s" % (GROUP, NUMBER) + m.group(2), topbar, count=1, flags=re.S,
    )
    if count != 1:
        sys.exit(u"[중단] 상단 바에서 현재 위치 표시를 찾지 못했습니다.")

    page = swap(r'<aside id="course-nav".*?</aside>', aside, page, u"사이드바")
    page = swap(r'<header class="topbar">.*?</header>', topbar, page, u"상단 바")
    page = swap(r'<nav class="page-pagination".*?</nav>', block(r'<nav class="page-pagination".*?</nav>', reference, u"이동 링크"), page, u"이동 링크")
    page = swap(r'<footer class="site-footer">.*?</footer>', block(r'<footer class="site-footer">.*?</footer>', reference, u"바닥글"), page, u"바닥글")
    page = swap(r'data-course-key="[^"]+"', block(r'data-course-key="[^"]+"', reference, u"과정 키"), page, u"과정 키")
    return page


def update_nav(path):
    text = read(path)
    placed = place_nav(text, False)
    if placed is None:
        return "건너뜀(사이드바 구조가 다름)"
    if placed == text:
        return "그대로"
    write(path, placed)
    return "고침"


def update_portal(path):
    text = read(path)
    new = OLD_SECTION_RE.sub("", text).replace(OLD_TOC_ITEM, "").replace(OLD_META[0], OLD_META[1])
    new = CARD_RE.sub("", new)
    if new.count(CARD_ANCHOR) != 1:
        return "건너뜀(포털 구조가 다름)"
    new = new.replace(CARD_ANCHOR, CARD + CARD_ANCHOR)
    if new == text:
        return "그대로"
    write(path, new)
    return "고침"


def main():
    if not os.path.isfile(os.path.join(LAB, REFERENCE_PAGE)):
        sys.exit(u"[중단] %s 에 %s 가 없습니다. 랩 폴더 경로를 확인하세요." % (LAB, REFERENCE_PAGE))

    results = {}
    for name in sorted(os.listdir(LAB)):
        if name.endswith(".html") and name != PAGE + ".html":
            results.setdefault(update_nav(os.path.join(LAB, name)), []).append(name)
    for state, names in sorted(results.items()):
        print(u"사이드바 %s: %d개%s" % (state, len(names), "" if state in (u"고침", u"그대로") else " " + ", ".join(names)))

    write(os.path.join(LAB, PAGE + ".html"), build_page(read(os.path.join(LAB, REFERENCE_PAGE))))
    print(u"페이지: %s.html (%s · %s)" % (PAGE, GROUP, NUMBER))

    os.makedirs(os.path.join(LAB, "assets", "legacy"), exist_ok=True)
    shutil.copyfile(
        os.path.join(SOURCE, "assets", "legacy", PAGE + ".css"), os.path.join(LAB, "assets", "legacy", PAGE + ".css")
    )
    images = os.path.join(LAB, "assets", "day1-lab")
    if os.path.isdir(images):
        shutil.rmtree(images)
    shutil.copytree(os.path.join(SOURCE, "assets", "day1-lab"), images)
    print(u"자산: assets/legacy/%s.css, assets/day1-lab/ (%d개)" % (PAGE, len(os.listdir(images))))
    print(u"포털: %s" % update_portal(os.path.join(LAB, "index.html")))


if __name__ == "__main__":
    main()
