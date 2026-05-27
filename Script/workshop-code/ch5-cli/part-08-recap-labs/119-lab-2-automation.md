# Slide 119: Lab 2 / 자동화 스크립트

**Part 8: RECAP & 4 LABS**

## Code Blocks

### Lab 2

```bash
#!/bin/bash
# my-pr-review.sh - 본인이 직접 작성하는 PR 리뷰
set -euo pipefail

PR_NUM="${1:?Usage: my-pr-review.sh <PR-number>}"

# Step 1: PR 정보 가져오기
echo "PR #$PR_NUM 정보 수집..."
PR_INFO=$(gh pr view "$PR_NUM" --json title,additions,deletions)
TITLE=$(echo "$PR_INFO" | jq -r '.title')
echo "제목: $TITLE"

# Step 2: 크기 체크
TOTAL=$(echo "$PR_INFO" | jq '.additions + .deletions')
if [ "$TOTAL" -gt 1000 ]; then
  echo "⚠️  PR이 큽니다 ($TOTAL 줄)"
  read -p "계속할까요? (y/N) " ANS
  [ "$ANS" != "y" ] && exit 0
fi

# Step 3: Claude로 리뷰
echo "Claude 리뷰 시작..."
REVIEW=$(claude -p "$(cat <<EOF
PR #$PR_NUM "$TITLE" 리뷰.

Diff:
$(gh pr diff "$PR_NUM")

관점: 1) 코드 품질 2) 보안 3) 테스트 4) 문서
출력: Markdown, 우선순위별 정리
EOF
)" \
  --allowed-tools "Read,Grep,Glob" \
  --max-turns 10 \
  --output-format json | jq -r '.result')

# Step 4: 결과 출력
echo ""
echo "=== Review ==="
echo "$REVIEW"

# Step 5: 코멘트 게시 여부 확인
read -p "PR에 코멘트 게시할까요? (y/N) " POST
if [ "$POST" = "y" ]; then
  gh pr comment "$PR_NUM" --body "$REVIEW"
  echo "✓ 코멘트 게시 완료"
fi

# 활용 예시
# $ chmod +x my-pr-review.sh
# $ ./my-pr-review.sh 1234
```

## Speaker Notes

Lab 2는 자동화 스크립트 작성 실습입니다.
약 30분 소요됩니다.
PR 리뷰 스크립트를 본인이 직접 작성합니다.
Step 1에서 PR 정보를 가져옵니다.
gh pr view로 title, additions, deletions를 추출합니다.
Step 2에서 크기를 체크합니다.
1000줄 초과 시 사용자에게 진행 여부를 묻습니다.
Step 3에서 Claude로 리뷰합니다.
heredoc으로 PR 정보를 포함한 프롬프트를 만들고 4가지 관점에서 리뷰를 요청합니다.
Step 4에서 결과를 출력합니다.
Step 5에서 코멘트 게시 여부를 사용자에게 묻고 동의 시 gh pr comment로 게시합니다.
이 스크립트는 본인 저장소의 실제 PR에 적용할 수 있습니다.
chmod로 실행 권한 부여 후 PR 번호를 인자로 실행합니다.
allowed-tools와 max-turns로 안전성과 비용을 통제하는 패턴이 핵심입니다.
