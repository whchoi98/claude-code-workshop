# Slide 47: Stop example

**Part 3: HOOKS 4가지 시점**

## Code Blocks

### stop notify

```bash
#!/bin/bash
# /opt/claude/hooks/stop-notify.sh

INPUT=$(cat)
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id')

# 환경변수에서 Slack webhook URL 가져옴
if [ -z "$SLACK_WEBHOOK_URL" ]; then
  exit 0
fi

# 세션 소요 시간 계산 (예시: 5분 이상이면 알림)
SESSION_FILE="/tmp/claude-session-$SESSION_ID"
if [ ! -f "$SESSION_FILE" ]; then
  date +%s > "$SESSION_FILE"
  exit 0
fi

START=$(cat "$SESSION_FILE")
NOW=$(date +%s)
DURATION=$((NOW - START))

if [ "$DURATION" -lt 300 ]; then
  # 5분 미만은 알림 안 함
  exit 0
fi

# Slack 알림 발송
MIN=$((DURATION / 60))
USER=$(whoami)
PROJECT=$(basename "$(pwd)")

curl -s -X POST "$SLACK_WEBHOOK_URL" \
  -H 'Content-Type: application/json' \
  -d "{\"text\":\"🎉 Claude task completed in $PROJECT (${MIN}min) by $USER\"}" \
  >/dev/null

exit 0
```

## Speaker Notes

Stop 실전 예시는 Slack 작업 완료 알림입니다.
SLACK_WEBHOOK_URL 환경변수가 없으면 즉시 종료합니다.
세션 소요 시간을 계산합니다.
/tmp 디렉토리에 세션별 시작 시간 파일을 저장합니다.
첫 호출 시 시작 시간을 기록하고 종료합니다.
이후 호출에서 현재 시간과 비교해 duration을 계산합니다.
5분 미만은 알림 없이 종료합니다.
짧은 작업까지 매번 알림이 가면 노이즈가 됩니다.
5분 이상 걸린 작업만 알림을 보냅니다.
curl로 Slack webhook URL에 POST 요청을 보냅니다.
메시지에는 프로젝트명, 소요 시간, 사용자명이 포함됩니다.
사용자가 다른 작업을 하다가 Claude 작업이 끝났음을 알 수 있어 productivity가 향상됩니다.
비동기 발송이며 실패해도 도구 진행에 영향이 없습니다.
