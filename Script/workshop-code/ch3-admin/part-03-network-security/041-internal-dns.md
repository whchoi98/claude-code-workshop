# Slide 41: Internal DNS

**Part 3: NETWORK & SECURITY**

## Code Blocks

### Split DNS

```bash
# 시나리오: 외부 도메인은 인터넷, 내부 도메인은 사설망

# 1. /etc/hosts 또는 사내 DNS 서버 설정
api.anthropic.com         52.x.x.x   # 외부 직접
bedrock-runtime.ap-...    10.0.x.x   # VPC Endpoint 사설 IP
mcp.internal.company.com  10.1.x.x   # 사내 MCP 서버
github.enterprise.com     10.2.x.x   # GitHub Enterprise

# 2. Split DNS (사내 DNS 서버)
# 외부 조회: api.anthropic.com → 인터넷 라우팅
# 내부 조회: *.internal.company.com → 사내 IP
# Bedrock VPC EP 활성화 시 자동 분기

# 3. Route 53 Resolver (AWS 환경)
# Outbound endpoint으로 사내 DNS와 양방향 연동

# 4. 효과
- Bedrock 호출이 사설 경로로
- 사내 MCP 서버에 직접 접근
- 외부 API는 정상 라우팅
- 사용자 별도 설정 불필요

# 5. 디버깅
$ dig bedrock-runtime.ap-northeast-2.amazonaws.com
# 사내에서 10.x.x.x 응답이 나오면 정상
```

## Speaker Notes

사내 DNS 분기 설정입니다.
외부 도메인은 인터넷으로, 내부 도메인은 사설망으로 분리해 라우팅하는 패턴입니다.
1단계 /etc/hosts나 사내 DNS 서버에서 도메인별 IP를 설정합니다.
api.anthropic.com은 외부 직접 IP로, bedrock-runtime은 VPC Endpoint 사설 IP로, 사내 MCP 서버는 사내 IP로 분기합니다.
2단계 Split DNS를 사내 DNS 서버에 구성합니다.
외부 조회는 인터넷 라우팅, 내부 조회는 사내 IP로 분기됩니다.
Bedrock VPC Endpoint 활성화 시 자동으로 분기됩니다.
3단계 AWS 환경은 Route 53 Resolver를 사용할 수 있습니다.
Outbound endpoint로 사내 DNS와 양방향 연동합니다.
4단계 효과는 Bedrock 호출이 사설 경로로 가고, 사내 MCP 서버에 직접 접근하며, 외부 API는 정상 라우팅되고, 사용자 별도 설정이 불필요한 것입니다.
5단계 디버깅은 dig 명령으로 도메인 해석 결과를 확인합니다.
사내에서 10.x로 시작하는 사설 IP가 응답되면 정상 분기되는 것입니다.
