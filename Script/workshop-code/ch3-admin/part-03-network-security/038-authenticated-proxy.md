# Slide 38: Authenticated proxy

**Part 3: NETWORK & SECURITY**

## Code Blocks

### Auth proxy

```bash
# 1. Basic 인증 (URL에 자격증명 포함)
export HTTPS_PROXY=http://user:pass@proxy.company.com:8080
# 단점: PC 환경변수에 평문 저장 (지양)

# 2. 환경변수 분리 (조금 안전)
export PROXY_USER=user
export PROXY_PASS=$(cat ~/.proxy_pass)  # 파일에서 읽기
export HTTPS_PROXY=http://${PROXY_USER}:${PROXY_PASS}@proxy:8080

# 3. NTLM 인증 (Windows AD)
# cntlm 같은 로컬 프록시로 우회
# https://cntlm.sourceforge.net/
$ cat ~/.cntlm/cntlm.ini
Username  user
Domain    COMPANY
PassNTLMv2 ABC123...

Proxy     proxy.company.com:8080
NoProxy   localhost, .company.com
Listen    3128

# Claude는 cntlm으로
export HTTPS_PROXY=http://localhost:3128

# 4. 권장: Kerberos SSO 프록시
# 사용자 입력 없이 자동 인증
```

## Speaker Notes

인증 프록시를 통과하는 방법입니다.
Basic 인증은 URL에 자격증명을 포함하는 방식입니다.
간단하지만 PC 환경변수에 평문이 저장되므로 지양합니다.
조금 더 안전한 방법은 환경변수를 분리하는 것입니다.
PROXY_USER와 PROXY_PASS를 별도로 두고 파일에서 읽도록 합니다.
NTLM 인증, 즉 Windows AD 환경은 cntlm 같은 로컬 프록시로 우회합니다.
cntlm.ini에 자격증명을 한 번만 설정하고 NTLMv2 해시로 저장합니다.
Claude Code는 localhost의 cntlm 포트를 프록시로 사용합니다.
가장 권장하는 방법은 Kerberos SSO 프록시입니다.
Windows AD 로그인 시 자동으로 인증되어 사용자 입력이 필요 없습니다.
사내 IT팀과 협의해 SSO 프록시를 구축하는 것이 운영 부담을 줄이는 길입니다.
