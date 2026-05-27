# Slide 68: MCP primitives

**Part 5: MCP 기본과 공식 서버**

## Code Blocks

### primitives

```bash
# 예시: GitHub MCP 서버가 제공하는 것

# Tools (액션)
- create_issue(title, body, labels)
- merge_pr(pr_number, method)
- search_code(query, repo)

# Resources (데이터)
- github://repos/owner/repo/issues
- github://repos/owner/repo/pulls

# Prompts (템플릿)
- "review-pr"  → "다음 PR을 리뷰: {pr_number}"
- "summarize-issues" → "최근 issue 요약"
```

## Speaker Notes

MCP의 3가지 primitive를 정확히 이해해야 합니다.
Tools는 AI가 호출하는 함수입니다.
액션을 수행하는 용도로 create_issue, send_message 같은 함수들입니다.
Resources는 AI가 읽는 데이터입니다.
정적 또는 동적 콘텐츠로 file 경로나 db 스키마 같은 URI 형태로 식별됩니다.
Prompts는 재사용 가능한 프롬프트 템플릿입니다.
review-pr이나 summarize-meeting 같은 이름의 템플릿입니다.
GitHub MCP 서버를 예시로 봅니다.
Tools에는 create_issue, merge_pr, search_code 같은 액션이 있습니다.
Resources에는 github 스킴의 repository와 issues URI가 있습니다.
Prompts에는 review-pr과 summarize-issues 템플릿이 있습니다.
MCP 서버를 작성할 때 어떤 primitive를 제공할지가 핵심 설계 결정입니다.
Claude Code는 이 3가지를 모두 활용해 사용자 요청을 처리합니다.
