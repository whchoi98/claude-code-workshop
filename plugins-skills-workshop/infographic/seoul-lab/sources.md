# 실습 구조 그림의 사실 확인

그림(`structure.py`의 `T`)에 적은 내용과 그 근거다. 모두 이 저장소 안의 파일에서 확인했다. 내용이 바뀌면 `T`를 고치고 다시 빌드한다.

| 그림의 내용 | 값 | 근거 |
|---|---|---|
| Skill 세 개와 결과물 | `board`는 HTML 현황판, `sheet`는 Excel 통계표, `deck`은 PowerPoint 브리핑 | `marketplace/plugins/seoul-kit/skills/*/SKILL.md` |
| Claude가 쓰는 것 | `work/<이름>.json` 자료 파일 하나 | 각 `SKILL.md`의 절차 |
| 결과물을 만드는 것 | `kit/kit.py`가 검사한 뒤 `out/`에 생성 | `marketplace/plugins/seoul-kit/kit/kit.py` |
| 자료 출처 순서 | 서울 MCP, 웹(WebSearch, WebFetch), 미리 받아 둔 자료 | `kit/data-guide.md` 1절 |
| 예비 자료 수 | 15개 | `workspace/data/seoul-sample/` |
| 신호등 값 | green, yellow, red, none 4종 | `kit/contracts.py` |
| 수식 함수 | SUM, AVERAGE, MAX, MIN, ROUND, IF, RANK, ABS, COUNT 9종 | `kit/contracts.py`의 `FUNCTIONS` |
| 권한 | 허용 `mcp__seoul`, `WebSearch`, `WebFetch`, `Bash(python3:*)`, 금지 `Read(./.env)`, `Bash(rm -rf:*)`, `Bash(curl:*)`, `Bash(sudo:*)` | `workspace/.claude/settings.json` |
| 진행 시간 | 준비 10, M1 35, M2 40, 휴식 10, M3 40, M4 15, 합계 150분 | `lab/ClaudeCode_Day1_SeoulData_HandsOnLab.html`의 미션별 시간과 M2 끝의 쉬는 시간 |

## 다시 빌드하기

`my-plugins:aws-infographic` 스킬의 `infokit.py`, `buildkit.py`를 이 폴더에 복사한 뒤 실행한다. 두 파일과 `build/`는 저장소에 올리지 않는다.

```bash
uv run --no-project --with playwright==1.64.1 --with pillow python buildkit.py build structure:seoul-lab-structure
cp build/seoul-lab-structure_16x9_light.png ../../lab/assets/day1-lab/structure-light.png
cp build/seoul-lab-structure_16x9_dark.png  ../../lab/assets/day1-lab/structure-dark.png
python3 ../../scripts/add-lab-to-workshop.py
```
