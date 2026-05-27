# Slide 84: MCP 도구 흐름

**Part 5: MCP SDK 통합**

## Code Blocks

### flow

```bash
# 흐름 비교
# 방식 A: 직접 도구 (Part 3)
# 우리 서버 -> tools 정의 -> Claude 호출
#           -> tool_use 받음 -> 도구 실행 (우리 코드)
#           -> tool_result 보냄 -> 최종 응답

# 방식 B: MCP via SDK (이번 Part)
# 우리 서버 -> mcp_servers 명시 -> Claude 호출
#           -> Anthropic 인프라가 MCP 서버와 통신
#           -> Claude가 도구 호출/결과 자동 처리
#           -> 최종 응답을 우리 서버에 반환
# 우리는 그냥 호출하고 응답을 받기만 함
```

## Speaker Notes

MCP 도구 흐름의 내부 처리 과정입니다.
5단계로 진행됩니다.
SDK 호출 시 mcp_servers를 명시합니다.
Anthropic 인프라가 MCP 서버를 호출해 도구 목록을 조회합니다.
Claude가 필요한 도구를 호출하고 결과를 처리합니다.
최종 응답을 사용자에게 반환합니다.
중요한 점이 있습니다.
mcp_servers를 사용하면 MCP 서버 호출은 Anthropic 인프라가 처리합니다.
본인 서버에서 MCP 클라이언트 코드를 작성할 필요가 없습니다.
흐름 비교를 봅니다.
방식 A 직접 도구는 우리 서버에서 tools 정의, Claude 호출, tool_use 받음, 도구 실행, tool_result 보냄, 최종 응답까지 모두 직접 관리합니다.
방식 B MCP via SDK는 우리 서버가 mcp_servers를 명시하고 Claude를 호출하면 Anthropic 인프라가 MCP 서버와 통신을 모두 처리하고 최종 응답만 우리 서버에 반환합니다.
우리는 그냥 호출하고 응답을 받기만 합니다.
매우 간단합니다.
