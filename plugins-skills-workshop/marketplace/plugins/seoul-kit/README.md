# seoul-kit

서울 열린데이터(서울 MCP)와 웹 자료로 업무용 산출물 세 가지를 만드는 Claude Code 플러그인이다.

| Skill | 만드는 것 | 예 |
|---|---|---|
| `/seoul-kit:board` | HTML 현황판 | `/seoul-kit:board 강남역, 여의도, 성수` |
| `/seoul-kit:sheet` | Excel 통계표 | `/seoul-kit:sheet 강남역 2호선 시간대별 승하차` |
| `/seoul-kit:deck` | PowerPoint 브리핑 | `/seoul-kit:deck 강남역 저녁 유동 브리핑` |

## 폴더

- `skills/`: Skill마다 설명서(`SKILL.md`)가 하나씩 있다.
- `kit/kit.py`: 자료(JSON)를 검사하고 파일을 만드는 도구.
- `kit/contracts.py`: 자료가 지켜야 할 규칙표.
- `kit/board_template.html`: 현황판 화면 틀.
- `kit/data-guide.md`: 숫자를 어디서 가져오고 어떻게 다루는지 적은 공통 지침.
- `kit/examples/`: 실제 서울 데이터로 만든 예시 자료 세 개.

## 필요한 것

- Python 3.9 이상
- 통계표에는 `openpyxl`, 브리핑에는 `python-pptx`. `python3 kit/kit.py doctor`로 확인한다.
- `seoul`이라는 이름으로 등록한 서울 MCP 서버. 없어도 사용자가 준 자료로는 동작한다.

## 도구만 따로 쓰기

```bash
python3 kit/kit.py example board > my.json
python3 kit/kit.py board my.json
python3 kit/kit.py rules board
```
