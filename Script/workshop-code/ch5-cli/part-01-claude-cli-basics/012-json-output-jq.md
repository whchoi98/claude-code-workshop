# Slide 12: JSON 출력 파싱 (jq)

**Part 1: claude 명령 기본**

## Code Blocks

### jq patterns

```bash
# 1. 결과만 추출
$ claude -p "..." --output-format json | jq -r '.result'

# 2. 토큰 사용량 추출
$ claude -p "..." --output-format json | \
    jq '.usage | {in: .input_tokens, out: .output_tokens}'

# 3. 응답 시간 측정 (밀리초 → 초)
$ claude -p "..." --output-format json | \
    jq '.duration_ms / 1000'

# 4. 결과를 다음 명령에 전달
$ RESULT=$(claude -p "Python 정렬 알고리즘 추천" \
    --output-format json | jq -r '.result')
$ echo "$RESULT" > recommendation.md

# 5. 비용 계산 (단가 가정)
$ claude -p "..." --output-format json | jq '
    .usage as $u |
    ($u.input_tokens * 0.003 + $u.output_tokens * 0.015) / 1000
  '

# 6. 에러 확인
$ RESPONSE=$(claude -p "..." --output-format json)
$ SUBTYPE=$(echo "$RESPONSE" | jq -r '.subtype')
$ if [ "$SUBTYPE" != "success" ]; then
    ERROR=$(echo "$RESPONSE" | jq -r '.error // "unknown"')
    echo "Failed: $ERROR" >&2
    exit 1
  fi
```

## Speaker Notes

JSON 출력 파싱의 jq 6가지 핵심 패턴입니다.
첫째, 결과만 추출입니다.
jq -r .result로 응답 텍스트만 가져옵니다.
-r은 raw 출력으로 따옴표를 제거합니다.
둘째, 토큰 사용량 추출입니다.
usage 필드에서 input_tokens와 output_tokens를 추출합니다.
셋째, 응답 시간 측정입니다.
duration_ms를 1000으로 나눠 초 단위로 변환합니다.
넷째, 결과를 다음 명령에 전달합니다.
shell 변수로 저장한 후 echo로 파일에 쓰거나 다른 명령에 전달합니다.
다섯째, 비용 계산입니다.
입력 토큰과 출력 토큰의 단가를 곱해 비용을 자동 계산할 수 있습니다.
여섯째, 에러 확인입니다.
subtype 필드가 success인지 확인하고 그렇지 않으면 error 메시지를 추출해 stderr로 출력하고 exit 1로 종료합니다.
이 6가지 패턴이 자동화 스크립트의 기본이 됩니다.
