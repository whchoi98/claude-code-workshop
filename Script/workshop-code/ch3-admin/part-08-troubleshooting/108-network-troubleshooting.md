# Slide 108: Network troubleshooting

**Part 8: TROUBLESHOOTING**

## Code Blocks

### net-debug.sh

```bash
# 종합 진단 스크립트
#!/bin/bash
echo "=== Network diagnosis ==="

# 1. doctor
claude doctor 2>&1 | grep -A 5 'Network'

# 2. 도메인별 연결 테스트
for d in api.anthropic.com bedrock-runtime.ap-northeast-2.amazonaws.com; do
  echo "Testing $d ..."
  curl -sS -o /dev/null -w "  Status: %{http_code}, Time: %{time_total}s\n" \
    --connect-timeout 5 \
    "https://$d/" || echo "  FAIL"
done

# 3. 인증서 검증
openssl s_client -connect api.anthropic.com:443 \
  -CAfile ${NODE_EXTRA_CA_CERTS} </dev/null 2>&1 | \
  grep 'Verify return code'

# 4. DNS
dig +short api.anthropic.com
dig +short bedrock-runtime.ap-northeast-2.amazonaws.com

# 5. 프록시 환경변수
env | grep -i proxy
```

## Speaker Notes

네트워크 트러블슈팅의 진단 흐름입니다.
5단계로 차근차근 진행합니다.
doctor로 증상을 확인하고 curl로 도메인을 직접 테스트하며 프록시와 인증서, DNS 해석, 방화벽 로그를 점검합니다.
종합 진단 스크립트를 봅니다.
1단계 claude doctor의 Network 섹션을 추출합니다.
2단계 도메인별 연결 테스트를 합니다.
api.anthropic.com과 bedrock-runtime을 차례로 테스트합니다.
status 코드와 응답 시간을 출력합니다.
3단계 인증서 검증입니다.
openssl s_client로 NODE_EXTRA_CA_CERTS를 사용한 검증을 수행합니다.
Verify return code가 0이어야 정상입니다.
4단계 DNS 해석을 dig로 확인합니다.
IP 응답이 사설인지 공인인지로 사내 DNS 분기 동작을 확인할 수 있습니다.
5단계 프록시 환경변수를 점검합니다.
이 스크립트를 사내 표준으로 배포하면 사용자가 직접 1차 진단을 할 수 있습니다.
