# Slide 122: 4-mechanism integration

**Part 8: INTEGRATION & TROUBLESHOOTING**

## Code Blocks

### integration

```bash
# 시나리오: PR 자동 종합 처리

# 1. Custom Command (.claude/commands/handle-pr.md)
---
description: PR을 종합 처리 (리뷰 + 머지 + 알림 + JIRA)
allowed-tools:
  - Bash(gh pr:*)
  - mcp__jira__transition_issue
  - mcp__slack__send_message
---

PR #$ARGUMENTS 를 종합 처리합니다:
1. /review-pr 수행 (위 명령 활용)
2. 승인 시 PR 머지
3. JIRA 티켓 Done 처리 (MCP github + jira)
4. Slack 알림 (MCP slack)

# 2. Permissions (managed-settings.json)
{
  "permissions": {
    "deny": ["Bash(rm -rf:*)", "Read(**/.env*)"],
    "allow": ["Bash(gh pr:*)", "Bash(git diff:*)"]
  }
}

# 3. Hooks (조직 표준 적용)
{
  "hooks": {
    "PreToolUse": [{ "matcher": ".*", "hooks": [
      { "command": "/opt/claude/dlp.sh" },
      { "command": "/opt/claude/audit.sh pre" }
    ]}],
    "PostToolUse": [{ "matcher": "Write|Edit", "hooks": [
      { "command": "/opt/claude/auto-format.sh" }
    ]}]
  }
}

# 4. MCP (사내 + 공식)
{
  "mcpServers": {
    "github": { "command": "npx", "args": ["@modelcontextprotocol/server-github"] },
    "jira":   { "command": "npx", "args": ["@modelcontextprotocol/server-jira"] },
    "slack":  { "command": "npx", "args": ["@modelcontextprotocol/server-slack"] }
  }
}
```

## Speaker Notes

4 메커니즘을 통합한 완성된 PR 워크플로 예시입니다.
시나리오는 PR 종합 처리입니다.
Custom Command가 진입점입니다.
handle-pr.md에 한 명령으로 4단계 작업을 정의합니다.
allowed-tools에 gh pr 명령과 mcp jira transition, mcp slack send_message를 명시합니다.
Permissions가 안전망 역할입니다.
managed-settings에서 위험 명령은 deny, 안전한 명령은 allow로 통제합니다.
Hooks가 자동화 메커니즘입니다.
PreToolUse에 DLP와 감사 로그를 등록하고 PostToolUse에 auto-format을 등록합니다.
MCP가 외부 통합을 담당합니다.
github, jira, slack 세 서버를 등록해 외부 시스템과 자동 연동합니다.
사용자는 /handle-pr 1234 한 명령으로 PR 리뷰, 머지, JIRA 상태 변경, Slack 알림이 자동으로 완료됩니다.
4 메커니즘의 시너지가 명확히 드러나는 예시입니다.
