# Slide 64: CI 보안 검증

**Part 4: CI/CD 통합**

## Code Blocks

### security

```bash
# 위협: 외부 기여자가 악성 PR을 만들어 시크릿을 탈취하려 함

# 1. fork PR은 secrets 차단 (GitHub 기본)
# pull_request 이벤트에서 PR이 fork에서 오면
# secrets는 자동으로 비어 있음
# 의도: 악성 PR이 시크릿을 사용 못 함

# 2. workflow_run + pull_request_target 패턴
# Step A: 안전한 워크플로 (코드 다운로드만)
name: PR Trigger
on: pull_request
jobs:
  collect:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/upload-artifact@v4
        with:
          name: pr-data
          path: |
            .

# Step B: 권한 있는 워크플로
name: Run Claude
on:
  workflow_run:
    workflows: ["PR Trigger"]
    types: [completed]
permissions:
  pull-requests: write
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: pr-data
      - env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p "..." \
            --disallowed-tools "Write,Edit,Bash" \
            --output-format json

# 3. 도구 권한을 좁게 제한
$ claude -p "..." \
    --allowed-tools "Read,Grep,Glob" \
    --disallowed-tools "Write,Edit,Bash"
# 코드 변경은 금지
```

## Speaker Notes

CI 보안 검증, 악성 PR 방어 패턴입니다.
위협을 먼저 이해해야 합니다.
외부 기여자가 악성 PR을 만들어 시크릿을 탈취하려 시도할 수 있습니다.
1번 fork PR은 secrets 차단입니다.
GitHub 기본 동작으로 fork에서 온 PR은 secrets가 자동으로 비어 있습니다.
악성 PR이 시크릿을 사용할 수 없게 차단됩니다.
2번 workflow_run + pull_request_target 패턴입니다.
두 워크플로로 분리합니다.
Step A는 안전한 워크플로로 PR 데이터를 다운로드해 artifact에 저장만 합니다.
Step B는 권한 있는 워크플로로 workflow_run 트리거로 실행됩니다.
artifact에서 데이터를 받아 claude를 호출합니다.
claude는 disallowed-tools로 Write, Edit, Bash를 차단해 read-only로만 동작합니다.
3번 도구 권한을 좁게 제한합니다.
Read, Grep, Glob만 허용하고 코드 변경은 금지합니다.
악성 코드가 main 브랜치에 들어갈 가능성을 완전히 차단합니다.
