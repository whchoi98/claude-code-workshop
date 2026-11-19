"""Seoul Data 실습 구조 (16:9, 라이트와 다크).

랩 페이지 본문에서는 절반쯤으로 줄어 보이므로 글자를 기본보다 크게 잡는다.
색은 담당으로 고정한다: orange 사람, purple Claude, blue 정해진 도구, yellow 자료, pink 실패와 금지, green 허용.
"""
from infokit import CODE_FAMILY, Doc, card, check, cross, cw, footer_note, header, para, rw, section, tag

T = dict(
    title="Seoul Data 실습 구조",
    sub_en="One Request, Three Reports",
    sub_ko="한 줄 요청이 세 가지 보고로 바뀌는 경로",
    chip="CAPSTONE 7 / SEOUL DATA",
    s1=("요청에서 결과까지", "Claude는 자료만 작성, 결과물은 도구가 생성"),
    # (담당, 색, 제목, [(문구, 코드 여부), ...])
    flow=[
        ("참가자", "orange", "한 줄 요청", [("/seoul-kit:board", True), ("장소와 주제 지정", False)]),
        ("Skill", "purple", "순서 안내", [("SKILL.md", True), ("작업 순서와 규칙", False)]),
        ("Claude", "purple", "자료 수집", [("서울 MCP 우선,", False), ("웹과 예비 자료", False)]),
        ("Claude", "purple", "자료 파일 작성", [("work/이름.json", True), ("숫자와 문구만 기록", False)]),
        ("도구", "blue", "검사와 생성", [("kit.py", True), ("규칙 검사 후 생성", False)]),
        ("결과", "orange", "결과 보관함", [("out/", True), ("HTML, xlsx, pptx", False)]),
    ],
    # (첫 칸, 끝 칸, 색, 문구)
    zones=[
        (0, 0, "orange", "사람: 요청과 판단"),
        (1, 3, "purple", "Claude: 자료 수집과 자료 파일 작성"),
        (4, 5, "blue", "도구: 규칙 검사와 파일 생성"),
    ],
    retry="검사 실패 시 자료만 수정",
    s2=("자료 출처", "위에서부터 차례로 사용"),
    sources=[
        ("서울 MCP", "실시간 인구, 혼잡도, 지하철, 대기질"),
        ("WebSearch, WebFetch", "MCP에 없는 자료, 직접 연 페이지의 숫자만"),
        ("예비 자료", "미리 받아 둔 응답 15개, 응답 없을 때 사용"),
    ],
    s3=("seoul-kit 플러그인", "Skill 3개와 공용 도구"),
    skills=[
        ("M1", "/seoul-kit:board", "HTML 현황판", "숫자 카드, 신호등, 정렬 표"),
        ("M2", "/seoul-kit:sheet", "Excel 통계표", "수식, 색 눈금, 차트, 출처 시트"),
        ("M3", "/seoul-kit:deck", "PowerPoint 브리핑", "큰 숫자, 차트, 표, 발표자 노트"),
    ],
    m4=("M4", "내 팀 지표에 적용, 내 Skill로 저장"),
    s4=("규칙과 권한", "틀린 자료와 위험한 명령 차단"),
    rules=("자료 검사", "kit/contracts.py", ["신호등 값 4종만 허용", "수식 함수 9종만 허용", "실패 시 고칠 칸 안내"]),
    perms=("권한 설정", ".claude/settings.json", "허용: 서울 MCP, 웹 검색, python3", "금지: .env 읽기, rm -rf, curl, sudo"),
    s5=("150분 진행", "각자 자기 속도로 진행"),
    # (이름, 분, 미션 여부)
    plan=[("준비", 10, False), ("M1 현황판", 35, True), ("M2 통계표", 40, True), ("휴식", 10, False),
          ("M3 브리핑", 40, True), ("M4 내 업무로", 15, True)],
    note="시간은 랩 가이드의 미션별 배정, 2026.11 기준",
)

