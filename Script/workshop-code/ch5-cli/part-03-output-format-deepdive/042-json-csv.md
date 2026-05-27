# Slide 42: JSON → CSV 변환

**Part 3: 출력 형식과 파싱 심화**

## Code Blocks

### JSON to CSV

```bash
# 시나리오: 100개 응답을 CSV로 변환해 Excel 분석

# 1. 기본 CSV 변환
$ jq -r '[
    .timestamp,
    .model,
    .duration_ms,
    .usage.input_tokens,
    .usage.output_tokens,
    .is_error
  ] | @csv' all.json > responses.csv

# 2. 헤더 추가
$ {
    echo '"timestamp","model","duration_ms","input","output","error"'
    jq -r '[
      (.timestamp // ""),
      (.model // ""),
      (.duration_ms // 0),
      (.usage.input_tokens // 0),
      (.usage.output_tokens // 0),
      .is_error
    ] | @csv' all.json
  } > responses.csv

# 3. 다중 응답 → CSV (slurp 사용)
$ jq -rs '
  ["timestamp","model","duration_ms","input","output","error"],
  (.[] | [
    .timestamp,
    .model,
    .duration_ms,
    .usage.input_tokens,
    .usage.output_tokens,
    .is_error
  ])
  | @csv
' responses/*.json > responses.csv

# 4. TSV (탭 구분)
$ jq -rs '...| @tsv' all.json > responses.tsv

# 5. 비용 컬럼 추가
$ jq -r '. as $r |
  ($r.usage.input_tokens * 0.003 +
   $r.usage.output_tokens * 0.015) / 1000 as $cost |
  [$r.timestamp, $r.model, $r.duration_ms, $cost] | @csv
' all.json > with-cost.csv

# 6. Excel에서 바로 열기
$ open responses.csv      # macOS
$ start responses.csv     # Windows
```

## Speaker Notes

JSON을 CSV로 변환하는 패턴입니다.
100개 응답을 CSV로 변환해 Excel로 분석하는 시나리오입니다.
1번 기본 CSV 변환은 배열에 추출할 필드들을 나열하고 at csv 함수에 파이프합니다.
2번 헤더를 별도로 추가하면 Excel에서 자동 인식됩니다.
3번 다중 응답을 한 번에 CSV로 만들려면 -s 옵션으로 slurp합니다.
첫 줄에 헤더, 그 다음 점 대괄호로 각 응답을 펼쳐 행으로 만듭니다.
4번 TSV 즉 탭 구분 형식이 필요하면 at tsv로 바꿉니다.
5번 비용 컬럼 추가입니다.
as 연산자로 응답을 변수에 저장하고 비용을 계산해 추가합니다.
6번 Excel에서 바로 열기는 open이나 start 명령을 사용합니다.
CSV 형식이 데이터 분석의 표준이므로 이 패턴은 매우 자주 사용됩니다.
