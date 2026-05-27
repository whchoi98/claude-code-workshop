# Slide 72: Auth Method 1: OAuth

**Part 4: AUTHENTICATION**

## Code Blocks

### OAuth Flow

```bash
# 1. 첫 실행 (또는 /login 명령)
$ claude
> Welcome to Claude Code! Please sign in to continue.
> Press Enter to open the browser for authentication...
[Enter]

# 2. 브라우저에서 OAuth 동의 (자동으로 콘솔 사이트 열림)
#    - Claude.ai 계정 로그인
#    - "Authorize Claude Code" 클릭
#    - 임시 코드가 CLI로 자동 전달됨

# 3. 인증 완료 후 자동으로 CLI에 복귀
> Successfully signed in as user@example.com
> Plan: Claude Max

# 4. 로그아웃
/logout
```

## Speaker Notes

첫 번째 인증 방식, Claude Pro 또는 Max 구독자의 OAuth 인증 흐름입니다.
1단계 claude 명령을 처음 실행하면 자동으로 로그인 안내가 표시되고 Enter를 누르면 브라우저가 열립니다.
2단계 브라우저에서 Claude.ai 계정으로 로그인하고 Authorize Claude Code 버튼을 클릭하면, 임시 코드가 CLI로 자동 전달됩니다.
3단계 CLI에 복귀하면 로그인된 이메일과 플랜 정보가 표시됩니다.
4단계 로그아웃은 /logout 슬래시 명령으로 가능합니다.
이 방식은 PKCE 표준을 사용해 안전하며, 별도의 API Key 관리 없이 가장 빠르게 시작할 수 있습니다.
