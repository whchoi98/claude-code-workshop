# Slide 87: Pattern 5 / 보고서 스크립트

**Part 5: 자동화 패턴**

## Code Blocks

### daily-report.sh

```bash
#!/bin/bash
# daily-report.sh
set -euo pipefail

DATE=$(date -d "yesterday" +%Y-%m-%d)
WORKDIR="/tmp/daily-$DATE"
mkdir -p "$WORKDIR"

# 1. 데이터 수집
gh pr list --state merged \
  --search "merged:$DATE" \
  --json title,author,labels,additions,deletions \
  > "$WORKDIR/prs.json"

gh issue list --state closed \
  --search "closed:$DATE" \
  --json title,labels,author > "$WORKDIR/closed-issues.json"

gh issue list --state open \
  --search "created:$DATE" \
  --json title,labels,author > "$WORKDIR/new-issues.json"

# 2. AI 요약 (구조화)
REPORT=$(claude -p "$(cat <<EOF
어제($DATE) 팀 활동을 stand-up 보고서로 요약:

머지된 PR:
$(cat $WORKDIR/prs.json | jq -c '.')

클로즈된 이슈:
$(cat $WORKDIR/closed-issues.json | jq -c '.')

새 이슈:
$(cat $WORKDIR/new-issues.json | jq -c '.')

응답: 다음 구조의 Markdown
# 📅 Daily Report - $DATE

## 🎯 Highlights (3-5개)
- ...

## ✅ 완료된 작업
- 카테고리별 정리

## 🆕 새로운 이슈
- 우선순위별 정리

## 👥 Active Contributors
- top 5

## ⚠️ 주목할 사항
- 긴급한 것, 차단된 것
EOF
)" \
  --model claude-sonnet-4-5 \
  --max-turns 5 \
  --output-format json | jq -r '.result')

echo "$REPORT" > "$WORKDIR/report.md"

# 3. Slack 게시 (Block Kit)
PAYLOAD=$(jq -n --rawfile r "$WORKDIR/report.md" '{
  blocks: [
    { type: "section",
      text: { type: "mrkdwn", text: $r } }
  ]
}')

curl -X POST "$SLACK_WEBHOOK" \
  -H 'Content-Type: application/json' \
  -d "$PAYLOAD"

echo "✓ 매일 보고서 게시 완료"
```

## Speaker Notes

Pattern 5 보고서 스크립트 daily-report.sh입니다.
DATE 변수로 어제 날짜를 가져옵니다.
1단계 데이터 수집입니다.
gh pr list로 어제 머지된 PR, gh issue list로 어제 클로즈된 이슈와 새로 열린 이슈를 JSON으로 수집합니다.
각각 별도 파일에 저장합니다.
2단계 AI 요약입니다.
3가지 데이터를 모두 프롬프트에 포함시킵니다.
응답 구조를 명확히 명시합니다.
Highlights 3-5개, 완료된 작업, 새로운 이슈, Active Contributors top 5, 주목할 사항 5 섹션으로 구성합니다.
이모지와 카테고리를 활용해 가독성을 높입니다.
claude-sonnet-4-5로 균형 잡힌 분석을 받습니다.
결과를 report.md에 저장합니다.
3단계 Slack 게시입니다.
Block Kit 형식의 PAYLOAD를 jq로 만듭니다.
rawfile 옵션으로 마크다운 파일을 안전하게 JSON에 포함시킵니다.
특수 문자 이스케이프를 자동으로 처리합니다.
curl로 webhook에 POST 합니다.
팀 채널에 깔끔한 형식으로 자동 게시됩니다.
