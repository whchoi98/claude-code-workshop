# Slide 56: GitHub Actions / Reusable Workflow

**Part 4: CI/CD 통합**

## Code Blocks

### reusable

```bash
# 1. 호출되는 워크플로 (재사용 가능)
# .github/workflows/claude-review.yml in org/.github
name: Claude Review (Reusable)
on:
  workflow_call:
    inputs:
      prompt-file:
        required: true
        type: string
      allowed-tools:
        required: false
        type: string
        default: "Read,Grep,Glob"
      max-turns:
        required: false
        type: number
        default: 15
    secrets:
      ANTHROPIC_API_KEY:
        required: true

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install -g @anthropic-ai/claude-code
      - env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p "$(cat ${{ inputs.prompt-file }})" \
            --allowed-tools "${{ inputs.allowed-tools }}" \
            --max-turns ${{ inputs.max-turns }} \
            --output-format json | jq -r '.result' > review.md

# 2. 호출하는 워크플로
# .github/workflows/pr.yml in any-team/repo
name: PR Workflow
on: pull_request
jobs:
  review:
    uses: org/.github/.github/workflows/claude-review.yml@main
    with:
      prompt-file: prompts/security.md
      allowed-tools: "Read,Grep,Bash(gh pr:*)"
    secrets:
      ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

## Speaker Notes

Reusable Workflow는 여러 repo에서 같은 워크플로를 공유하는 패턴입니다.
1번 호출되는 워크플로는 .github 저장소의 workflows에 두는 것이 일반적입니다.
on workflow_call로 재사용 가능 선언을 합니다.
inputs에 prompt-file, allowed-tools, max-turns 같은 매개변수를 정의합니다.
required, type, default를 각각 명시합니다.
secrets 블록에 ANTHROPIC_API_KEY 같은 시크릿을 명시 선언합니다.
jobs 정의는 일반 워크플로와 동일합니다.
inputs context와 secrets context로 외부에서 전달된 값을 받아 사용합니다.
2번 호출하는 워크플로는 어느 팀의 어느 repo에서든 사용 가능합니다.
uses에 호출 경로를 적습니다.
org/.github/.github/workflows/파일명@브랜치 형식입니다.
with로 inputs를 전달하고 secrets 블록으로 시크릿을 명시 전달합니다.
조직 표준 워크플로를 정의하고 여러 팀이 매개변수만 다르게 해서 활용할 수 있습니다.
DRY 원칙에 따른 운영 효율성이 큽니다.
