# Slide 90: CI integration

**Part 7: PATTERN 4 / DOCS WRITER**

## Code Blocks

### docs-sync.yml

```bash
# .github/workflows/docs-sync.yml
name: Documentation Sync
on:
  pull_request:
    paths:
      - 'src/**/*.{js,ts}'

jobs:
  sync-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Sync docs
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p "@docs-writer 이번 PR의 코드 변경에 맞춰
            관련 문서를 docs/ 디렉토리에서 업데이트해 주세요."

      - name: Commit docs
        run: |
          git config user.email "ci@example.com"
          git add docs/
          git diff --staged --quiet || git commit -m "docs: sync"
          git push
```

## Speaker Notes

docs-writer를 CI에 통합하는 패턴입니다.
GitHub Actions 워크플로 예시를 봅니다.
PR이 열릴 때 src 디렉토리의 .js나 .ts 파일이 변경되면 트리거됩니다.
ubuntu-latest에서 Claude Code를 npm으로 설치합니다.
ANTHROPIC_API_KEY는 GitHub Secrets에서 안전하게 주입합니다.
claude -p 헤드리스 모드로 @docs-writer를 명시 호출합니다.
이번 PR의 코드 변경에 맞춰 docs 디렉토리를 업데이트해 달라고 지시합니다.
마지막으로 변경된 문서를 git에 커밋하고 푸시합니다.
결과적으로 코드 변경과 함께 관련 문서가 자동으로 동기화됩니다.
PR 리뷰어는 코드와 문서를 한 번에 검토할 수 있습니다.
