# Slide 102: 환경변수 트러블슈팅

**Part 6: 환경변수와 설정**

## Code Blocks

### troubleshooting

```bash
# 문제 1: 환경변수가 안 보임
# 증상: claude doctor에서 ANTHROPIC_API_KEY가 not set

# 원인 1: export 안 함
$ ANTHROPIC_API_KEY=sk-...    # 잘못
$ export ANTHROPIC_API_KEY=sk-...    # 올바름

# 원인 2: 새 셸에서 적용 안 됨
$ source ~/.bashrc
# 또는 ~/.bashrc에 export 추가 후 새 터미널

# 원인 3: sudo 후 환경변수 안 가져감
$ sudo -E claude doctor    # -E 옵션으로 환경 유지

# 문제 2: 프록시 통과 안 됨
# 증상: connect ETIMEDOUT

# 진단
$ curl -v https://api.anthropic.com 2>&1 | head -20

# 원인 확인
$ echo $HTTPS_PROXY
$ echo $NO_PROXY
$ env | grep -i proxy

# 해결
$ export HTTPS_PROXY=http://proxy.company.com:8080
$ export NO_PROXY=localhost,127.0.0.1,.internal

# 문제 3: 사내 CA 인식 안 됨
# 증상: unable to verify the first certificate

$ openssl x509 -in /etc/ssl/company-ca.pem -text -noout
# 인증서가 유효한지 확인

$ export NODE_EXTRA_CA_CERTS=/etc/ssl/company-ca.pem
$ claude doctor

# 문제 4: Bedrock 자격증명 만료
# 증상: ExpiredTokenException

$ aws sso login --profile production
$ export AWS_PROFILE=production

# 문제 5: direnv 적용 안 됨
$ direnv allow .
$ direnv reload

# 종합 디버그
$ CLAUDE_CODE_LOG_LEVEL=debug claude doctor 2>&1 | less
```

## Speaker Notes

환경변수 트러블슈팅에서 자주 발생하는 5가지 문제입니다.
문제 1은 환경변수가 안 보이는 경우입니다.
export를 안 한 경우, 새 셸에서 적용 안 된 경우, sudo로 환경변수가 안 넘어간 경우가 있습니다.
export 명령 사용, source로 .bashrc 재로드, sudo -E 옵션으로 해결합니다.
문제 2는 프록시 통과 안 됨입니다.
connect ETIMEDOUT 증상이 나타납니다.
curl -v로 직접 테스트하고 HTTPS_PROXY, NO_PROXY 환경변수를 점검합니다.
문제 3은 사내 CA 인식 안 됨입니다.
unable to verify certificate 에러가 발생합니다.
openssl로 인증서 유효성을 확인하고 NODE_EXTRA_CA_CERTS를 설정합니다.
문제 4는 Bedrock 자격증명 만료입니다.
ExpiredTokenException이 발생하면 aws sso login으로 재인증합니다.
문제 5는 direnv 적용 안 됨입니다.
direnv allow와 reload로 명시 적용합니다.
종합 디버그는 LOG_LEVEL debug로 claude doctor를 실행하면 모든 로딩 과정을 추적할 수 있습니다.
