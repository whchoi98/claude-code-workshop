# Slide 90: 실전 / Slack 통합

**Part 5: MCP SDK 통합**

## Code Blocks

### Slack MCP

```python
# slack_assistant.py - Slack과 결합된 비서
import anthropic

client = anthropic.Anthropic()

def smart_team_update(message_for_claude: str):
    response = client.beta.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2048,
        mcp_servers=[
            {
                "type": "url",
                "url": "https://mcp.slack.com/mcp",
                "name": "slack",
                "authorization_token": os.getenv("SLACK_TOKEN"),
            },
        ],
        # 채널 게시만 허용
        tools=[
            {"name": "slack__send_message"},
            {"name": "slack__list_channels"},
        ],
        system="""당신은 팀 커뮤니케이션 비서입니다.
        사용자의 요청을 적절한 Slack 채널에 자동 게시합니다.
        먼저 list_channels로 채널을 확인하고
        가장 적절한 채널에 send_message로 게시합니다.""",
        messages=[{
            "role": "user",
            "content": message_for_claude,
        }],
        betas=["mcp-client-2025-04-04"],
    )

    return response

# 사용 예시
smart_team_update("배포 완료 알림: v2.5.0이 prod에 배포됨")
# Claude가 자동으로:
# 1. slack__list_channels 호출
# 2. #deployments 또는 #general 같은 적절한 채널 찾음
# 3. slack__send_message로 메시지 게시

smart_team_update("내일 미팅 일정: 오전 10시 디자인 리뷰")
# Claude가 자동으로 #meetings 같은 채널 찾아 게시

# 다중 MCP 결합
def github_to_slack(pr_number: int):
    response = client.beta.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2048,
        mcp_servers=[
            {"type": "url", "url": "https://mcp.github.com/mcp",
             "name": "github", "authorization_token": GH_TOKEN},
            {"type": "url", "url": "https://mcp.slack.com/mcp",
             "name": "slack", "authorization_token": SLACK_TOKEN},
        ],
        system="""PR을 분석하고 결과를 Slack에 게시합니다.
        github__get_pull_request로 분석 후
        slack__send_message로 #engineering에 요약 게시.""",
        messages=[{
            "role": "user",
            "content": f"PR #{pr_number} 검토 후 팀에 공유",
        }],
        betas=["mcp-client-2025-04-04"],
    )
    return response

# Claude가 자동으로:
# 1. github__get_pull_request 호출 (PR 정보 수집)
# 2. github__get_pull_request_files 호출 (변경 파일)
# 3. 분석 수행
# 4. slack__send_message로 #engineering에 요약 게시
```

## Speaker Notes

실전 Slack MCP 통합 예시입니다.
smart_team_update 함수로 메시지를 적절한 채널에 자동 게시합니다.
slack MCP 서버 연결 후 send_message와 list_channels 두 도구만 허용합니다.
system prompt에서 list_channels로 채널을 먼저 확인하고 가장 적절한 채널에 send_message로 게시하라고 명시합니다.
사용은 매우 단순합니다.
배포 완료 알림 메시지를 주면 Claude가 자동으로 deployments나 general 채널을 찾아 게시합니다.
내일 미팅 일정 메시지는 meetings 채널을 찾아 게시합니다.
채널 매핑을 우리가 직접 코드로 작성하지 않아도 됩니다.
다중 MCP 결합 예시가 강력합니다.
github_to_slack 함수는 GitHub과 Slack 두 MCP 서버를 함께 사용합니다.
system prompt에서 PR 분석 후 Slack에 게시하는 흐름을 명시합니다.
Claude가 자동으로 GitHub 도구로 PR을 분석하고 Slack 도구로 결과를 게시합니다.
여러 시스템에 걸친 워크플로가 자연어 한 줄로 완성됩니다.
전통적인 코드라면 GitHub API 호출, 분석 로직, Slack API 호출의 여러 단계를 직접 작성해야 했습니다.
