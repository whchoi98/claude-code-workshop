# Slide 57: GitLab CI / 기본 설정

**Part 4: CI/CD 통합**

## Code Blocks

### .gitlab-ci.yml

```bash
# .gitlab-ci.yml
image: node:20

stages:
  - install
  - review
  - notify

variables:
  CLAUDE_VERSION: "1.2.0"

# Pipeline 캐싱 (node_modules)
cache:
  key: "claude-${CLAUDE_VERSION}"
  paths:
    - .npm-cache/

# Stage 1: 설치 (캐시 활용)
install:claude:
  stage: install
  script:
    - npm config set cache .npm-cache
    - npm install -g @anthropic-ai/claude-code@$CLAUDE_VERSION
    - claude --version    # 확인
  artifacts:
    paths:
      - .npm-cache/

# Stage 2: PR 리뷰
review:
  stage: review
  needs: [install:claude]
  only:
    - merge_requests
  variables:
    ANTHROPIC_API_KEY: $ANTHROPIC_API_KEY
  script:
    - |
      claude -p "MR !$CI_MERGE_REQUEST_IID 리뷰: \
        $(git diff origin/$CI_MERGE_REQUEST_TARGET_BRANCH_NAME...HEAD)" \
        --allowed-tools "Read,Grep,Glob" \
        --max-turns 15 \
        --output-format json | jq -r '.result' > review.md
  artifacts:
    paths:
      - review.md
    expire_in: 1 week
```

## Speaker Notes

GitLab CI 기본 설정 파일 .gitlab-ci.yml입니다.
image로 기본 컨테이너 환경을 명시합니다.
node:20 이미지를 사용합니다.
stages로 단계를 정의합니다.
install, review, notify 3단계입니다.
variables로 전역 변수를 정의할 수 있습니다.
cache 블록으로 파이프라인 캐싱을 활성화합니다.
key는 캐시 식별자이고 paths는 캐싱할 경로입니다.
Stage 1 install:claude에서 npm install로 claude-code를 설치합니다.
캐시를 활용하면 두 번째 실행부터 빠릅니다.
claude --version으로 정상 설치를 확인합니다.
artifacts로 다음 stage에 전달할 파일을 명시합니다.
Stage 2 review는 needs로 install 완료를 기다립니다.
only: merge_requests로 MR 이벤트에만 실행됩니다.
ANTHROPIC_API_KEY는 GitLab의 CI/CD Settings의 Variables에서 설정합니다.
claude 명령에 MR ID와 diff를 함께 전달합니다.
expire_in 1 week으로 artifact 자동 정리합니다.
