# Slide 47: Network troubleshooting

**Part 3: NETWORK & SECURITY**

## Code Blocks

### Diagnostics

```bash
# 1. claude doctor로 1차 진단
$ claude doctor
# Network 섹션의 OK/FAIL 항목 확인

# 2. 기본 연결 테스트
$ curl -v https://api.anthropic.com/v1/health
# TLS handshake와 응답 확인

# 3. 프록시 통과 테스트
$ curl -v --proxy $HTTPS_PROXY https://api.anthropic.com

# 4. 인증서 검증
$ openssl s_client -connect api.anthropic.com:443 \
    -CAfile $NODE_EXTRA_CA_CERTS
# Verify return code: 0 (ok) 확인

# 5. DNS 확인
$ dig api.anthropic.com
$ dig bedrock-runtime.ap-northeast-2.amazonaws.com

# 6. 방화벽 (개발자 PC에서)
# Windows: New-NetFirewallRule (관리자)
# macOS: pf rule 확인
# Linux: iptables -L
```

## Speaker Notes

네트워크 연결 실패 시 진단 순서입니다.
5단계로 차근차근 점검합니다.
1단계 claude doctor를 실행해 Network 섹션의 OK FAIL 항목을 확인합니다.
2단계 curl로 기본 연결을 테스트합니다.
verbose 옵션으로 TLS handshake와 응답을 확인합니다.
3단계 프록시 통과를 테스트합니다.
curl에 --proxy 옵션으로 명시해 프록시 경로를 검증합니다.
4단계 인증서 검증입니다.
openssl s_client로 TLS 연결을 시뮬레이션하고 -CAfile로 사내 CA를 명시합니다.
Verify return code가 0 ok로 나오면 정상입니다.
5단계 DNS를 확인합니다.
dig 명령으로 도메인 해석 결과를 봅니다.
사내 DNS 분기가 제대로 동작하는지 점검합니다.
6단계 개발자 PC의 방화벽을 점검합니다.
Windows는 New-NetFirewallRule, macOS는 pf rule, Linux는 iptables를 확인합니다.
이 순서대로 점검하면 대부분의 네트워크 문제를 식별할 수 있습니다.
