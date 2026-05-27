# Slide 46: Internal MCP server

**Part 3: NETWORK & SECURITY**

## Code Blocks

### Internal MCP

```bash
# 시나리오: 사내 JIRA, Confluence, 사내 GitLab을 Claude Code가 사용

# .claude/settings.json (팀 공유)
{
  "mcpServers": {
    "jira-internal": {
      "command": "node",
      "args": ["/opt/mcp/jira-server.js"],
      "env": {
        "JIRA_URL": "https://jira.company.com",
        "JIRA_TOKEN": "${JIRA_TOKEN}"
      }
    },
    "confluence-internal": {
      "type": "http",
      "url": "https://mcp-confluence.company.com",
      "auth": {
        "type": "oauth",
        "client_id": "claude-code"
      }
    },
    "gitlab-internal": {
      "type": "sse",
      "url": "https://mcp-gitlab.company.com/sse",
      "headers": {
        "X-Internal-Auth": "${GITLAB_TOKEN}"
      }
    }
  }
}

# 사용 예
> 이번 스프린트의 JIRA 티켓 5개를 GitLab MR로 이동해 줘
```

## Speaker Notes

사내 MCP 서버 통합 방법입니다.
사내 JIRA, Confluence, GitLab을 Claude Code가 직접 사용할 수 있게 합니다.
settings.json의 mcpServers에 사내 도구를 등록합니다.
jira-internal은 로컬 stdio 방식입니다.
node로 jira-server.js를 실행하며 JIRA URL과 토큰을 환경변수로 주입합니다.
confluence-internal은 HTTP 방식입니다.
사내 MCP 서버 URL을 지정하고 OAuth로 인증합니다.
gitlab-internal은 Server-Sent Events 방식입니다.
sse URL과 헤더에 내부 인증 토큰을 포함합니다.
환경변수는 dollar-sign 중괄호 형태로 참조해 실제 값은 런타임에 주입됩니다.
사용 예시처럼 자연어로 JIRA 티켓을 GitLab MR로 이동해 달라고 요청하면 Claude Code가 두 시스템을 자동으로 호출합니다.
사내 시스템을 AI 워크플로에 통합하는 강력한 패턴입니다.
