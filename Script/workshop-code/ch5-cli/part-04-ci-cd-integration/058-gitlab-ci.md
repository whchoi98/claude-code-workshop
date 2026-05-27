# Slide 58: GitLab CI 고급 패턴

**Part 4: CI/CD 통합**

## Code Blocks

### GitLab rules

```bash
# rules: 조건부 실행 (only/except 대체)
review:
  stage: review
  rules:
    # MR이고 main 대상이고 .py 파일이 바뀐 경우만
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      changes:
        - "**/*.py"
        - "**/*.js"
      when: on_success

    # nightly 빌드는 모든 코드 분석
    - if: $CI_PIPELINE_SOURCE == "schedule"
      when: always

    # 그 외는 실행 안 함
    - when: never

  script:
    - claude -p "..." --output-format json

# 환경별 설정
.review_base:
  script:
    - claude -p "$PROMPT" \
        --model "$MODEL" \
        --max-turns "$MAX_TURNS" \
        --output-format json | jq -r '.result'

review:staging:
  extends: .review_base
  environment: staging
  variables:
    PROMPT: "Staging PR 리뷰"
    MODEL: "claude-haiku-4-5"
    MAX_TURNS: "10"
  rules:
    - if: $CI_COMMIT_BRANCH == "staging"

review:production:
  extends: .review_base
  environment: production
  variables:
    PROMPT: "Production PR 종합 리뷰 + 보안 검토"
    MODEL: "claude-sonnet-4-5"
    MAX_TURNS: "30"
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

## Speaker Notes

GitLab CI 고급 패턴입니다.
rules는 only와 except를 대체하는 새로운 조건부 실행 방식입니다.
첫 번째 rule은 MR 이벤트이고 main 대상이고 .py나 .js 파일이 변경된 경우만 on_success로 실행합니다.
두 번째 rule은 nightly 빌드처럼 스케줄 이벤트일 때 항상 실행합니다.
그 외는 never로 실행하지 않습니다.
rules는 위에서부터 평가되어 첫 매칭에서 결정됩니다.
환경별 설정 패턴도 강력합니다.
.review_base에 공통 script를 정의합니다.
점 prefix는 hidden job으로 직접 실행되지 않고 템플릿으로만 사용됩니다.
review:staging은 extends로 base를 상속하고 environment, variables, rules를 오버라이드합니다.
staging은 Haiku, max-turns 10으로 가볍게 설정합니다.
review:production은 Sonnet, max-turns 30으로 더 철저합니다.
환경별 다른 동작을 깔끔하게 구현할 수 있습니다.
