# Slide 38: stream-json 이벤트 타입 전체

**Part 3: 출력 형식과 파싱 심화**

## Code Blocks

### stream events

```bash
# stream-json은 한 줄 당 하나의 JSON 이벤트

# 이벤트 1: system (세션 시작)
{"type":"system","subtype":"init","session_id":"ses_...",
 "model":"claude-sonnet-4-5","cwd":"/path/to/project"}

# 이벤트 2: message (모델 응답 청크)
{"type":"message","role":"assistant",
 "content":[{"type":"text","text":"이 코드를 분석..."}],
 "stop_reason":null}

# 이벤트 3: tool_use (도구 호출 시작)
{"type":"tool_use","id":"toolu_abc",
 "name":"Read",
 "input":{"file_path":"/path/to/file.js"}}

# 이벤트 4: tool_result (도구 호출 결과)
{"type":"tool_result","tool_use_id":"toolu_abc",
 "content":"...파일 내용...",
 "is_error":false}

# 이벤트 5: text_delta (스트리밍 텍스트 청크)
{"type":"text_delta","delta":"분"}
{"type":"text_delta","delta":"석"}
{"type":"text_delta","delta":" 결과"}

# 이벤트 6: result (최종 완료)
{"type":"result","subtype":"success",
 "result":"전체 응답...","duration_ms":2840,
 "usage":{...}}

# 처리 패턴
$ claude -p "..." --output-format stream-json | \
    while IFS= read -r line; do
      TYPE=$(echo "$line" | jq -r '.type')
      case "$TYPE" in
        tool_use)    echo "🔧 $(echo "$line" | jq -r '.name')" ;;
        text_delta)  echo -n "$(echo "$line" | jq -r '.delta')" ;;
        result)      echo "✓ 완료" ;;
      esac
    done
```

## Speaker Notes

stream-json 이벤트 타입을 정리합니다.
한 줄 당 하나의 JSON 이벤트로 출력됩니다.
6가지 주요 이벤트 타입이 있습니다.
이벤트 1은 system으로 세션 시작 시 전송됩니다.
session_id, model, cwd 같은 메타데이터를 포함합니다.
이벤트 2는 message로 모델 응답 청크입니다.
content 배열에 text 객체가 들어 있습니다.
이벤트 3은 tool_use로 도구 호출 시작입니다.
id, name, input을 포함합니다.
이벤트 4는 tool_result로 도구 호출 결과입니다.
tool_use_id로 매칭하고 content에 결과 내용이 옵니다.
이벤트 5는 text_delta로 스트리밍 텍스트 청크입니다.
사용자가 실시간으로 응답을 받는 인상을 줍니다.
이벤트 6은 result로 최종 완료입니다.
JSON 모드와 동일한 형식의 종료 메시지입니다.
처리 패턴은 while read 루프로 한 줄씩 받아 type에 따라 분기합니다.
도구 호출은 이모지로, 텍스트는 그대로 출력, 결과는 완료 표시 같은 식입니다.
