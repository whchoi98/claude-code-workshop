# Slide 86: 사내 MCP 서버 연결

**Part 5: MCP SDK 통합**

## Code Blocks

### internal MCP

```python
# 사내에 배포한 MCP 서버를 SDK에서 활용

# 1. 사내 MCP 서버 URL
SDK_MCP = {
    "type": "url",
    "url": "https://mcp.company.internal/api",
    "name": "company-tools",
    "authorization_token": os.getenv("COMPANY_MCP_TOKEN"),
}

# 2. VPC private endpoint
PRIVATE_MCP = {
    "type": "url",
    "url": "https://internal-mcp-elb.us-east-1.amazonaws.com",
    "name": "internal",
    "authorization_token": os.getenv("INTERNAL_TOKEN"),
}

# 3. 사내 헤더 추가
{
    "type": "url",
    "url": "https://mcp.company.com",
    "name": "company",
    "authorization_token": "Bearer abc123",
    # 추가 헤더는 보통 token으로 충분
}

# 4. 사내 MCP 서버 동작 확인
import requests

def health_check_mcp(url, token):
    r = requests.post(
        url,
        headers={"Authorization": f"Bearer {token}"},
        json={"jsonrpc": "2.0", "method": "tools/list", "id": 1},
        timeout=5,
    )
    return r.status_code == 200 and "result" in r.json()

# 사전 확인
if not health_check_mcp(SDK_MCP["url"], SDK_MCP["authorization_token"]):
    raise Exception("MCP server not reachable")

# 5. 도구 목록 미리 보기
def list_mcp_tools(url, token):
    r = requests.post(
        url,
        headers={"Authorization": f"Bearer {token}"},
        json={"jsonrpc": "2.0", "method": "tools/list", "id": 1},
    )
    return [t["name"] for t in r.json()["result"]["tools"]]

# 6. 환경별 MCP 서버 분리
MCP_CONFIG = {
    "dev":     "https://mcp-dev.company.com",
    "staging": "https://mcp-staging.company.com",
    "prod":    "https://mcp.company.com",
}

env = os.getenv("ENV", "dev")
company_mcp = {
    "type": "url",
    "url": MCP_CONFIG[env],
    "name": f"company-{env}",
    "authorization_token": os.getenv(f"MCP_TOKEN_{env.upper()}"),
}

# 사용
response = client.beta.messages.create(
    mcp_servers=[company_mcp],
    messages=[{"role": "user", "content": "..."}],
    betas=["mcp-client-2025-04-04"],
)
```

## Speaker Notes

사내 MCP 서버 연결입니다.
Day 2에서 MCP 서버를 만드는 법을 배웠고 이제 SDK에서 활용합니다.
1번 사내 MCP 서버 URL을 SDK_MCP dict로 정의합니다.
type, url, name, authorization_token을 명시합니다.
2번 VPC private endpoint도 동일한 패턴입니다.
AWS ELB 같은 내부 endpoint를 url로 명시합니다.
3번 사내 헤더 추가가 필요한 경우는 보통 authorization_token으로 충분합니다.
4번 사내 MCP 서버 동작 확인을 사전에 합니다.
health_check_mcp 함수로 tools/list 메서드를 호출해 응답이 정상인지 확인합니다.
200 응답이고 result 필드가 있으면 정상입니다.
5번 도구 목록 미리 보기로 어떤 도구가 제공되는지 확인할 수 있습니다.
list_mcp_tools 함수에서 응답의 tools 배열에서 name만 추출합니다.
6번 환경별 MCP 서버 분리가 중요합니다.
dev, staging, prod 각각 다른 URL과 token을 사용합니다.
환경변수로 ENV를 받아 적절한 설정을 동적으로 선택합니다.
MCP_TOKEN_DEV, MCP_TOKEN_STAGING, MCP_TOKEN_PROD 같은 환경변수로 token도 분리합니다.
프로덕션 사고가 staging에 번지지 않게 합니다.
