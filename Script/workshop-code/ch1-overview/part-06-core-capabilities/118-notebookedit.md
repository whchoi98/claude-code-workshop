# Slide 118: NotebookEdit

**Part 6: CORE CAPABILITIES**

## Code Blocks

### NotebookEdit

```bash
# NotebookEdit 도구
NotebookEdit(
  notebook_path: "analysis/sales_q4.ipynb",
  cell_id: "abc-123",       # 또는 새 셀 추가
  new_source: "import pandas as pd\ndf = pd.read_csv(...)",
  cell_type: "code",        # code | markdown
  edit_mode: "replace",     # replace | insert | delete
)

# 셀 추가
NotebookEdit(
  notebook_path: "...",
  cell_id: "abc-123",       # 이 셀 다음에 삽입
  new_source: "df.describe()",
  cell_type: "code",
  edit_mode: "insert",
)

# 활용 패턴
- EDA 워크플로 자동화
- 분석 결과 보고서 작성
- ML 실험 추적
```

## Speaker Notes

NotebookEdit은 Jupyter 노트북 .ipynb 파일을 셀 단위로 편집하는 전용 도구입니다.
cell_id로 특정 셀을 지정하고 edit_mode로 replace, insert, delete 중 하나를 선택합니다.
cell_type은 code 또는 markdown입니다.
데이터 과학과 머신러닝 워크플로에 매우 유용한데, EDA, 즉 탐색적 데이터 분석 워크플로를 자동화하거나, 분석 결과 보고서를 자동 작성하거나, ML 실험을 추적할 때 사용합니다.
일반 코드 편집과 달리 Jupyter의 셀 구조를 보존하면서 작업하므로 출력 결과나 메타데이터도 함께 관리됩니다.
