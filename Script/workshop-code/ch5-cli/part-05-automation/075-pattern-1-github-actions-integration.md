# Slide 75: Pattern 1 / GitHub Actions 통합

**Part 5: 자동화 패턴**

## Code Blocks

### pr-review-bot.yml

```bash
# .github/workflows/pr-review-bot.yml
name: Claude PR Review Bot

on:
  pull_request:
    types: [opened, synchronize]

permissions:
  pull-requests: write
  issues: write
  contents: read

jobs:
  review:
    runs-on: ubuntu-latest
    timeout-minutes: 15

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Claude
        run: npm install -g @anthropic-ai/claude-code

      - name: Run review bot
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          GH_TOKEN: ${{ github.token }}
        run: |
          chmod +x .github/scripts/pr-review-bot.sh
          .github/scripts/pr-review-bot.sh \
            ${{ github.event.pull_request.number }}

      - name: Notify on failure
        if: failure()
        uses: 8398a7/action-slack@v3
        with:
          status: failure
          channel: '#ci-alerts'
          text: 'PR review bot failed'

# 효과
# - 모든 새 PR에 자동 리뷰
# - 라벨 자동 부착으로 분류
# - 인라인 코멘트로 정확한 위치 표시
# - 사람 리뷰는 비즈니스 결정에 집중
```

## Speaker Notes

Pattern 1을 GitHub Actions에 통합하는 워크플로입니다.
on pull_request로 opened와 synchronize 이벤트를 잡습니다.
permissions에 pull-requests write, issues write, contents read를 명시합니다.
코멘트 게시와 라벨 부착에 필요한 권한입니다.
timeout-minutes 15로 무한 실행을 방지합니다.
actions/checkout v4로 코드를 받고 fetch-depth 0으로 전체 history를 가져옵니다.
setup-node v4로 Node 20을 설치합니다.
Install Claude 스텝에서 npm install로 claude-code를 설치합니다.
Run review bot 스텝에서 환경변수를 주입하고 pr-review-bot.sh를 실행합니다.
ANTHROPIC_API_KEY는 secrets에서, GH_TOKEN은 github.token으로 전달합니다.
PR 번호는 github.event에서 가져옵니다.
Notify on failure 스텝은 실패 시에만 Slack에 알림을 보냅니다.
이 워크플로 등록으로 모든 새 PR에 자동 리뷰가 적용됩니다.
라벨 자동 부착으로 분류, 인라인 코멘트로 정확한 위치 표시, 사람은 비즈니스 결정에 집중하는 워크플로가 완성됩니다.
