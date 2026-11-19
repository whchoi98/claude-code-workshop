# Plugins & Skills 워크숍 Day 1 자료

비개발 직군을 위한 Claude Code 워크숍 Day 1의 오후 세션(Plugins & Skills 50분)과 LAB(150분) 자료다. 참가자는 서울 열린데이터를 가져와 HTML 현황판, Excel 통계표, PowerPoint 브리핑을 각자 만든다.

## 구성

| 경로 | 내용 |
|---|---|
| `marketplace/` | 플러그인 마켓플레이스. `plugins/seoul-kit`에 Skill 세 개(`board`, `sheet`, `deck`)와 공용 도구(`kit/`)가 있다 |
| `workspace/` | 참가자 작업 폴더 틀. 권한 설정, 안내 문서, 대체 데이터, 연습용 팀 지표 |
| `lab/` | 참가자용 랩 가이드(`ClaudeCode_Day1_SeoulData_HandsOnLab.html`). 기존 핸즈온 랩과 같은 디자인이며 `assets/`를 같은 폴더에 둔다 |
| `docs/session-plugins-skills.md` | 50분 세션 구성안과 시연 대본 |
| `docs/facilitator-runbook.md` | 진행자 운영안: 진행표, 사전 준비, 호출 한도, 대체 수단, 확인 범위 |
| `scripts/setup-lab.sh` | 참가자 실습 서버 한 대를 LAB 상태로 만드는 스크립트 |
| `scripts/add-lab-to-workshop.py` | 랩 가이드를 기존 핸즈온 랩(`../ccw-hands-on-lab/`)의 캡스톤 M7로 넣는 스크립트. 여러 번 실행해도 된다 |

## 빠르게 돌려 보기

```bash
bash scripts/setup-lab.sh
claude plugin marketplace add ~/workshop-kit
claude plugin install seoul-kit@workshop-kit
cd ~/seoul-lab && claude
```

Claude Code 안에서 `/seoul-kit:board 강남역, 여의도, 성수`를 실행한다. 결과는 `out/`에 생기고, 브라우저에서 code-server 주소 끝에 `/proxy/8000/`을 붙여 연다. 서울 MCP는 `seoul`이라는 이름으로 등록돼 있어야 한다.

## 기존 핸즈온 랩과의 관계

랩 가이드의 원본은 `lab/ClaudeCode_Day1_SeoulData_HandsOnLab.html`이다. `scripts/add-lab-to-workshop.py`가 이 원본에 기존 랩의 사이드바와 상단 바를 입혀 `ccw-hands-on-lab/`에 쓰고, 모든 랩 페이지 사이드바의 「캡스톤 · 프로젝트 선택」 묶음(M7 Seoul Data)과 포털의 Capstone Missions(MISSION 7)에 항목을 넣는다. 내용을 고칠 때는 `lab/`의 원본을 고친 뒤 스크립트를 다시 실행한다. 랩 페이지를 원본 덱에서 다시 생성해 항목이 사라졌을 때도 다시 실행하면 된다.

## 설계 원칙

- Claude는 자료 파일(JSON)만 쓴다. HTML, Excel, PowerPoint 파일은 `kit/kit.py`가 만든다.
- 규칙은 `kit/contracts.py` 한 곳에 있다. 규칙에 어긋난 자료는 파일을 만들기 전에 한국어 안내와 함께 막힌다.
- 숫자는 서울 MCP에서 먼저 찾고, 없는 것은 웹에서 찾아 출처를 붙인다. 둘 다 안 되면 미리 받아 둔 자료를 쓴다.

## 참고 자료에 관한 메모

이 폴더 최상위에 있는 zip 3개, HTML 2개, txt 1개는 설계할 때 참고한 외부 실습 자료이며 저작권이 있다. 아이디어만 참고했고 저장소에 올리지 않는다(`.gitignore`).
