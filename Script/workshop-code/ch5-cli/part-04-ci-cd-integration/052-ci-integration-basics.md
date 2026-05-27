# Slide 52: CI 통합 기본 패턴

**Part 4: CI/CD 통합**

## Code Blocks

### common pattern

```bash
# 모든 CI 시스템에 공통된 기본 명령 형태
$ claude -p "PR #${PR_NUMBER} 리뷰" \
    --allowed-tools "Read,Grep,Glob,Bash(gh pr:*)" \
    --max-turns 15 \
    --output-format json | jq -r '.result'
```

## Speaker Notes

CI 통합 기본 패턴은 3가지 핵심 요소입니다.
Step 1은 설치입니다.
npm install -g 명령으로 claude-code 패키지를 전역 설치합니다.
CI runner에 매번 설치하거나 결과를 캐싱해서 재사용합니다.
Step 2는 인증입니다.
ANTHROPIC_API_KEY 환경변수를 CI의 secret 기능으로 안전하게 전달합니다.
Bedrock이나 Vertex 경로도 동일한 패턴으로 자격증명을 주입합니다.
Step 3는 호출입니다.
Headless 모드 -p와 --output-format json을 함께 사용합니다.
jq로 결과를 파싱한 후 후속 액션을 수행합니다.
공통 명령 형태가 모든 CI 시스템에서 동일합니다.
claude -p에 PR 번호 같은 환경변수를 주입하고 allowed-tools, max-turns, output-format을 명시합니다.
이 표준 패턴을 익히면 어떤 CI 시스템에도 쉽게 적용할 수 있습니다.
