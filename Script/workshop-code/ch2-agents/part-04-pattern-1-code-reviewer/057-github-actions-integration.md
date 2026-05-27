# Slide 57: GitHub Actions integration

**Part 4: PATTERN 1 / CODE REVIEWER**

## Code Blocks

### GitHub Actions

```typescript
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
      
      - name: Run Code Reviewer
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          git diff origin/main...HEAD | claude -p \
            "code-reviewer로 이 PR을 검토" \
            --allowed-tools "Read,Grep,Glob" \
            --output-format text > review.md
      
      - name: Post Review Comment
        uses: actions/github-script@v7
        with:
          script: |
            const review = require('fs').readFileSync('review.md', 'utf8');
            github.rest.issues.createComment({ ... body: review ... });
```

## Speaker Notes

세 번째 호출 방법은 GitHub Actions 통합입니다.
PR 생성 시 자동으로 리뷰 댓글이 게시되도록 워크플로를 구성합니다.
워크플로 파일을 살펴봅니다.
on pull_request 트리거로 main 브랜치 대상 PR에서 실행됩니다.
ubuntu-latest 러너에서 동작합니다.
3단계로 구성됩니다.
1단계는 코드 체크아웃입니다.
fetch-depth 0으로 전체 git 히스토리를 가져옵니다.
diff 계산에 필요합니다.
2단계는 Claude Code 설치입니다.
npm으로 글로벌 설치합니다.
3단계는 리뷰 실행입니다.
ANTHROPIC_API_KEY를 secrets에서 가져옵니다.
git diff와 claude -p를 파이프로 연결합니다.
allowed-tools 플래그로 CI 환경에서 권한을 더 좁힙니다.
결과를 review.md 파일로 저장합니다.
마지막 단계로 PR에 댓글로 자동 게시합니다.
github-script 액션으로 GitHub API를 호출해 댓글을 생성합니다.
