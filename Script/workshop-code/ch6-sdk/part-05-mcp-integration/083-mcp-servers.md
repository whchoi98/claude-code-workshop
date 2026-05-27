# Slide 83: mcp_servers 매개변수

**Part 5: MCP SDK 통합**

## Code Blocks

### mcp_servers

```typescript
# 1. URL 기반 MCP 서버 연결
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    mcp_servers=[
        {
            "type": "url",
            "url": "https://mcp.github.com/mcp",
            "name": "github",
            "authorization_token": os.getenv("GITHUB_TOKEN"),
        }
    ],
    messages=[{
        "role": "user",
        "content": "anthropics/claude-code 저장소의 최근 이슈 5개",
    }],
    betas=["mcp-client-2025-04-04"],
)

# 2. 여러 MCP 서버 동시 연결
response = client.beta.messages.create(
    mcp_servers=[
        {"type": "url", "url": "https://mcp.github.com/mcp",
         "name": "github", "authorization_token": GH_TOKEN},
        {"type": "url", "url": "https://mcp.slack.com/mcp",
         "name": "slack", "authorization_token": SLACK_TOKEN},
        {"type": "url", "url": "https://mcp.linear.app/mcp",
         "name": "linear", "authorization_token": LINEAR_TOKEN},
    ],
    messages=[{
        "role": "user",
        "content": "최근 PR을 분석하고 Slack 팀에 요약 게시",
    }],
    betas=["mcp-client-2025-04-04"],
)

# 3. 응답에서 MCP 도구 사용 추적
for block in response.content:
    if block.type == "mcp_tool_use":
        print(f"MCP tool: {block.server_name}.{block.name}")
        print(f"  Input: {block.input}")
    elif block.type == "mcp_tool_result":
        print(f"  Result: {block.content[:100]}")
    elif block.type == "text":
        print(f"Text: {block.text}")

# 4. TypeScript도 동일
const response = await client.beta.messages.create({
  model: "claude-sonnet-4-5",
  max_tokens: 1024,
  mcp_servers: [
    {
      type: "url",
      url: "https://mcp.github.com/mcp",
      name: "github",
      authorization_token: process.env.GITHUB_TOKEN,
    },
  ],
  messages: [{ role: "user", content: "..." }],
  betas: ["mcp-client-2025-04-04"],
});
```

## Speaker Notes

mcp_servers 매개변수 사용법입니다.
1번 URL 기반 MCP 서버 연결입니다.
client.beta.messages.create에 mcp_servers 배열을 명시합니다.
각 서버는 type url, url, name, authorization_token을 가집니다.
name은 서버를 식별하는 별명이고 authorization_token은 인증 정보입니다.
betas 매개변수에 mcp-client-2025-04-04를 명시해 beta 기능을 활성화합니다.
2번 여러 MCP 서버 동시 연결도 가능합니다.
github, slack, linear를 한 번에 연결하면 Claude가 모든 도구를 인식합니다.
복합 작업 예를 들어 PR 분석 후 Slack에 게시 같은 작업이 자연스럽게 처리됩니다.
3번 응답에서 MCP 도구 사용을 추적합니다.
block.type이 mcp_tool_use면 어떤 서버의 어떤 도구가 호출됐는지 추적할 수 있습니다.
server_name과 name이 핵심 정보입니다.
mcp_tool_result는 호출 결과입니다.
4번 TypeScript도 동일한 패턴입니다.
beta.messages.create에 mcp_servers와 betas를 명시합니다.
betas는 헤더로 전송되어 beta 기능을 활성화합니다.
