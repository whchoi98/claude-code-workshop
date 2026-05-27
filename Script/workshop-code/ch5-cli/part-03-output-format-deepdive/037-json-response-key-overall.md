# Slide 37: JSON 응답 스키마 전체

**Part 3: 출력 형식과 파싱 심화**

## Code Blocks

### JSON schema

```bash
# 성공 응답 (subtype: success)
{
  "type": "result",
  "subtype": "success",
  "result": "...실제 응답 텍스트...",
  "session_id": "ses_01HXYZ...",
  "duration_ms": 2840,
  "model": "claude-sonnet-4-5",
  "usage": {
    "input_tokens": 1523,
    "output_tokens": 487,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0
  },
  "stop_reason": "end_turn",
  "num_turns": 3,
  "is_error": false
}

# 에러 응답 (subtype: error)
{
  "type": "result",
  "subtype": "error",
  "error": "Tool 'WebFetch' not allowed",
  "error_code": "permission_denied",
  "session_id": "ses_01HXYZ...",
  "duration_ms": 120,
  "is_error": true
}

# 일부 응답 (subtype: max_turns_reached)
{
  "type": "result",
  "subtype": "max_turns_reached",
  "result": "...부분 응답...",
  "session_id": "...",
  "num_turns": 30,
  "is_error": false
}

# subtype 종류
# - success           정상 완료
# - error             도구/권한/내부 오류
# - max_turns_reached --max-turns 도달
# - max_tokens_reached --max-tokens 도달
```

## Speaker Notes

JSON 응답 스키마의 모든 필드를 정리합니다.
성공 응답은 subtype이 success입니다.
type은 result로 고정이고 subtype으로 세부 분류합니다.
result 필드에 실제 응답 텍스트가 들어 있습니다.
session_id는 세션 재사용에 사용하고 duration_ms는 응답 시간입니다.
model은 사용된 모델 ID입니다.
usage 객체에 input_tokens, output_tokens가 있고 캐시 관련 두 필드가 추가로 있습니다.
stop_reason은 응답이 왜 끝났는지 알려줍니다.
num_turns는 도구 호출 횟수, is_error는 오류 여부 boolean입니다.
에러 응답은 subtype이 error이고 error 필드에 메시지, error_code에 분류 코드가 옵니다.
일부 응답은 max_turns_reached 또는 max_tokens_reached로 제한에 걸린 경우입니다.
부분 결과가 result에 들어 있어 활용할 수 있습니다.
subtype 4종을 정확히 이해하면 어떤 결과든 분기 처리 가능합니다.
