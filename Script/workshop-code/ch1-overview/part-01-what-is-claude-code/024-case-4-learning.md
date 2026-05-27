# Slide 24: Case 4 코드베이스 학습

**Part 1: WHAT IS CLAUDE CODE**

## Code Blocks

### TYPICAL FLOW

```
User: 이 프로젝트의 인증 흐름을 설명해 주세요.

Claude:
  1. Read    package.json, README.md (스택 파악)
  2. Glob    "**/auth/**" → 관련 파일 12개 식별
  3. Read    src/auth/middleware.js, src/auth/jwt.js, ...
  4. Grep    "verify|authenticate|sign" 패턴 확인
  5. Output  Markdown 다이어그램과 함께 흐름 설명
            - Login → JWT 발급 → 토큰 검증 미들웨어
            - Refresh 토큰 회전 정책 / 권한 매트릭스
```

## Speaker Notes

네 번째 사례는 코드베이스 학습입니다.
새로 합류한 프로젝트의 인증 흐름을 자연어로 묻는 시나리오를 예로 들어보겠습니다.
Claude Code는 먼저 package.json과 README를 읽어 기술 스택을 파악하고, Glob 패턴으로 auth 관련 파일들을 자동 식별합니다.
그 다음 핵심 파일들을 Read로 읽고 verify, authenticate, sign 같은 키워드를 Grep으로 확인한 후, Markdown 형식의 흐름 다이어그램과 함께 설명을 만들어 줍니다.
로그인 시 JWT 발급 흐름, 토큰 검증 미들웨어, 리프레시 토큰 회전 정책, 권한 매트릭스까지 한 번에 설명을 받을 수 있습니다.
이 패턴은 신규 합류 멤버의 온보딩 기간을 며칠에서 몇 시간 수준으로 단축할 수 있으며, 학습 결과를 CLAUDE.md에 저장하면 팀 전체가 같은 자산을 활용할 수 있습니다.
