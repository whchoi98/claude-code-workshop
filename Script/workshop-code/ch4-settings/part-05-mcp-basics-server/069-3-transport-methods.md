# Slide 69: 3 transport methods

**Part 5: MCP 기본과 공식 서버**

## Code Blocks

### 3 transports

```bash
# settings.json - 3가지 방식 예시
{
  "mcpServers": {
    "local-filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path"]
    },
    "remote-jira": {
      "type": "http",
      "url": "https://mcp-jira.company.com",
      "headers": { "Authorization": "Bearer ${JIRA_TOKEN}" }
    },
    "stream-events": {
      "type": "sse",
      "url": "https://mcp-events.company.com/sse"
    }
  }
}
```

## Speaker Notes

MCP의 3가지 통신 방식을 비교합니다.
stdio 방식은 로컬 프로세스 통신입니다.
Claude Code가 MCP 서버를 자식 프로세스로 실행하고 표준 입출력으로 메시지를 주고받습니다.
로컬 도구나 빠른 응답이 필요한 시나리오에 적합합니다.
http 방식은 HTTP API 호출입니다.
원격 서버와 통신하며 Bearer 토큰 같은 인증을 헤더로 전달합니다.
사내 마이크로서비스나 인증이 필요한 경우에 적합합니다.
sse 방식은 Server-Sent Events 양방향 스트리밍입니다.
장기 실행 작업이나 실시간 알림이 필요한 시나리오에 적합합니다.
settings.json 예시를 봅니다.
local-filesystem은 stdio로 npx 명령을 실행합니다.
remote-jira는 http 타입과 url, headers를 명시합니다.
stream-events는 sse 타입과 url만 명시합니다.
한 settings 안에 3가지 방식을 혼합 사용할 수 있습니다.
