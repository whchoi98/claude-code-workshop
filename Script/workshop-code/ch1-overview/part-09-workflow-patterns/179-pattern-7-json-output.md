# Slide 179: Pattern 7 JSON Output

**Part 9: WORKFLOW PATTERNS**

## Code Blocks

### JSON OUTPUT

```bash
# JSON 출력 옵션
$ claude -p "현재 디렉토리 분석" --output-format json

{
  "model": "claude-sonnet-4-5",
  "tokens": { "input": 1240, "output": 670, "cost_usd": 0.012 },
  "summary": "...",
  "tools_used": [
    { "tool": "Read", "count": 5 },
    { "tool": "Grep", "count": 2 }
  ],
  "files_modified": [],
  "files_read": [
    "package.json", "src/index.ts", "README.md"
  ],
  "structured_output": {
    "stack": ["typescript", "express"],
    "issues": [
      { "severity": "high", "file": "src/auth.ts:42", ... }
    ]
  }
}

# jq로 추출
$ claude -p "..." --output-format json | jq '.structured_output.issues'
```

## Speaker Notes

JSON 출력 형식은 자동화 파이프라인에서 매우 유용합니다.
--output-format json 플래그를 주면 사용된 모델, 토큰 사용량과 비용, 요약, 사용된 도구와 횟수, 수정한 파일 목록, 읽은 파일 목록, 그리고 구조화된 출력까지 모두 JSON으로 반환됩니다.
jq 같은 도구로 필드를 추출해 후속 처리에 활용할 수 있습니다.
issues 필드만 뽑아서 GitHub Issue로 자동 생성하거나, tokens 정보로 비용 알람을 설정하거나, files_modified로 PR 자동 생성에 활용할 수 있습니다.
