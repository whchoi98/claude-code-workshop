# Slide 78: Pattern 2 / 액션 실행

**Part 5: 자동화 패턴**

## Code Blocks

### triage actions

```bash
# 이어서: triage-issue.sh

# 4. 라벨 부착
gh issue edit "$ISSUE_NUM" \
  --add-label "$CATEGORY,priority:$PRIORITY,effort:$EFFORT"

# 5. 정보 부족 시 자동 응답
if [ "$NEEDS_INFO" = "true" ]; then
  gh issue comment "$ISSUE_NUM" --body "$(cat <<EOF
👋 이슈 등록 감사합니다.

좀 더 정확히 도와드리기 위해 다음 정보가 필요합니다:
- 발생 환경 (OS, 브라우저, 버전)
- 재현 단계
- 예상 동작 vs 실제 동작
- 스크린샷 또는 로그

업데이트 부탁드립니다.
EOF
)"
  gh issue edit "$ISSUE_NUM" --add-label "needs-info"
fi

# 6. 보안 이슈는 별도 채널로
if [ "$CATEGORY" = "security" ]; then
  curl -X POST "$SECURITY_SLACK_WEBHOOK" \
    -H 'Content-Type: application/json' \
    -d "$(jq -n --arg num "$ISSUE_NUM" --arg sum "$SUMMARY" \
      '{text: ":warning: Security issue #\($num): \($sum)"}')"
fi

# 7. 담당자 자동 할당 (suggested의 첫 번째)
ASSIGNEE=$(echo "$ANALYSIS" | jq -r '.suggested_assignees[0] // empty')
if [ -n "$ASSIGNEE" ] && [ "$ASSIGNEE" != "null" ]; then
  gh issue edit "$ISSUE_NUM" --add-assignee "$ASSIGNEE"
fi

# 8. 중복 감지 시 안내
DUP=$(echo "$ANALYSIS" | jq -r '.duplicate_of // empty')
if [ -n "$DUP" ] && [ "$DUP" != "null" ]; then
  gh issue comment "$ISSUE_NUM" --body \
    "🔄 이 이슈는 #$DUP와 중복일 수 있습니다."
fi

echo "✓ Issue #$ISSUE_NUM 트리아지 완료: $CATEGORY/$PRIORITY"
```

## Speaker Notes

Pattern 2 액션 실행 단계입니다.
4단계 라벨 부착입니다.
gh issue edit의 --add-label로 카테고리, 우선순위, effort 3가지 라벨을 한 번에 부착합니다.
5단계 정보 부족 시 자동 응답입니다.
needs_more_info가 true면 정중한 안내 코멘트를 자동 게시합니다.
발생 환경, 재현 단계, 예상 동작 대비 실제 동작, 스크린샷 또는 로그 4가지를 요청합니다.
needs-info 라벨도 함께 부착해 검색이 쉽게 합니다.
6단계 보안 이슈는 별도 채널로 알림입니다.
category가 security면 보안 전용 Slack webhook으로 즉시 알림을 보냅니다.
7단계 담당자 자동 할당입니다.
suggested_assignees의 첫 번째 사람을 자동 할당합니다.
빈 배열이거나 null이면 스킵합니다.
8단계 중복 감지입니다.
duplicate_of가 명시되면 그 이슈와 중복일 수 있다고 안내 코멘트를 답니다.
모든 액션이 자동 수행되어 트리아지 시간이 90 퍼센트 이상 단축됩니다.
