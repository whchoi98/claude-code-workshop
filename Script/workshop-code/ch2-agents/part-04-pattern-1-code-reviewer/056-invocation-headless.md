# Slide 56: Invocation headless

**Part 4: PATTERN 1 / CODE REVIEWER**

## Code Blocks

### headless

```bash
# 헤드리스 모드로 단일 호출
$ git diff main..HEAD | claude -p \
    "code-reviewer 에이전트로 이 PR diff를 검토해 주세요" \
    --output-format json \
    > review-result.json

# JSON 구조: 최상위 키는 실행 메타데이터, 리뷰 본문은 result 문자열
{
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "result": "## Severity: high\n- payment.js:88 null 참조 ...\n\n## Severity: medium\n- ...",
  "session_id": "46dcf366-0059-45f0-adf1-44bb058ff5d6",
  "num_turns": 3,
  "total_cost_usd": 0.041,
  "usage": { "input_tokens": 6, "output_tokens": 944, "cache_read_input_tokens": 106228 }
}

# jq로 후처리: 리뷰 본문과 비용
$ jq -r '.result' review-result.json
$ jq '{cost: .total_cost_usd, turns: .num_turns}' review-result.json

# issues, severity 같은 필드로 다루려면 에이전트 프롬프트에 JSON 출력을 지정하고 한 번 더 파싱
$ jq -r '.result | fromjson | .issues | map(select(.severity == "high"))' review-result.json

# 또는 --json-schema로 출력 계약을 고정하면 structured_output 키에 담깁니다
$ git diff main..HEAD | claude -p "code-reviewer 에이전트로 이 PR diff를 검토해 주세요" \
    --output-format json --json-schema '{"type":"object","properties":{"issues":{"type":"array"}},"required":["issues"]}' \
    | jq '.structured_output.issues | map(select(.severity == "high"))'

# pre-commit hook으로 활용 가능
```

## Speaker Notes

두 번째 호출 방법은 헤드리스 모드입니다.
스크립트와 자동화에 친화적인 방식입니다.
git diff 결과를 stdin으로 claude 명령에 전달합니다.
-p 플래그로 프롬프트를 지정하고 code-reviewer 에이전트를 명시 호출합니다.
--output-format json으로 구조화 출력을 요청합니다.
결과를 파일로 저장합니다.
JSON 구조를 살펴봅니다.
최상위 키는 session_id, num_turns, total_cost_usd, usage 같은 실행 메타데이터이고, 에이전트가 쓴 리뷰 본문은 result 문자열 하나에 들어갑니다.
summary나 issues 같은 키는 최상위에 없습니다.
jq -r '.result'로 본문을, total_cost_usd로 비용을 추출해 후처리할 수 있습니다.
severity가 high인 항목만 필터링하려면 --json-schema로 출력 계약을 고정해 structured_output 키를 읽거나, 에이전트 프롬프트에 JSON 출력 형식을 지정한 뒤 result를 fromjson으로 한 번 더 파싱합니다.
Git pre-commit hook에 등록하면 커밋 직전에 자동 리뷰가 실행되는 워크플로도 가능합니다.
