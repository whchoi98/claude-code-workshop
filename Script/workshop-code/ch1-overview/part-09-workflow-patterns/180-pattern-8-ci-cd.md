# Slide 180: Pattern 8 CI/CD

**Part 9: WORKFLOW PATTERNS**

## Code Blocks

### CI/CD

```bash
# .github/workflows/claude-review.yml
name: Claude Code Review

on:
  pull_request:
    branches: [main]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          CLAUDE_DISABLE_UPDATE_CHECK: '1'
        run: |
          git diff origin/main..HEAD \
            | claude -p "이 PR을 CLAUDE.md 기준으로 리뷰해 줘" \
              --allowed-tools "Read,Grep,Glob" \
              --output-format json \
              > review.json

      - name: Comment on PR
        run: gh pr comment --body-file review.json
```

## Speaker Notes

Pattern 8 CI/CD Integration의 구체 예시로 GitHub Actions 워크플로를 보여드립니다.
pull_request 이벤트에 트리거되어 review job이 실행됩니다.
checkout으로 fetch-depth 0을 지정해 전체 히스토리를 받고, npm install -g로 Claude Code를 설치합니다.
ANTHROPIC_API_KEY는 GitHub Secrets에서 안전하게 주입하고, CLAUDE_DISABLE_UPDATE_CHECK로 매번 업데이트 체크하는 네트워크 호출을 막습니다.
git diff를 파이프해 Claude에 전달하고, 읽기 전용 도구만 허용해 안전성을 보장합니다.
JSON 결과를 받아 gh CLI로 PR에 자동 댓글을 게시합니다.
