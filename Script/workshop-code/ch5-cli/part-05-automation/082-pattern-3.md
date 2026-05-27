# Slide 82: Pattern 3 / 실패 분석

**Part 5: 자동화 패턴**

## Code Blocks

### analyze-failures.sh

```bash
#!/bin/bash
# analyze-failures.sh - 마이그레이션 실패 파일 분석

mkdir -p .migration/analysis

# 각 실패 파일 분석
for backup in .migration/failed/*; do
  ORIG_NAME=$(basename "$backup" | tr '_' '/')
  OUT=".migration/analysis/$(basename "$backup" .failed).md"

  claude -p "$(cat <<EOF
다음 코드 변환이 테스트 실패했습니다. 이유를 분석:

원본 파일 위치: $ORIG_NAME

변환 시도 코드:
$(cat "$backup")

분석 요청:
1. 변환 실패 원인 (테스트 에러 메시지 포함)
2. 어느 부분이 문제인가
3. 수정 방법 제안 (3가지 옵션)
4. 사람의 검토가 필요한 이유
5. 다음 시도 시 변환 규칙에 추가할 예외

출력 형식: Markdown 보고서
EOF
)" \
    --allowed-tools "Read,Bash(npm test:*)" \
    --max-turns 10 \
    --output-format json | jq -r '.result' > "$OUT"

  echo "✓ 분석 완료: $OUT"
done

# 통합 보고서
{
  echo "# 마이그레이션 실패 분석 보고서"
  echo "생성: $(date)"
  echo ""
  echo "## 통계"
  echo "- 실패 파일: $(ls .migration/failed | wc -l)개"
  echo "- 성공 파일: $(ls .migration/success | wc -l)개"
  echo ""
  echo "## 파일별 분석"
  for f in .migration/analysis/*.md; do
    echo ""
    echo "### $(basename "$f" .md)"
    cat "$f"
    echo ""
    echo "---"
  done
} > .migration/REPORT.md

echo "✓ 종합 보고서: .migration/REPORT.md"
```

## Speaker Notes

Pattern 3의 실패 분석 스크립트입니다.
.migration/analysis 디렉토리를 만듭니다.
각 실패 파일에 대해 분석을 수행합니다.
파일명에서 원본 경로를 복원합니다.
claude에게 5가지 분석을 요청합니다.
변환 실패 원인을 테스트 에러 메시지와 함께 분석합니다.
어느 부분이 문제인지 명확히 짚어줍니다.
수정 방법을 3가지 옵션으로 제안합니다.
사람의 검토가 왜 필요한지 설명합니다.
다음 시도 시 변환 규칙에 추가할 예외 사항을 제안합니다.
allowed-tools에 Read와 npm test 명령을 허용해 실제 테스트 실행이 가능합니다.
각 파일별 분석 보고서를 마크다운으로 저장합니다.
마지막에 모든 분석을 한 통합 보고서로 합칩니다.
REPORT.md에 통계와 파일별 분석이 모두 포함됩니다.
사람이 이 보고서만 보면 어떤 파일을 수동 처리해야 하는지 즉시 알 수 있습니다.
반복 마이그레이션 시 규칙을 점진 개선하는 데이터 기반이 됩니다.
