# Slide 44: 다중 호출 집계

**Part 3: 출력 형식과 파싱 심화**

## Code Blocks

### aggregation

```bash
#!/bin/bash
# batch-analyze.sh - 여러 파일 분석 후 통합

mkdir -p results

# 1. 각 파일을 개별 분석 (병렬)
analyze_one() {
  local f="$1"
  local out="results/$(basename "$f").json"
  claude -p "다음 코드를 분석. 결과는 JSON: \
    {complexity: 1-10, issues: [], suggestions: []}" \
    --output-format json \
    < "$f" > "$out"
}
export -f analyze_one
find src/ -name "*.js" | parallel -j 4 analyze_one

# 2. 결과 집계 (jq slurp)
jq -s '
  # 모든 분석 결과의 .result를 JSON으로 파싱
  map(.result | fromjson) as $analyses |

  {
    total_files: ($analyses | length),
    avg_complexity: ([$analyses[].complexity] | add / length),
    high_complexity: [
      $analyses[] | select(.complexity > 7) |
      {file: input_filename, complexity}
    ],
    total_issues: ([$analyses[].issues[]] | length),
    common_issues: ([$analyses[].issues[]]
      | group_by(.)
      | map({issue: .[0], count: length})
      | sort_by(-.count) | .[0:5])
  }
' results/*.json > summary.json

# 3. Markdown 리포트로 변환
jq -r '
  "# 코드 품질 분석 결과\n" +
  "\n분석 파일: \(.total_files)개" +
  "\n평균 복잡도: \(.avg_complexity)" +
  "\n총 이슈: \(.total_issues)개" +
  "\n\n## 자주 발견된 이슈 Top 5\n" +
  ([.common_issues[] | "- \(.issue) (\(.count)건)"] | join("\n"))
' summary.json > REPORT.md

echo "✓ 보고서: REPORT.md"
```

## Speaker Notes

다중 호출 결과 집계 패턴입니다.
batch-analyze.sh로 여러 파일을 분석한 후 결과를 통합합니다.
1단계 각 파일을 병렬로 개별 분석합니다.
analyze_one 함수에서 claude에게 JSON 형식으로 결과를 요청합니다.
complexity 점수, 이슈 배열, 제안 배열이 포함된 구조입니다.
parallel -j 4로 4개씩 동시 처리합니다.
2단계 결과 집계는 jq slurp으로 합니다.
모든 .result를 fromjson으로 파싱해서 JSON 객체 배열로 만듭니다.
총 파일 수, 평균 복잡도, 높은 복잡도 파일 목록, 총 이슈 수, 자주 발견된 이슈 top 5를 집계합니다.
3단계 Markdown 리포트로 변환합니다.
jq의 문자열 인터폴레이션으로 통계 값을 본문에 삽입합니다.
join 함수로 배열을 줄바꿈으로 합쳐 목록을 만듭니다.
결과적으로 사람이 읽기 좋은 통합 보고서가 자동 생성됩니다.
