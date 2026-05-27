# Slide 87: MCP 도구 권한 통제

**Part 5: MCP SDK 통합**

## Code Blocks

### permissions

```python
# MCP 서버에 모든 도구가 있지만 일부만 허용하고 싶음

# 1. allowed_tools로 제한
response = client.beta.messages.create(
    mcp_servers=[{
        "type": "url",
        "url": "https://mcp.github.com/mcp",
        "name": "github",
        "authorization_token": GH_TOKEN,
    }],
    # Claude가 호출할 수 있는 도구 명시 제한
    tools=[
        {"name": "github__list_issues"},
        {"name": "github__get_issue"},
        # github__create_issue은 차단됨
    ],
    messages=[...],
    betas=["mcp-client-2025-04-04"],
)

# 2. tool_choice로 강제
client.beta.messages.create(
    mcp_servers=[...],
    tool_choice={"type": "tool", "name": "github__search_code"},
    messages=[...],
    betas=["mcp-client-2025-04-04"],
)

# 3. 환경별 권한 매트릭스
TOOL_PERMISSIONS = {
    "dev": ["github__list_*", "github__get_*"],   # 읽기만
    "prod": ["github__*"],                          # 모두
}

def get_allowed_tools(env, server):
    patterns = TOOL_PERMISSIONS.get(env, [])
    # 와일드카드 매칭으로 도구 선택
    all_tools = fetch_mcp_tools(server)
    allowed = []
    for tool in all_tools:
        for pattern in patterns:
            if fnmatch.fnmatch(tool, pattern):
                allowed.append({"name": tool})
                break
    return allowed

# 4. 사용자별 권한
def get_user_mcp_config(user):
    base = {
        "type": "url",
        "url": "https://mcp.company.com",
        "name": "company",
        "authorization_token": user.mcp_token,
    }
    if user.role == "admin":
        return [base]
    else:
        # 일반 사용자는 읽기 전용
        base["url"] = "https://mcp-readonly.company.com"
        return [base]

# 5. 위험한 도구 사용자 확인
DANGEROUS_TOOLS = {
    "github__delete_repo",
    "slack__delete_channel",
    "db__drop_table",
}

# 미리 차단
allowed = [t for t in all_tools if t not in DANGEROUS_TOOLS]
client.beta.messages.create(
    tools=[{"name": t} for t in allowed],
    ...
)
```

## Speaker Notes

MCP 도구 권한 통제로 안전한 통합을 만듭니다.
MCP 서버에 많은 도구가 있어도 일부만 허용하고 싶은 경우가 많습니다.
1번 allowed_tools로 제한합니다.
tools 매개변수에 허용할 도구만 명시합니다.
name은 server__tool 형식으로 prefix가 붙습니다.
명시하지 않은 도구는 Claude가 호출할 수 없습니다.
2번 tool_choice로 강제 호출도 가능합니다.
특정 도구만 사용하게 강제합니다.
3번 환경별 권한 매트릭스를 관리합니다.
TOOL_PERMISSIONS dict에 환경별 허용 패턴을 정의합니다.
dev는 list와 get 같은 읽기만 허용하고 prod는 모두 허용합니다.
fnmatch로 와일드카드 패턴 매칭을 합니다.
4번 사용자별 권한도 적용 가능합니다.
admin은 일반 MCP 서버, 일반 사용자는 read-only MCP 서버를 사용합니다.
서버 URL을 분리해 권한을 강제하는 패턴입니다.
5번 위험한 도구는 사용자 확인이 필요합니다.
delete나 drop 같은 파괴적 도구는 DANGEROUS_TOOLS set에 등록해 미리 차단합니다.
tools 명시에서 제외하면 Claude가 호출할 수 없습니다.
안전 우선 원칙을 SDK 레벨에서 적용할 수 있습니다.
