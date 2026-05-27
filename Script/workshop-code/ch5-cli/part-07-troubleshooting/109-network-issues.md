# Slide 109: 네트워크 문제 진단

**Part 7: 디버깅과 트러블슈팅**

## Code Blocks

### network issues

```bash
# Symptom: connect ETIMEDOUT, unable to verify certificate

# 진단 1: 기본 네트워크 도달성
$ curl -v https://api.anthropic.com 2>&1 | head -20
# 빠른 응답: 네트워크 OK
# Timeout: 프록시 문제 가능성

# 진단 2: 프록시 환경변수
$ env | grep -i proxy
# HTTPS_PROXY가 설정됐는지, 형식 정확한지 확인

# 진단 3: 사내 CA 인식
$ openssl s_client -connect api.anthropic.com:443 \
    -CAfile $NODE_EXTRA_CA_CERTS < /dev/null
# Verify return code: 0 (ok) 면 CA 정상

# 진단 4: DNS 확인
$ nslookup api.anthropic.com
$ dig api.anthropic.com

# 진단 5: IPv6 문제 (드물지만 발생)
$ curl -4 https://api.anthropic.com    # IPv4 강제
$ curl -6 https://api.anthropic.com    # IPv6 강제

# 해결 1: 프록시 설정
$ export HTTPS_PROXY=http://proxy.company.com:8080
$ export NO_PROXY=localhost,127.0.0.1,.internal

# 해결 2: 사내 CA 추가
$ export NODE_EXTRA_CA_CERTS=/etc/ssl/company-ca.pem

# 해결 3: IPv4 강제
$ export NODE_OPTIONS="--dns-result-order=ipv4first"

# 해결 4: timeout 늘림
$ export NODE_TIMEOUT_MS=60000

# 종합 디버그
$ CLAUDE_CODE_LOG_LEVEL=debug claude doctor 2>&1 \
    | grep -iE 'proxy|cert|timeout|dns'
```

## Speaker Notes

네트워크 문제 진단입니다.
connect ETIMEDOUT이나 unable to verify certificate가 일반적 에러입니다.
진단 1은 기본 네트워크 도달성입니다.
curl -v로 api.anthropic.com에 직접 접속해 봅니다.
빠른 응답이면 네트워크는 정상이고 Timeout이면 프록시 문제가 의심됩니다.
진단 2는 프록시 환경변수 확인입니다.
HTTPS_PROXY 설정과 형식을 점검합니다.
진단 3은 사내 CA 인식입니다.
openssl s_client로 직접 TLS 핸드셰이크를 테스트합니다.
Verify return code 0이면 CA가 정상 인식되는 것입니다.
진단 4는 DNS 확인입니다.
nslookup이나 dig로 도메인 해석이 정상인지 확인합니다.
진단 5는 IPv6 문제로 드물지만 발생합니다.
curl -4와 -6으로 어느 쪽이 실패하는지 확인합니다.
해결 패턴은 4가지입니다.
프록시 설정, 사내 CA 추가, IPv4 강제, timeout 늘림입니다.
종합 디버그는 LOG_LEVEL debug로 doctor를 실행하고 proxy, cert, timeout, dns 키워드로 grep합니다.
