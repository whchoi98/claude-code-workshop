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

# JSON 구조
{
  "summary": "신규 결제 흐름 추가...",
  "issues": [
    { "severity": "high",   "file": "payment.js", "line": 88,
      "message": "...", "suggestion": "..." },
    { "severity": "medium", "file": "payment.js", "line": 124, ... }
  ],
  "tokens_used": 8234,
  "cost_usd": 0.041
}

# jq로 후처리
$ jq '.issues | map(select(.severity == "high"))' review-result.json

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
summary 필드에 한 단락 요약이 들어갑니다.
issues 배열에는 각 이슈가 severity, file, line, message, suggestion 필드로 구조화됩니다.
tokens_used와 cost_usd 같은 메타데이터도 포함됩니다.
jq 같은 도구로 필요한 필드만 추출해 후처리할 수 있습니다.
예시처럼 severity가 high인 항목만 필터링할 수도 있습니다.
Git pre-commit hook에 등록하면 커밋 직전에 자동 리뷰가 실행되는 워크플로도 가능합니다.
