# Slide 73: Pattern 1 / 핵심 스크립트

**Part 5: 자동화 패턴**

## Code Blocks

### pr-review-bot.sh

```bash
#!/bin/bash
# pr-review-bot.sh
set -euo pipefail

PR_NUM="${1:?Usage: pr-review-bot.sh <PR-number>}"

# 1. PR 정보 수집
PR_DATA=$(gh pr view "$PR_NUM" \
  --json title,body,additions,deletions,changedFiles,author)
TITLE=$(echo "$PR_DATA" | jq -r '.title')
ADDITIONS=$(echo "$PR_DATA" | jq -r '.additions')
DELETIONS=$(echo "$PR_DATA" | jq -r '.deletions')

# 2. 큰 PR 차단 (비용 통제)
TOTAL_CHANGES=$((ADDITIONS + DELETIONS))
if [ "$TOTAL_CHANGES" -gt 2000 ]; then
  gh pr comment "$PR_NUM" --body \
    "⚠️ PR이 너무 큽니다 ($TOTAL_CHANGES 줄). 분할 요청."
  exit 0
fi

# 3. AI 분석 (구조화 JSON 응답)
REVIEW=$(claude -p "$(cat <<EOF
다음 PR을 4가지 관점에서 분석. 출력은 JSON.

PR: $TITLE
Diff:
$(gh pr diff "$PR_NUM")

{
  "verdict": "approve|comment|request_changes",
  "labels": ["bugfix"|"feature"|"refactor"|"docs"|"test"],
  "severity": "low|medium|high",
  "comments": [
    {"file": "...", "line": 0, "severity": "...", "msg": "..."}
  ],
  "summary": "한 줄 요약"
}
EOF
)" \
  --allowed-tools "Read,Grep,Glob,Bash(gh pr:*)" \
  --max-turns 15 \
  --output-format json | jq -r '.result' | jq .)

echo "$REVIEW" > "/tmp/pr-$PR_NUM-review.json"
```

## Speaker Notes

Pattern 1의 핵심 스크립트 첫 부분입니다.
첫째, PR 정보 수집입니다.
gh pr view로 title, body, additions, deletions, changedFiles, author를 JSON으로 가져옵니다.
jq로 필요한 값들을 추출합니다.
둘째, 큰 PR 차단으로 비용을 통제합니다.
변경 라인이 2000줄을 초과하면 분할 요청 코멘트를 달고 종료합니다.
셋째, AI 분석으로 구조화 JSON 응답을 받습니다.
프롬프트에 정확한 JSON 스키마를 명시합니다.
verdict는 approve, comment, request_changes 중 하나입니다.
labels에 적절한 분류 라벨을 배열로 받습니다.
severity로 전체 심각도를 결정합니다.
comments 배열에 파일과 라인 단위 상세 코멘트를 담습니다.
summary로 한 줄 요약을 받습니다.
결과는 임시 파일에 저장해 다음 단계에서 활용합니다.
