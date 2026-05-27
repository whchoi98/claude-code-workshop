# Slide 54: GitHub Actions / 기본 워크플로

**Part 4: CI/CD 통합**

## Code Blocks

### pr-review.yml

```bash
# .github/workflows/pr-review.yml
name: PR Review with Claude

on:
  pull_request:
    types: [opened, synchronize, reopened]

permissions:
  pull-requests: write
  contents: read

jobs:
  review:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0    # 전체 git history 필요

      - name: Setup Node + Claude
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm install -g @anthropic-ai/claude-code

      - name: Run Claude review
        id: review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          GH_TOKEN: ${{ github.token }}
          PR_NUMBER: ${{ github.event.pull_request.number }}
        run: |
          REVIEW=$(claude -p "$(cat .github/prompts/review.md)
            PR: #$PR_NUMBER
            $(gh pr diff $PR_NUMBER)" \
            --allowed-tools "Read,Grep,Glob,Bash(gh pr:*)" \
            --max-turns 15 \
            --output-format json | jq -r '.result')
          echo "$REVIEW" > review.md
          # GitHub Actions output에 저장
          {
            echo 'review<<EOF'
            echo "$REVIEW"
            echo EOF
          } >> $GITHUB_OUTPUT

      - name: Post comment
        uses: marocchino/sticky-pull-request-comment@v2
        with:
          message: ${{ steps.review.outputs.review }}
```

## Speaker Notes

GitHub Actions 기본 워크플로입니다.
PR이 열리거나 변경되면 자동 실행됩니다.
permissions로 pull-requests write와 contents read 권한을 명시합니다.
timeout-minutes 10으로 무한 실행을 방지합니다.
actions/checkout v4로 코드를 가져오되 fetch-depth 0으로 전체 history를 받습니다.
actions/setup-node v4로 Node 20을 설치하고 npm install -g로 claude-code를 설치합니다.
Claude review 스텝에서 환경변수를 주입합니다.
ANTHROPIC_API_KEY, GH_TOKEN, PR_NUMBER 세 가지가 핵심입니다.
claude 명령에 프롬프트 파일을 cat으로 포함시키고 PR 정보도 함께 전달합니다.
allowed-tools로 권한을 좁히고 max-turns 15로 제한합니다.
GITHUB_OUTPUT에 리뷰 결과를 저장해 다음 스텝에서 참조 가능하게 합니다.
sticky-pull-request-comment v2 액션으로 PR에 코멘트를 게시합니다.
같은 PR에서 재실행 시 기존 코멘트가 업데이트됩니다.
