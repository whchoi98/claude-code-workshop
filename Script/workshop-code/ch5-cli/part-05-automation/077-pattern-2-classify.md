# Slide 77: Pattern 2 / 분류 스크립트

**Part 5: 자동화 패턴**

## Code Blocks

### triage-issue.sh

```bash
#!/bin/bash
# triage-issue.sh
set -euo pipefail

ISSUE_NUM="${1:?Usage: triage-issue.sh <issue-number>}"

# 1. 이슈 정보 수집
ISSUE=$(gh issue view "$ISSUE_NUM" --json title,body,author,createdAt)

# 2. AI 분석 (구조화 JSON)
ANALYSIS=$(claude -p "$(cat <<EOF
다음 이슈를 분석하고 JSON으로 응답:

이슈 제목: $(echo "$ISSUE" | jq -r '.title')
내용:
$(echo "$ISSUE" | jq -r '.body')

응답 형식:
{
  "category": "bug|feature-request|documentation|question|security|performance|enhancement",
  "priority": "critical|high|medium|low",
  "estimated_effort": "trivial|small|medium|large",
  "suggested_assignees": ["github-username"],
  "needs_more_info": true|false,
  "duplicate_of": null,
  "summary": "한 문장 요약"
}

판단 기준:
- security: 보안 취약점, 데이터 노출
- critical: 프로덕션 중단, 데이터 손실
- high: 주요 기능 동작 불가
EOF
)" \
  --allowed-tools "Read,Grep,Glob,Bash(gh issue:*)" \
  --max-turns 10 \
  --output-format json | jq -r '.result' | jq .)

echo "$ANALYSIS" > "/tmp/issue-$ISSUE_NUM.json"

# 3. 결과 추출
CATEGORY=$(echo "$ANALYSIS" | jq -r '.category')
PRIORITY=$(echo "$ANALYSIS" | jq -r '.priority')
EFFORT=$(echo "$ANALYSIS" | jq -r '.estimated_effort')
NEEDS_INFO=$(echo "$ANALYSIS" | jq -r '.needs_more_info')
SUMMARY=$(echo "$ANALYSIS" | jq -r '.summary')

echo "[$CATEGORY] [$PRIORITY] [$EFFORT] $SUMMARY"
```

## Speaker Notes

Pattern 2 분류 스크립트 triage-issue.sh입니다.
첫째, 이슈 정보 수집입니다.
gh issue view로 title, body, author, createdAt을 JSON으로 가져옵니다.
둘째, AI 분석으로 구조화 JSON 응답을 받습니다.
프롬프트에 정확한 JSON 스키마를 명시합니다.
category는 7가지 표준 카테고리 중 하나로 분류합니다.
priority는 critical, high, medium, low 4단계입니다.
estimated_effort는 trivial, small, medium, large 4단계입니다.
suggested_assignees는 잠재 담당자 GitHub 사용자명 배열입니다.
needs_more_info는 정보 부족 여부 boolean입니다.
duplicate_of는 기존 이슈와 중복 시 그 번호입니다.
summary는 한 문장 요약입니다.
판단 기준도 명시합니다.
security는 보안 취약점이나 데이터 노출, critical은 프로덕션 중단이나 데이터 손실, high는 주요 기능 동작 불가입니다.
셋째, 결과를 변수로 추출해 다음 단계에서 활용합니다.
