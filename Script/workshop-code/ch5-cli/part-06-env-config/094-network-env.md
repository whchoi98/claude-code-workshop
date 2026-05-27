# Slide 94: 네트워크 환경변수

**Part 6: 환경변수와 설정**

## Code Blocks

### network env

```bash
# 1. HTTP/HTTPS Proxy
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080

# 인증이 필요한 프록시
export HTTPS_PROXY=http://user:pass@proxy.company.com:8080
# 또는 URL 인코딩
export HTTPS_PROXY=http://user:%40pass@proxy.company.com:8080

# 2. NO_PROXY (프록시 우회 도메인)
export NO_PROXY=localhost,127.0.0.1,.company.com,.internal

# 3. 사내 CA 인증서 (Self-signed 또는 사내 CA)
# 옵션 A: 단일 인증서
export NODE_EXTRA_CA_CERTS=/etc/ssl/certs/company-ca.pem

# 옵션 B: 여러 인증서 (PEM bundle)
export NODE_EXTRA_CA_CERTS=/etc/ssl/certs/ca-bundle.pem

# 4. TLS 검증 비활성화 (개발 환경만)
export NODE_TLS_REJECT_UNAUTHORIZED=0
# 프로덕션에서는 절대 금지

# 5. DNS 캐시
export NODE_DNS_CACHE_TIME=300    # 5분 캐싱

# 6. 연결 timeout
export NODE_TIMEOUT_MS=30000      # 30초

# 7. IPv4 강제 (IPv6 문제 시)
export NODE_OPTIONS="--dns-result-order=ipv4first"

# 8. 디버깅 (자세한 네트워크 로그)
export DEBUG="claude:*,axios"
$ claude doctor 2>&1 | grep -i proxy

# 9. 트러블슈팅 체크리스트
# - curl -v https://api.anthropic.com 으로 직접 테스트
# - proxy 환경변수가 정확히 export됐는지 확인
# - 사내 CA가 제대로 로드되는지 doctor로 확인
# - NO_PROXY에 api 도메인이 잘못 포함되지 않았는지
```

## Speaker Notes

네트워크 환경변수는 사내망 통합에 핵심입니다.
1번 HTTP_PROXY와 HTTPS_PROXY로 프록시 서버를 명시합니다.
인증이 필요한 프록시는 user:pass 형식으로 URL에 포함시킵니다.
특수 문자는 URL 인코딩이 필요합니다.
2번 NO_PROXY는 프록시를 우회할 도메인입니다.
localhost, 사내 도메인, .internal 같은 내부 호스트를 명시합니다.
3번 사내 CA 인증서를 NODE_EXTRA_CA_CERTS로 추가합니다.
Self-signed 인증서나 사내 CA를 사용하는 경우 필수입니다.
여러 인증서를 PEM bundle로 합친 파일도 지원합니다.
4번 TLS 검증 비활성화는 개발 환경만 사용합니다.
NODE_TLS_REJECT_UNAUTHORIZED를 0으로 두면 위험하므로 프로덕션에서는 절대 금지입니다.
5번 DNS 캐시로 NODE_DNS_CACHE_TIME을 5분 정도로 설정해 성능을 개선할 수 있습니다.
6번 NODE_TIMEOUT_MS로 연결 timeout을 조정합니다.
7번 IPv6 문제 발생 시 IPv4 강제도 가능합니다.
8번 DEBUG 환경변수로 자세한 네트워크 로그를 볼 수 있습니다.
9번 트러블슈팅 체크리스트로 4가지를 단계별로 확인합니다.
