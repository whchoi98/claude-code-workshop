# Slide 82: MCP 복습

**Part 5: MCP SDK 통합**

## Code Blocks

### comparison

```python
# 일반 Tool Use vs MCP 통합

# 방식 1: 직접 도구 정의 (Part 3에서 배움)
TOOLS = [
    {"name": "get_repo_issues", "description": "...", "input_schema": {...}},
]
def get_repo_issues(owner, repo): ...
client.messages.create(tools=TOOLS, ...)

# 방식 2: MCP 서버 활용 (이번 Part)
client.beta.messages.create(
    mcp_servers=[{
        "type": "url",
        "url": "https://example.com/mcp",
        "name": "github",
        "authorization_token": "ghp_...",
    }],
    messages=[{"role": "user", "content": "..."}],
)
# Claude가 github MCP 서버의 모든 도구를 자동 인식
```

## Speaker Notes

MCP 복습입니다.
MCP는 Model Context Protocol의 약자입니다.
AI가 외부 시스템과 통신하는 표준 프로토콜이고 JSON-RPC 기반입니다.
도구와 리소스를 표준화해 다양한 시스템을 일관된 방식으로 연결합니다.
왜 사용하는지 명확합니다.
도구를 매번 직접 구현하지 않고 기존 MCP 서버를 재사용합니다.
생태계를 활용해 빠르게 통합할 수 있습니다.
SDK에서는 mcp_servers 매개변수로 서버를 명시합니다.
Claude가 자동으로 도구로 인식해 호출합니다.
방식 1 직접 도구 정의는 Part 3에서 배운 방법입니다.
TOOLS 배열을 만들고 함수를 매핑해야 합니다.
방식 2 MCP 서버 활용은 이번 Part의 핵심입니다.
client.beta.messages.create에 mcp_servers를 명시하기만 하면 됩니다.
beta는 MCP가 beta 기능이기 때문이고 정식 릴리즈 시 client.messages.create에서 사용 가능합니다.
Claude가 github MCP 서버의 모든 도구를 자동 인식하고 필요할 때 호출합니다.
