# Slide 11: 출력 형식 옵션

**Part 1: claude 명령 기본**

## Code Blocks

### --output-format

```bash
# 1. text (기본값) - 사람이 읽기 좋음
$ claude -p "Python의 list comprehension 설명"
# 출력: 일반 마크다운 텍스트

# 2. json - 구조화 데이터 (스크립트용)
$ claude -p "..." --output-format json
{
  "type": "result",
  "subtype": "success",
  "result": "...",
  "session_id": "ses_abc123",
  "usage": {
    "input_tokens": 152,
    "output_tokens": 384
  },
  "duration_ms": 2840
}

# 3. stream-json - 실시간 스트림 (UI/CI용)
$ claude -p "..." --output-format stream-json
{"type":"system","subtype":"init","session_id":"..."}
{"type":"message","role":"assistant","content":"Pyt"}
{"type":"message","role":"assistant","content":"hon "}
{"type":"tool_use","tool":"Read","input":{...}}
{"type":"tool_result","content":"..."}
{"type":"result","subtype":"success","duration_ms":2840}

# 사용 패턴
# - text: 사람 읽기, 빠른 확인
# - json: 스크립트 파싱, 결과만 필요할 때
# - stream-json: 실시간 진행 표시, 토큰별 처리
```

## Speaker Notes

출력 형식 옵션의 3가지 모드를 비교합니다.
첫째, text는 기본값이며 사람이 읽기 좋은 형식입니다.
일반 마크다운 텍스트로 출력됩니다.
둘째, json은 구조화 데이터 형식입니다.
스크립트로 결과를 파싱할 때 사용합니다.
type, subtype, result, session_id, usage, duration_ms 같은 필드가 모두 포함됩니다.
토큰 사용량과 응답 시간을 정확히 추출할 수 있습니다.
셋째, stream-json은 실시간 스트림입니다.
각 메시지, 도구 호출, 결과가 한 줄씩 JSON으로 출력됩니다.
UI에서 실시간 진행을 보여주거나 CI에서 점진 처리할 때 유용합니다.
사용 패턴은 명확합니다.
text는 사람이 빠르게 확인할 때, json은 스크립트가 결과만 필요할 때, stream-json은 실시간 진행 표시가 필요할 때 사용합니다.
