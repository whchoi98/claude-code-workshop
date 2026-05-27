# Slide 24: 자동화 1 / PR 리뷰

**Part 2: HEADLESS 모드 심화**

## Code Blocks

### pr-review.sh

```bash
#!/bin/bash
# pr-review.sh - GitHub PR 자동 리뷰
set -euo pipefail

PR_NUM="${1:?Usage: pr-review.sh <PR-number>}"

# 1. PR 정보 수집
PR_TITLE=$(gh pr view "$PR_NUM" --json title -q '.title')
PR_DIFF=$(gh pr diff "$PR_NUM")

# 2. Claude로 리뷰
REVIEW=$(claude -p "$(cat <<EOF
다음 PR을 리뷰해 주세요.

제목: $PR_TITLE

변경 내용:
$PR_DIFF

검토 관점:
1. 코드 품질 (가독성, 명명, 복잡도)
2. 보안 (OWASP Top 10)
3. 테스트 커버리지
4. 성능 영향

출력: Markdown, 우선순위별 (Critical/Important/Suggestion)
EOF
)" \
  --allowed-tools "Read,Grep,Glob" \
  --max-turns 10 \
  --output-format json | jq -r '.result')

# 3. PR에 코멘트 게시
echo "$REVIEW" | gh pr comment "$PR_NUM" --body-file -

echo "✓ PR #$PR_NUM 리뷰 완료"

# 사용 예시
# $ ./pr-review.sh 1234
```

## Speaker Notes

자동화 1번 PR 리뷰 완성 스크립트입니다.
set -euo pipefail로 엄격한 셸 모드를 활성화합니다.
첫 인자로 PR 번호를 받고 없으면 즉시 사용법 표시 후 종료합니다.
1단계 PR 정보 수집입니다.
gh pr view로 제목을, gh pr diff로 변경 내용을 가져옵니다.
2단계 Claude로 리뷰입니다.
heredoc으로 PR 정보를 포함한 큰 프롬프트를 구성합니다.
검토 관점 4가지를 명시하고 출력 형식을 Markdown 우선순위별로 지정합니다.
allowed-tools로 Read, Grep, Glob만 허용해 안전합니다.
max-turns 10으로 무한 루프를 방지하고 JSON 출력 후 jq로 result만 추출합니다.
3단계 PR에 코멘트를 게시합니다.
gh pr comment의 --body-file 옵션에 - 를 주면 stdin을 본문으로 사용합니다.
사용은 ./pr-review.sh 1234처럼 PR 번호만 주면 됩니다.
