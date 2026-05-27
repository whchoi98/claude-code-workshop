# Slide 75: Official server: slack

**Part 5: MCP 기본과 공식 서버**

## Code Blocks

### slack

```bash
# 1. Slack App 생성 및 Bot Token 발급
# https://api.slack.com/apps → Create New App
# OAuth Scopes 추가:
#   - chat:write       (메시지 작성)
#   - channels:read    (채널 목록)
#   - users:read       (사용자 목록)
#   - search:read      (검색)

# 2. settings.json 등록
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}",
        "SLACK_TEAM_ID": "T0123456"
      }
    }
  }
}

# 3. 제공되는 도구
- send_message(channel, text)
- list_channels()
- list_users(channel)
- search_messages(query)
- get_thread_replies(channel, thread_ts)
- add_reaction(channel, ts, name)

# 4. 사용 예시
> #engineering 채널에 오늘 PR 머지 결과 요약 메시지 보내줘
> 이번 주 'urgent' 라벨된 메시지 찾아줘
> 회의 결과를 #team-decisions에 정리해서 게시해줘
```

## Speaker Notes

세 번째 공식 서버는 slack입니다.
Slack 통합 서버입니다.
사용 절차는 다음과 같습니다.
1단계 Slack App을 생성하고 Bot Token을 발급합니다.
api.slack.com에서 Create New App을 선택합니다.
OAuth Scopes에 chat:write, channels:read, users:read, search:read를 추가합니다.
2단계 settings.json에 등록합니다.
npx로 server-slack 패키지를 실행하고 env에 SLACK_BOT_TOKEN과 SLACK_TEAM_ID를 주입합니다.
3단계 제공되는 도구를 봅니다.
send_message로 메시지 전송, list_channels와 list_users로 목록 조회, search_messages로 검색이 가능합니다.
get_thread_replies로 스레드 전체를 가져올 수 있고 add_reaction으로 이모지 반응을 추가할 수 있습니다.
4단계 사용 예시는 풍부합니다.
채널에 자동 요약 메시지 보내기, urgent 라벨 메시지 찾기, 회의 결과를 정리해서 게시하기 같은 작업이 가능합니다.
Slack을 워크플로의 핵심 허브로 활용할 수 있습니다.