TS, KS = 30, 21   # 섹션 제목, 요지


def s1(d, x, y, w, h):
    section(d, x, y, w, h, 1, *T["s1"], tsize=TS, ksize=KS)
    ix, iw, gap = x + 24, w - 48, 36
    n = len(T["flow"])
    nw, nh, ny = (iw - gap * (n - 1)) / n, 150, y + 96
    left = [ix + i * (nw + gap) for i in range(n)]
    for i, (who, color, title, lines) in enumerate(T["flow"]):
        nx, box = left[i], (left[i], ny, nw, nh)
        card(d, nx, ny, nw, nh, stroke=color, sw=1.8, fill="panel")
        tag(d, nx + 16, ny + 14, who, color, 16, 28, 12, box=box)
        d.text(nx + 16, ny + 80, title, 26, 700, "text", box=box)
        for j, (txt, code) in enumerate(lines):
            if code:
                d.text(nx + 16, ny + 110 + j * 27, txt, 18, 400, "text", box=box, family=CODE_FAMILY)
            else:
                d.text(nx + 16, ny + 110 + j * 27, txt, 19, 400, "text2", box=box)
        if i < n - 1:
            d.arrow([(nx + nw + 5, ny + nh / 2), (nx + nw + gap - 5, ny + nh / 2)], sw=2.2)
    # 검사 실패 시 되돌아가는 길: 도구(5번째)에서 자료 파일(4번째)로
    a, b = left[4] + nw / 2, left[3] + nw / 2
    d.arrow([(a, ny - 3), (a, ny - 22), (b, ny - 22), (b, ny - 4)], color="pink", sw=2.0, dash="7 6")
    d.text((a + b) / 2, ny - 31, T["retry"], 18, 700, "pink", "middle", box=(x, y, w, h))
    # 담당 구간
    by = ny + nh + 16
    for first, last, color, label in T["zones"]:
        x1, x2 = left[first], left[last] + nw
        d.path(f"M{x1:.1f},{by - 7:.1f} L{x1:.1f},{by:.1f} L{x2:.1f},{by:.1f} L{x2:.1f},{by - 7:.1f}", stroke=color, sw=2.2)
        d.text((x1 + x2) / 2, by + 31, label, 20, 700, color, "middle", box=(x, y, w, h))


def s2(d, x, y, w, h):
    cy = section(d, x, y, w, h, 2, *T["s2"], tsize=TS, ksize=KS)
    box, ix, iw = (x, y, w, h), x + 24, w - 48
    rh = (y + h - 18 - cy - 8) / len(T["sources"])
    mids = [cy + 8 + i * rh + rh / 2 for i in range(len(T["sources"]))]
    for m1, m2 in zip(mids, mids[1:]):
        d.line(ix + 17, m1 + 21, ix + 17, m2 - 21, stroke="line2", sw=2)
    for i, ((name, desc), mid) in enumerate(zip(T["sources"], mids)):
        d.circle(ix + 17, mid, 17, fill="yellowF")
        d.text(ix + 17, mid + 7, str(i + 1), 19, 700, "onwarm", "middle")
        d.text(ix + 50, mid - 5, name, 23, 700, "text", box=box)
        para(d, ix + 50, mid + 24, iw - 50, desc, 18, 25, 400, "text2", box=box, maxl=2)


