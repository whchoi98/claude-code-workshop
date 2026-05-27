# Slide 12: mcpServers options

**Part 1: settings.json 구조**

## Code Blocks

### mcpServers

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path"],
      "env": {}
    },

    "github": {
      "type": "http",
      "url": "https://mcp-github.example.com",
      "headers": {
        "Authorization": "Bearer ${GITHUB_TOKEN}"
      }
    },

    "internal-jira": {
      "type": "sse",
      "url": "https://mcp-jira.company.com/sse",
      "headers": {
        "X-Auth": "${JIRA_TOKEN}"
      }
    },

    "custom-stdio": {
      "command": "/opt/my-mcp/server",
      "args": ["--config", "/etc/mcp.json"],
      "env": {
        "LOG_LEVEL": "info"
      }
    }
  }
}
```

## Speaker Notes

mcpServers 옵션의 3가지 통신 방식을 살펴봅니다.
첫 번째는 stdio 방식입니다.
command와 args로 로컬 프로세스를 실행합니다.
Claude Code가 자식 프로세스로 MCP 서버를 띄우고 표준 입출력으로 통신합니다.
npx로 공식 서버를 즉시 사용할 수 있는 편리한 방식입니다.
두 번째는 http 방식입니다.
type을 http로 명시하고 url과 headers를 지정합니다.
원격 HTTP 서버와 통신하며 인증은 Bearer 토큰을 헤더에 넣습니다.
세 번째는 sse 방식입니다.
Server-Sent Events로 양방향에 가까운 통신이 가능합니다.
사내 사용자 정의 MCP 서버에 자주 사용됩니다.
환경변수는 dollar-sign 중괄호 형태로 참조해 런타임에 안전하게 주입됩니다.
