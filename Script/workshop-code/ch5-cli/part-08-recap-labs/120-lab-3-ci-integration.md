# Slide 120: Lab 3 / CI 통합

**Part 8: RECAP & 4 LABS**

## Code Blocks

### Lab 3

```bash
# 1. 저장소에 secret 등록
# GitHub → Settings → Secrets and variables → Actions
# Name: ANTHROPIC_API_KEY
# Value: sk-ant-api03-...

# 2. .github/workflows/my-claude.yml 작성
name: My Claude Workflow

on:
  pull_request:
    types: [opened]
  workflow_dispatch:    # 수동 실행도 가능

permissions:
  pull-requests: write
  contents: read

jobs:
  test-claude:
    runs-on: ubuntu-latest
    timeout-minutes: 5
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Claude
        run: npm install -g @anthropic-ai/claude-code

      - name: Test Claude
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          # 간단한 테스트
          echo "안녕하세요" | claude -p "한국어 인사를 영어로" \
            --output-format json | jq -r '.result'

      - name: Show usage
        if: always()
        run: |
          echo "Workflow 완료 시각: $(date)"

# 3. PR 만들어서 자동 실행 확인
$ git checkout -b test-claude-action
$ git add .github/workflows/my-claude.yml
$ git commit -m "Add test workflow"
$ git push origin test-claude-action
$ gh pr create --title "Test Claude action" --body "Testing"

# 4. Actions 탭에서 결과 확인
$ gh run list
$ gh run watch    # 실시간 확인
```

## Speaker Notes

Lab 3는 CI 통합 실습입니다.
약 30분 소요됩니다.
GitHub Actions 워크플로를 처음부터 작성합니다.
1단계 저장소에 secret을 등록합니다.
GitHub의 Settings에서 ANTHROPIC_API_KEY를 명시합니다.
2단계 .github/workflows/my-claude.yml을 작성합니다.
on pull_request의 opened와 workflow_dispatch 트리거를 설정합니다.
permissions에 pull-requests write와 contents read를 명시합니다.
timeout-minutes 5로 짧게 잡습니다.
스텝은 checkout, setup-node, install claude, test claude 순서입니다.
환경변수로 secrets context의 ANTHROPIC_API_KEY를 주입합니다.
간단한 테스트로 한국어 인사를 영어로 번역해 봅니다.
show usage는 if always 조건으로 실패 시에도 실행됩니다.
3단계 PR을 만들어 자동 실행을 확인합니다.
새 브랜치, 커밋, push, gh pr create로 흐름을 완성합니다.
4단계 Actions 탭에서 결과를 확인합니다.
gh run list와 watch 명령으로 실시간 모니터링도 가능합니다.
첫 CI 통합 워크플로가 완성됩니다.
