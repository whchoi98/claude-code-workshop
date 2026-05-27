# Slide 107: Auth troubleshooting

**Part 8: TROUBLESHOOTING**

## Code Blocks

### Auth debug

```bash
# Symptom: "Authentication failed" 또는 "No credentials"

# 1. doctor로 시작
$ claude doctor
  Auth:
    Provider: ?  → 이 값이 핵심 단서

# 2. Bedrock 사용 시
$ aws sts get-caller-identity  # 자격증명 확인
$ aws bedrock list-foundation-models --region ap-northeast-2
# 둘 다 성공해야 정상

# 3. SSO 사용 시
$ aws sso login --profile claude-code
# 브라우저 열림 → 로그인 → 토큰 발급
$ ls -la ~/.aws/sso/cache/  # 토큰 파일 존재 확인

# 4. API Key 사용 시 (Pro/Max)
$ ls -la ~/.claude/oauth.json  # 토큰 파일
$ claude /logout && claude /login  # 재로그인

# 5. 환경변수 충돌 확인
$ env | grep -i 'claude\|anthropic\|aws_'
# 의도치 않은 환경변수가 우선 적용될 수 있음

# 6. 디버그 모드
$ claude --debug
# Task 호출 내부와 자격증명 흐름 출력
```

## Speaker Notes

인증 트러블슈팅을 단계별로 다룹니다.
Authentication failed나 No credentials 증상입니다.
1단계 claude doctor로 시작합니다.
Auth 섹션의 Provider 값이 핵심 단서입니다.
Bedrock인지, AWS Bedrock SSO인지, OAuth인지 확인합니다.
2단계 Bedrock 사용 시 aws sts get-caller-identity로 자격증명을 확인합니다.
aws bedrock list-foundation-models 명령으로 Bedrock 접근도 검증합니다.
둘 다 성공해야 정상입니다.
3단계 SSO 사용 시 aws sso login으로 재로그인합니다.
SSO 토큰 캐시 파일이 ~/.aws/sso/cache 디렉토리에 있는지 확인합니다.
4단계 API Key 또는 OAuth 사용 시 ~/.claude/oauth.json 토큰을 확인합니다.
/logout 후 /login으로 재로그인합니다.
5단계 환경변수 충돌을 확인합니다.
claude, anthropic, aws_ 관련 환경변수가 의도치 않게 설정되어 있을 수 있습니다.
6단계 --debug 옵션으로 상세 로그를 봅니다.
