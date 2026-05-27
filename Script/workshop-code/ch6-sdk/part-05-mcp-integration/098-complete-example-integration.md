# Slide 98: 완성 예시 / 통합 비서

**Part 5: MCP SDK 통합**

## Code Blocks

### integrated

```python
# integrated_assistant.py - 통합 비서
import anthropic
import os

client = anthropic.Anthropic()

# 환경별 MCP 설정
def get_mcp_servers():
    return [
        # GitHub
        {"type": "url", "url": "https://mcp.github.com/mcp",
         "name": "github", "authorization_token": os.getenv("GH_TOKEN")},
        # Slack
        {"type": "url", "url": "https://mcp.slack.com/mcp",
         "name": "slack", "authorization_token": os.getenv("SLACK_TOKEN")},
        # Linear (issue tracking)
        {"type": "url", "url": "https://mcp.linear.app/mcp",
         "name": "linear", "authorization_token": os.getenv("LINEAR_TOKEN")},
        # 사내 DB (read-only)
        {"type": "url", "url": "https://mcp.company.com/db",
         "name": "db", "authorization_token": os.getenv("DB_TOKEN")},
    ]

# 권한별 허용 도구
TOOLS_BY_ROLE = {
    "admin": [
        {"name": "github__*"},
        {"name": "slack__*"},
        {"name": "linear__*"},
        {"name": "db__query"},
    ],
    "developer": [
        {"name": "github__list_*"}, {"name": "github__get_*"},
        {"name": "slack__send_message"},
        {"name": "linear__create_issue"}, {"name": "linear__list_issues"},
        {"name": "db__query"},
    ],
    "viewer": [
        {"name": "github__list_*"}, {"name": "github__get_*"},
        {"name": "slack__list_channels"},
        {"name": "db__query"},
    ],
}

def assistant_query(user_id: str, role: str, question: str):
    response = client.beta.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=4000,
        mcp_servers=get_mcp_servers(),
        tools=TOOLS_BY_ROLE[role],
        metadata={"user_id": user_id},
        system=[{
            "type": "text",
            "text": """당신은 통합 업무 비서입니다.

            사용 가능한 시스템:
            - GitHub: 코드 저장소, PR, 이슈
            - Slack: 팀 커뮤니케이션
            - Linear: 작업 추적
            - DB: 비즈니스 데이터 (읽기 전용)

            원칙:
            - 필요한 도구만 호출
            - 결과를 명확하게 요약
            - 위험한 작업은 사용자 확인 요청""",
            "cache_control": {"type": "ephemeral"},
        }],
        messages=[{"role": "user", "content": question}],
        betas=["mcp-client-2025-04-04"],
    )

    return {
        "answer": "".join(b.text for b in response.content if b.type == "text"),
        "tools_used": [
            f"{b.server_name}.{b.name}" for b in response.content
            if b.type == "mcp_tool_use"
        ],
        "usage": response.usage.model_dump(),
    }

# 사용
result = assistant_query("user_1", "developer",
    "지난주 머지된 PR 3개를 분석하고 Slack #engineering에 요약 게시")
```

## Speaker Notes

완성 예시 멀티 MCP 통합 비서입니다.
4개 MCP 서버를 연결합니다.
GitHub, Slack, Linear, 사내 DB 4가지입니다.
get_mcp_servers 함수에서 모든 서버를 정의하고 환경변수로 token을 주입합니다.
권한별 허용 도구를 TOOLS_BY_ROLE dict로 관리합니다.
admin은 모든 도구, developer는 일부 쓰기와 모든 읽기, viewer는 읽기만 허용합니다.
와일드카드 패턴으로 도구 그룹을 효율적으로 명시합니다.
assistant_query 함수에서 user_id, role, question을 받아 통합 호출을 수행합니다.
mcp_servers와 권한별 tools를 명시하고 metadata에 user_id를 포함시켜 추적합니다.
system prompt에 사용 가능한 시스템과 원칙을 명시합니다.
cache_control로 system prompt를 캐시합니다.
응답에서 텍스트, 사용된 도구 목록, usage를 추출해 반환합니다.
사용은 매우 강력합니다.
지난주 머지된 PR 3개 분석 후 Slack engineering 채널에 요약 게시 같은 복합 작업이 한 호출로 가능합니다.
Claude가 자동으로 GitHub에서 PR 정보를 수집하고 분석한 후 Slack에 게시합니다.
이런 통합 비서가 SDK에서 수십 줄 코드로 구현 가능합니다.
