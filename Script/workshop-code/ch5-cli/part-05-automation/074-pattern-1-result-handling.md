# Slide 74: Pattern 1 / 결과 처리

**Part 5: 자동화 패턴**

## Code Blocks

### pr-review-bot.sh (cont)

```bash
# 이어서: pr-review-bot.sh

# 4. 라벨 부착
LABELS=$(echo "$REVIEW" | jq -r '.labels | join(",")')
gh pr edit "$PR_NUM" --add-label "$LABELS"

# 5. 종합 코멘트 게시
SUMMARY=$(echo "$REVIEW" | jq -r '.summary')
SEVERITY=$(echo "$REVIEW" | jq -r '.severity')
VERDICT=$(echo "$REVIEW" | jq -r '.verdict')

EMOJI="✅"
[ "$VERDICT" = "comment" ] && EMOJI="💬"
[ "$VERDICT" = "request_changes" ] && EMOJI="🚫"

COMMENT_BODY=$(cat <<EOF
## $EMOJI Claude AI 리뷰

**Summary:** $SUMMARY
**Severity:** $SEVERITY
**Verdict:** $VERDICT

### 세부 코멘트
$(echo "$REVIEW" | jq -r '.comments[] |
  "- **\(.file):\(.line)** [\(.severity)] \(.msg)"')

---
*자동 생성. 사람의 최종 리뷰가 필요합니다.*
EOF
)

gh pr comment "$PR_NUM" --body "$COMMENT_BODY"

# 6. 인라인 코멘트 (각 파일별)
echo "$REVIEW" | jq -c '.comments[]' | while read -r c; do
  FILE=$(echo "$c" | jq -r '.file')
  LINE=$(echo "$c" | jq -r '.line')
  MSG=$(echo "$c" | jq -r '.msg')
  if [ "$LINE" -gt 0 ]; then
    gh api "/repos/{owner}/{repo}/pulls/$PR_NUM/comments" \
      -X POST \
      -f body="$MSG" \
      -f path="$FILE" \
      -f line="$LINE" \
      -f commit_id="$(gh pr view $PR_NUM --json headRefOid \
                       -q '.headRefOid')"
  fi
done

echo "✓ PR #$PR_NUM 리뷰 완료"
```

## Speaker Notes

Pattern 1 결과 처리 이어집니다.
4단계 라벨 부착입니다.
AI 응답의 labels 배열을 join으로 콤마 구분 문자열로 만들고 gh pr edit로 추가합니다.
5단계 종합 코멘트 게시입니다.
verdict에 따라 다른 이모지를 사용합니다.
approve는 체크, comment는 말풍선, request_changes는 차단 이모지입니다.
heredoc으로 마크다운 본문을 구성합니다.
Summary, Severity, Verdict를 표시하고 jq로 comments 배열을 마크다운 목록으로 변환합니다.
자동 생성임을 마지막에 명시해 사용자가 알 수 있게 합니다.
6단계 인라인 코멘트입니다.
각 파일과 라인별 코멘트를 직접 GitHub API로 게시합니다.
gh api 명령으로 POST 요청하고 path, line, commit_id를 함께 전달합니다.
commit_id는 head ref의 oid를 jq로 추출합니다.
이로써 PR 화면에서 라인 옆에 직접 코멘트가 표시됩니다.
결과적으로 사람이 하는 리뷰와 거의 동일한 형태의 자동 리뷰가 완성됩니다.
