# Slide 88: /login /logout

**Part 4: AUTHENTICATION**

## Code Blocks

### auth commands

```bash
# /login - 인증 시작 또는 재인증
> /login
> Choose authentication method:
>   1. OAuth (Pro/Max subscription)
>   2. Anthropic API Key (paste)
>   3. Use AWS Bedrock (existing credentials)
>   4. Use Vertex AI (existing credentials)
> Selected: 1

# /logout - 현재 세션 인증 해제
> /logout
> Successfully signed out. Tokens cleared.

# 인증 상태 확인
> /status
> Auth: OAuth (user@example.com)
> Plan: Claude Max
> Tokens used today: 23%

# 또는 명령행에서
$ claude --auth-info
```

## Speaker Notes

Part 4 마지막 슬라이드로 인증 관련 슬래시 명령을 정리했습니다.
/login은 인증을 시작하거나 재인증할 때 사용합니다.
선택지로 OAuth, API Key, Bedrock, Vertex 네 가지가 표시되며, 원하는 방식을 선택하면 됩니다.
/logout은 현재 세션의 인증을 해제하고 저장된 토큰을 삭제합니다.
/status는 현재 사용 중인 인증 방식, 플랜, 일일 사용량을 한 번에 보여 줍니다.
명령행에서는 claude --auth-info로 동일한 정보를 확인할 수 있습니다.
명령은 세션을 빈번하게 전환하는 사용자나 디버깅 시 매우 유용합니다.
