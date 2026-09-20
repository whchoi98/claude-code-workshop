# Slide 179: Pattern 7 JSON Output

**Part 9: WORKFLOW PATTERNS**

## Code Blocks

### JSON OUTPUT

```bash
# JSON 출력 옵션
$ claude -p "현재 디렉토리 분석" --output-format json

{
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "result": "이 프로젝트는 TypeScript + Express 기반의 ... (응답 본문 전체)",
  "session_id": "46dcf366-0059-45f0-adf1-44bb058ff5d6",
  "num_turns": 3,
  "duration_ms": 27496,
  "duration_api_ms": 24912,
  "total_cost_usd": 1.392,
  "usage": {
    "input_tokens": 6, "output_tokens": 944,
    "cache_read_input_tokens": 106228, "cache_creation_input_tokens": 60777
  },
  "modelUsage": { "<model-id>": { "inputTokens": 6, "outputTokens": 944, "costUSD": 1.369 } },
  "permission_denials": [],
  "stop_reason": "end_turn"
}

# jq로 추출: 본문은 result, 비용과 세션은 최상위 메타데이터
$ claude -p "..." --output-format json | jq -r '.result'
$ claude -p "..." --output-format json | jq '{cost: .total_cost_usd, turns: .num_turns, session: .session_id}'

# 필드 단위 구조가 필요하면 프롬프트로 JSON 출력을 요구하고 result를 한 번 더 파싱
$ claude -p "... 결과를 JSON으로: {stack: [], issues: [{severity, file}]}" --output-format json \
    | jq -r '.result | fromjson | .issues'

# 스키마로 출력 계약을 고정하면 결과가 structured_output 키에 담깁니다
$ claude -p "..." --output-format json \
    --json-schema '{"type":"object","properties":{"issues":{"type":"array"}},"required":["issues"]}' \
    | jq '.structured_output.issues'
```

## Speaker Notes

JSON 출력 형식은 자동화 파이프라인에서 매우 유용합니다.
--output-format json 플래그를 주면 응답 본문(result)과 함께 세션 ID, 턴 수, 소요 시간, 토큰 사용량과 비용(usage, total_cost_usd, modelUsage), 권한 거부 목록 같은 실행 메타데이터가 JSON으로 반환됩니다.
요약이나 이슈 목록 같은 도메인 필드는 최상위에 없고, 응답 본문은 result 문자열 하나에 들어갑니다.
jq 같은 도구로 필드를 추출해 후속 처리에 활용할 수 있습니다.
필드 단위 구조가 필요하면 --json-schema로 출력 계약을 고정해 structured_output 키를 읽거나, 프롬프트에서 JSON 출력을 요구한 뒤 result를 fromjson으로 한 번 더 파싱합니다.
그렇게 얻은 issues로 GitHub Issue를 자동 생성하거나, total_cost_usd로 비용 알람을 설정하는 식으로 활용할 수 있습니다.