def s3(d, x, y, w, h):
    cy = section(d, x, y, w, h, 3, *T["s3"], tsize=TS, ksize=KS)
    box, ix, iw = (x, y, w, h), x + 24, w - 48
    rh = 82
    for i, (mission, cmd, out, desc) in enumerate(T["skills"]):
        mid = cy + 8 + i * rh + rh / 2
        tag(d, ix, mid - 26, mission, "orange", 15, 28, 10, box=box)
        cx = ix + 60
        d.text(cx, mid - 5, cmd, 19, 400, "text", box=box, family=CODE_FAMILY)
        ax = cx + cw(cmd, 19) + 12
        d.arrow([(ax, mid - 11), (ax + 34, mid - 11)], sw=2.0)
        d.text(ax + 46, mid - 4, out, 22, 700, "text", box=box)
        d.text(cx, mid + 24, desc, 18, 400, "text2", box=box)
    mission, text = T["m4"]
    ny = y + h - 52
    d.line(ix, ny - 12, ix + iw, ny - 12, stroke="cardline", sw=1.2)
    tag(d, ix, ny, mission, "orange", 15, 28, 10, box=box)
    d.text(ix + 60, ny + 21, text, 19, 400, "text", box=box)


def s4(d, x, y, w, h):
    cy = section(d, x, y, w, h, 4, *T["s4"], tsize=TS, ksize=KS)
    box, ix = (x, y, w, h), x + 24
    name, where, lines = T["rules"]
    tw_ = tag(d, ix, cy + 6, name, "blue", 16, 28, 12, box=box)
    d.text(ix + tw_ + 12, cy + 26, where, 17, 400, "muted", box=box, family=CODE_FAMILY)
    for i, ln in enumerate(lines):
        ly = cy + 70 + i * 34
        check(d, ix + 2, ly - 15, 16)
        d.text(ix + 32, ly, ln, 20, 400, "text2", box=box)
    name, where, allow, deny = T["perms"]
    py = cy + 70 + len(lines) * 34 + 6
    tw_ = tag(d, ix, py, name, "purple", 16, 28, 12, box=box)
    d.text(ix + tw_ + 12, py + 20, where, 17, 400, "muted", box=box, family=CODE_FAMILY)
    check(d, ix + 2, py + 49, 16)
    d.text(ix + 32, py + 64, allow, 20, 400, "text2", box=box)
    cross(d, ix + 3, py + 84, 14)
    d.text(ix + 32, py + 98, deny, 20, 400, "text2", box=box)


def s5(d, x, y, w, h):
    section(d, x, y, w, h, 5, *T["s5"], tsize=TS, ksize=KS)
    ix, iw, gap = x + 24, w - 48, 4
    total = sum(m for _, m, _ in T["plan"])
    unit = (iw - gap * (len(T["plan"]) - 1)) / total
    sy, sh, cx = y + 68, 50, ix
    for name, minutes, mission in T["plan"]:
        sw_ = unit * minutes
        if mission:
            d.rect(cx, sy, sw_, sh, rx=8, fill="orangeF", fo=0.16, stroke="orange", sw=1.4)
        else:
            d.rect(cx, sy, sw_, sh, rx=8, fill="panel", stroke="line2", sw=1.4)
        d.text(cx + sw_ / 2, sy + 32, f"{name} {minutes}분", 18, 700, "text" if mission else "muted", "middle",
               box=(cx - 5, sy, sw_ + 10, sh))
        cx += sw_ + gap


def landscape(theme):
    d = Doc(1920, 1080, theme)
    d.rect(0, 0, 1920, 1080, fill="bg")
    header(d, 48, 80, T["title"], T["sub_en"], T["sub_ko"], tsize=50, ssize=25, kosize=22)
    cwid = rw(T["chip"], 15, 700) + 28
    tag(d, 1872 - cwid, 46, T["chip"], "orange", 15, 30, 14)
    y1, h1, g, h2, h5 = 152, 330, 18, 386, 136
    s1(d, 48, y1, 1824, h1)
    y2, w3 = y1 + h1 + g, (1824 - 2 * 20) / 3
    s2(d, 48, y2, w3, h2)
    s3(d, 48 + w3 + 20, y2, w3, h2)
    s4(d, 48 + 2 * (w3 + 20), y2, w3, h2)
    s5(d, 48, y2 + h2 + g, 1824, h5)
    footer_note(d, 1872, 1066, T["note"], size=15)
    return d.svg()
