# Slide 67: PR 자동 처리 완성 예시

**Part 4: CI/CD 통합**

## Code Blocks

### complete example

```bash
# .github/workflows/pr-complete.yml
name: PR Complete Workflow

on:
  pull_request:
    types: [opened, synchronize]

permissions:
  contents: read
  pull-requests: write
  issues: write

jobs:
  size-check:
    runs-on: ubuntu-latest
    outputs:
      should_review: ${{ steps.check.outputs.should_review }}
    steps:
      - id: check
        env:
          GH_TOKEN: ${{ github.token }}
        run: |
          CHANGES=$(gh pr view ${{ github.event.pull_request.number }} \
            --json additions,deletions -q '.additions + .deletions')
          if [ "$CHANGES" -gt 2000 ]; then
            echo "should_review=false" >> $GITHUB_OUTPUT
          else
            echo "should_review=true" >> $GITHUB_OUTPUT
          fi

  review:
    needs: size-check
    if: needs.size-check.outputs.should_review == 'true'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: npm install -g @anthropic-ai/claude-code

      - name: Review
        id: review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p "PR 종합 리뷰" \
            --allowed-tools "Read,Grep,Glob,Bash(gh pr:*)" \
            --max-turns 15 \
            --output-format json > review.json

      - name: Post comment
        uses: marocchino/sticky-pull-request-comment@v2
        with:
          message-path: ${{ steps.review.outputs.message-path }}

      - name: Notify on failure
        if: failure()
        uses: 8398a7/action-slack@v3
        with:
          status: failure
          channel: '#ci-alerts'
```

## Speaker Notes

PR 자동 처리 완성 예시입니다.
GitHub Actions 전체 흐름입니다.
size-check job이 먼저 실행됩니다.
PR의 변경 라인 수를 확인해 2000줄 초과 시 should_review를 false로 설정합니다.
GITHUB_OUTPUT에 저장해 다음 job에서 참조 가능합니다.
review job은 needs로 size-check를 기다리고 if 조건으로 should_review가 true일 때만 실행됩니다.
큰 PR은 자동으로 스킵되어 비용을 절감합니다.
actions/checkout v4로 코드를 받고 setup-node로 환경 준비, claude-code를 설치합니다.
Review 스텝에서 claude로 PR 종합 리뷰를 수행합니다.
allowed-tools와 max-turns로 비용과 안전성을 통제합니다.
Post comment 스텝에서 sticky comment 액션으로 PR에 결과를 게시합니다.
Notify on failure는 if failure 조건으로 실패 시에만 Slack에 알림을 보냅니다.
전체 흐름이 사람 개입 없이 완전 자동화됩니다.
