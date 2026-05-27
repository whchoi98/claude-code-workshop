# Slide 60: Pattern 4 / Slack - script

**Part 4: HOOKS 실전 패턴**

## Code Blocks

### slack-notify.sh

```bash
#!/bin/bash
# /opt/claude/hooks/slack-notify.sh

[ -z "$SLACK_WEBHOOK_URL" ] && exit 0

INPUT=$(cat)
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id')
SESSION_FILE="/tmp/claude-session-$SESSION_ID"

# 첫 호출이면 시작 시간만 기록
if [ ! -f "$SESSION_FILE" ]; then
  date +%s > "$SESSION_FILE"
  exit 0
fi

START=$(cat "$SESSION_FILE")
NOW=$(date +%s)
DURATION=$((NOW - START))

# 5분 미만은 알림 안 함
[ "$DURATION" -lt 300 ] && exit 0

# 정보 수집
MIN=$((DURATION / 60))
USER=$(whoami)
PROJECT=$(basename "$(pwd)")
BRANCH=$(git branch --show-current 2>/dev/null || echo "no-git")

# Slack Block Kit 형식
PAYLOAD=$(cat <<EOF
{
  "blocks": [
    {
      "type": "section",
      "text": { "type": "mrkdwn",
                "text": "*🎉 Claude task completed*" }
    },
    {
      "type": "section",
      "fields": [
        { "type": "mrkdwn", "text": "*Project:*\n$PROJECT" },
        { "type": "mrkdwn", "text": "*Branch:*\n$BRANCH" },
        { "type": "mrkdwn", "text": "*User:*\n$USER" },
        { "type": "mrkdwn", "text": "*Duration:*\n${MIN} min" }
      ]
    }
  ]
}
EOF
)

curl -s -X POST "$SLACK_WEBHOOK_URL" \
  -H 'Content-Type: application/json' \
  -d "$PAYLOAD" >/dev/null 2>&1 &

# 다음 알림을 위해 시간 갱신
date +%s > "$SESSION_FILE"
exit 0
```

## Speaker Notes

Pattern 4 slack-notify.sh 완성 스크립트입니다.
SLACK_WEBHOOK_URL이 없으면 즉시 종료합니다.
stdin INPUT에서 session_id를 추출합니다.
/tmp 디렉토리에 세션별 시작 시간 파일을 관리합니다.
첫 호출이면 시작 시간을 기록하고 종료합니다.
이후 호출에서 현재 시간과 차이로 duration을 계산합니다.
5분 미만은 알림 없이 종료합니다.
알림을 보낼 때는 풍부한 정보를 수집합니다.
USER, PROJECT, BRANCH 정보를 포함시킵니다.
Slack Block Kit 형식으로 PAYLOAD를 만듭니다.
section 블록에 fields 배열로 4가지 정보를 표시합니다.
Project, Branch, User, Duration이 깔끔하게 정렬되어 표시됩니다.
curl로 비동기 전송합니다.
마지막에 시간 파일을 갱신해 다음 알림 임계치를 새로 시작합니다.
이렇게 하면 한 세션에서 여러 번 5분 임계치를 트리거할 수 있습니다.
