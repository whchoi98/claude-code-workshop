# Slide 68: 다른 CI 시스템 한눈에

**Part 4: CI/CD 통합**

## Code Blocks

### other CI

```bash
# 1. CircleCI (.circleci/config.yml)
version: 2.1
jobs:
  review:
    docker:
      - image: node:20-alpine
    steps:
      - checkout
      - run: npm install -g @anthropic-ai/claude-code
      - run:
          name: Run Claude
          environment:
            ANTHROPIC_API_KEY: $ANTHROPIC_API_KEY
          command: |
            claude -p "..." --output-format json

workflows:
  pr-review:
    jobs:
      - review:
          filters:
            branches:
              ignore: main

# 2. Travis CI (.travis.yml)
language: node_js
node_js: '20'
before_install:
  - npm install -g @anthropic-ai/claude-code
env:
  - ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY
script:
  - claude -p "..." --output-format json > result.json

# 3. Azure DevOps (azure-pipelines.yml)
trigger:
- main

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: NodeTool@0
  inputs:
    versionSpec: '20.x'
- script: npm install -g @anthropic-ai/claude-code
- script: |
    claude -p "..." --output-format json
  env:
    ANTHROPIC_API_KEY: $(ANTHROPIC_API_KEY)
```

## Speaker Notes

다른 CI 시스템에서의 통합 패턴입니다.
CircleCI의 .circleci/config.yml 예시입니다.
version 2.1로 시작하고 jobs에 review를 정의합니다.
docker로 node:20-alpine 이미지를 사용합니다.
checkout, install, run claude 3단계로 진행됩니다.
workflows에 filters로 main 브랜치를 제외하면 PR에서만 실행됩니다.
Travis CI의 .travis.yml 예시입니다.
language와 node_js 버전을 명시하고 before_install에서 claude-code를 설치합니다.
env 블록에 ANTHROPIC_API_KEY를 주입하고 script에서 claude를 호출합니다.
Azure DevOps의 azure-pipelines.yml 예시입니다.
trigger로 main 브랜치 변경 시 실행하고 ubuntu-latest VM에서 실행됩니다.
NodeTool 태스크로 Node 설치 후 npm으로 claude-code 설치, claude 호출 순서입니다.
환경변수는 달러 괄호 형식으로 참조합니다.
3가지 시스템 모두 install, 인증, 호출의 동일한 패턴을 따릅니다.
GitHub Actions와 GitLab CI를 익히면 다른 시스템도 쉽게 적용 가능합니다.
