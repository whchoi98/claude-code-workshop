# Slide 47: 실시간 진행 표시

**Part 3: 출력 형식과 파싱 심화**

## Code Blocks

### progress

```bash
#!/bin/bash
# progress.sh - 실시간 진행 표시

claude -p "큰 작업: 모든 .py 파일 분석 후 리포트 생성" \
  --output-format stream-json | \
while IFS= read -r line; do
  TYPE=$(echo "$line" | jq -r '.type')
  case "$TYPE" in
    system)
      MODEL=$(echo "$line" | jq -r '.model')
      echo "🚀 Started (model: $MODEL)"
      ;;
    tool_use)
      NAME=$(echo "$line" | jq -r '.name')
      INPUT=$(echo "$line" | jq -c '.input')
      echo "🔧 $NAME: $INPUT"
      ;;
    tool_result)
      IS_ERR=$(echo "$line" | jq -r '.is_error')
      if [ "$IS_ERR" = "true" ]; then
        echo "  ❌ 도구 실패"
      else
        echo "  ✓ 결과 수신"
      fi
      ;;
    text_delta)
      DELTA=$(echo "$line" | jq -r '.delta')
      echo -n "$DELTA"
      ;;
    result)
      SUBTYPE=$(echo "$line" | jq -r '.subtype')
      DURATION=$(echo "$line" | jq '.duration_ms')
      TOKENS=$(echo "$line" | jq '.usage.output_tokens')
      echo ""
      echo "═════════════════"
      echo "✓ 완료 [$SUBTYPE]"
      echo "  시간: ${DURATION}ms"
      echo "  토큰: $TOKENS"
      ;;
  esac
done

# 결과 예시:
# 🚀 Started (model: claude-sonnet-4-5)
# 🔧 Read: {"file_path": "src/app.py"}
#   ✓ 결과 수신
# 🔧 Read: {"file_path": "src/utils.py"}
#   ✓ 결과 수신
# 분석 결과...
# ═════════════════
# ✓ 완료 [success]
```

## Speaker Notes

실시간 진행 표시 스크립트입니다.
stream-json 출력을 while 루프로 한 줄씩 읽어 처리합니다.
type에 따라 5가지 케이스로 분기합니다.
system 이벤트는 세션 시작 시 한 번 발생하며 모델 정보를 표시합니다.
tool_use 이벤트는 도구 호출 시작입니다.
도구 이름과 입력 파라미터를 함께 표시해 어떤 작업이 진행 중인지 알립니다.
tool_result 이벤트는 도구 결과입니다.
is_error 필드를 확인해 성공이나 실패 표시를 다르게 합니다.
text_delta 이벤트는 텍스트 청크입니다.
echo -n으로 줄바꿈 없이 이어 붙여 ChatGPT같은 타이핑 효과를 만듭니다.
result 이벤트는 최종 완료입니다.
구분선과 함께 소요 시간과 토큰 사용량을 정리해서 보여줍니다.
실행 시 작업이 진행되는 모습이 실시간으로 보여 UX가 크게 개선됩니다.
