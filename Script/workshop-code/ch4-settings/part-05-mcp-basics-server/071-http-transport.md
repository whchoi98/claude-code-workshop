# Slide 71: HTTP transport

**Part 5: MCP 기본과 공식 서버**

## Code Blocks

### http

```bash
# settings.json
{
  "mcpServers": {
    "internal-mcp": {
      "type": "http",
      "url": "https://mcp.company.com/v1/mcp",
      "headers": {
        "Authorization": "Bearer ${MCP_TOKEN}",
        "X-Tenant-ID": "team-backend"
      },
      "timeout": 30000
    }
  }
}

# 동작 흐름
1. Claude Code가 HTTP POST 요청
2. body는 JSON-RPC 메시지
3. 서버가 HTTP 응답으로 결과 반환
4. 다음 호출은 새 HTTP 요청

# 장점
- 중앙 집중식 운영 (한 서버, 여러 사용자)
- 사내 인증 시스템과 통합 (Bearer, OAuth)
- 모니터링과 로깅 용이
- 업데이트 시 한 번에 전체 적용

# 단점
- 네트워크 지연 (수십 ms)
- 인증 토큰 관리 필요
- 인프라 운영 부담
```

## Speaker Notes

HTTP 통신 방식을 자세히 살펴봅니다.
settings.json 예시입니다.
type을 http로 명시합니다.
url에 원격 서버의 엔드포인트를 적습니다.
headers에 Authorization Bearer 토큰과 X-Tenant-ID 같은 사용자 정의 헤더를 추가할 수 있습니다.
timeout으로 응답 제한 시간을 명시합니다.
동작 흐름을 봅니다.
Claude Code가 HTTP POST 요청을 보냅니다.
body는 JSON-RPC 메시지 형식입니다.
서버가 HTTP 응답으로 결과를 반환합니다.
다음 호출은 새 HTTP 요청으로 진행됩니다.
장점은 중앙 집중식 운영입니다.
한 서버로 여러 사용자를 처리할 수 있고 사내 인증 시스템과 통합이 쉽습니다.
모니터링과 로깅이 용이하며 업데이트 시 한 번에 전체 적용됩니다.
단점은 네트워크 지연이 수십 ms 발생한다는 것입니다.
인증 토큰 관리가 필요하고 인프라 운영 부담이 있습니다.
