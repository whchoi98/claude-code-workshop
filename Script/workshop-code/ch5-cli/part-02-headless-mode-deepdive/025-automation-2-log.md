# Slide 25: 자동화 2 / 로그 분석

**Part 2: HEADLESS 모드 심화**

## Code Blocks

### analyze-logs.sh

```bash
#!/bin/bash
# analyze-logs.sh - 로그 파일 병렬 분석
set -euo pipefail

LOG_DIR="${1:-./logs}"
OUTPUT_DIR="${2:-./analyses}"

mkdir -p "$OUTPUT_DIR"

# 각 로그 파일 분석 함수
analyze_one() {
  local file="$1"
  local out="$OUTPUT_DIR/$(basename "$file" .log).md"

  claude -p "$(cat <<EOF
다음 로그에서:
1. 에러 패턴 (빈도순 top 5)
2. 시간대별 분포
3. 의심스러운 동작
4. 권장 조치

로그 내용:
$(tail -10000 "$file")
EOF
)" \
    --model claude-haiku-4-5 \
    --max-turns 5 \
    --output-format json | jq -r '.result' > "$out"

  echo "✓ $(basename "$file")"
}

export -f analyze_one
export OUTPUT_DIR

# GNU parallel로 4개씩 병렬 실행
find "$LOG_DIR" -name "*.log" | \
  parallel -j 4 analyze_one {}

# 통합 보고서
{
  echo "# 로그 분석 통합 보고서"
  echo "분석 일시: $(date)"
  for f in "$OUTPUT_DIR"/*.md; do
    echo ""
    echo "## $(basename "$f" .md)"
    cat "$f"
  done
} > "$OUTPUT_DIR/SUMMARY.md"

echo "✓ 총 $(ls "$OUTPUT_DIR" | wc -l)개 분석 완료"
```

## Speaker Notes

자동화 2번 대량 로그 분석 스크립트입니다.
로그 디렉토리와 출력 디렉토리를 인자로 받습니다.
analyze_one 함수에서 한 파일을 분석합니다.
claude -p에 heredoc으로 분석 요청 4가지를 명시합니다.
에러 패턴 빈도순, 시간대별 분포, 의심 동작, 권장 조치를 분석합니다.
로그 내용은 tail -10000으로 마지막 만 줄만 추출합니다.
전체 파일은 너무 크므로 분할이 필요합니다.
모델은 claude-haiku-4-5로 비용을 절감합니다.
GNU parallel로 4개씩 병렬 실행합니다.
-j 4는 동시 4개 작업이고 작업이 끝나면 다음 파일을 자동 시작합니다.
마지막에 모든 개별 분석을 SUMMARY.md로 통합합니다.
로그 파일이 100개라도 25개씩 4 라운드로 빠르게 처리됩니다.
