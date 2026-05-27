# Slide 29: OAuth Pro/Max

**Part 2: CREDENTIALS MANAGEMENT**

## Code Blocks

### OAuth flow

```bash
# 1. Anthropic 계정 생성 + 결제 카드 등록
# https://claude.ai 에서 Pro 또는 Max 구독

# 2. Claude Code에서 OAuth 로그인
$ claude
> /login
# 브라우저가 열리며 OAuth 인증 진행
# 성공 시 토큰이 ~/.claude/oauth.json에 저장

# 3. 가입 플랜에 따른 차이
- Pro:  표준 사용량 (개인 개발 적합)
- Max:  더 큰 컨텍스트 사용량, 우선 처리
- Team/Enterprise: 별도 협의

# 4. 토큰 자동 회전 (시간제 만료 후)
- access_token: 1시간
- refresh_token: 자동 갱신

# 5. 적합한 경우
- 1-5인 스타트업, 작은 팀
- PoC, 트라이얼 단계
- 개인 개발자

# 6. 제한사항
- 사내 SSO 통합 불가
- IAM 기반 권한 통제 어려움
- 감사 로그가 Anthropic 측에만 남음
```

## Speaker Notes

OAuth, 즉 Anthropic Pro 또는 Max 구독 옵션입니다.
소규모 조직이나 개인 사용에 적합합니다.
1단계 Anthropic 계정을 만들고 결제 카드를 등록합니다.
claude.ai에서 Pro 또는 Max를 구독합니다.
2단계 Claude Code에서 OAuth 로그인합니다.
/login 명령을 실행하면 브라우저가 열리고 OAuth 인증이 진행됩니다.
성공 시 토큰이 사용자 홈의 oauth.json에 저장됩니다.
3단계 가입 플랜에 따라 차이가 있습니다.
Pro는 표준 사용량으로 개인 개발에 적합합니다.
Max는 더 큰 컨텍스트 사용량과 우선 처리가 제공됩니다.
Team이나 Enterprise는 별도 협의가 필요합니다.
4단계 토큰은 자동 회전됩니다.
access token은 1시간 유효하고 refresh token으로 자동 갱신됩니다.
5단계 적합한 경우는 1-5인 스타트업이나 PoC, 개인 개발자입니다.
6단계 제한사항도 명확합니다.
사내 SSO 통합이 불가하고 IAM 권한 통제가 어렵습니다.
감사 로그가 Anthropic 측에만 남는 제약이 있습니다.
