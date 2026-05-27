# Slide 88: MCP 서버 디버깅

**Part 5: MCP SDK 통합**

## Code Blocks

### debugging

```python
# 1. MCP 서버 응답 확인
import requests

def debug_mcp_server(url, token):
    print(f"=== Debugging {url} ===")

    # 1. Health check
    try:
        r = requests.get(url, timeout=5)
        print(f"GET / : {r.status_code}")
    except Exception as e:
        print(f"GET / failed: {e}")
        return

    # 2. Tools list
    try:
        r = requests.post(
            url,
            headers={"Authorization": f"Bearer {token}"},
            json={"jsonrpc": "2.0", "method": "tools/list", "id": 1},
            timeout=10,
        )
        if r.status_code == 200:
            tools = r.json()["result"]["tools"]
            print(f"Tools ({len(tools)}):")
            for t in tools[:5]:
                print(f"  - {t['name']}: {t.get('description', '')[:50]}")
        else:
            print(f"tools/list failed: {r.status_code} {r.text[:200]}")
    except Exception as e:
        print(f"tools/list error: {e}")

# 2. SDK 호출 디버깅
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("anthropic")

# DEBUG 레벨로 모든 HTTP 요청/응답 로그

# 3. MCP 응답 분석
def inspect_mcp_response(response):
    blocks_by_type = {}
    mcp_calls = []

    for block in response.content:
        blocks_by_type[block.type] = blocks_by_type.get(block.type, 0) + 1

        if block.type == "mcp_tool_use":
            mcp_calls.append({
                "server": block.server_name,
                "tool": block.name,
                "input": block.input,
            })
        elif block.type == "mcp_tool_result":
            mcp_calls[-1]["result"] = block.content
            mcp_calls[-1]["is_error"] = getattr(block, "is_error", False)

    return {
        "blocks": blocks_by_type,
        "stop_reason": response.stop_reason,
        "usage": response.usage.model_dump(),
        "mcp_calls": mcp_calls,
    }

# 4. 일반 에러
# - 401 Unauthorized: token 확인
# - 404 Not Found: URL 확인
# - 500/502: MCP 서버 자체 문제
# - Timeout: 서버 응답 느림, 또는 도구 실행 오래 걸림

# 5. tools/list가 캐시되는 경우
# 서버를 재배포해도 SDK는 기존 도구 목록을 보유
# 새 세션 또는 5분 대기 후 재시도
```

## Speaker Notes

MCP 서버 디버깅을 위한 도구입니다.
1번 MCP 서버 응답을 직접 확인합니다.
debug_mcp_server 함수에서 GET으로 health check 후 tools/list POST 호출로 도구 목록을 확인합니다.
응답이 정상이면 tools 배열을 출력합니다.
실패 시 status code와 응답 body를 표시해 원인을 추적합니다.
2번 SDK 호출 디버깅은 logging 모듈로 합니다.
anthropic logger를 DEBUG 레벨로 설정하면 모든 HTTP 요청과 응답이 로그됩니다.
어떤 데이터가 오가는지 정확히 확인할 수 있습니다.
3번 MCP 응답 분석은 inspect_mcp_response 함수로 합니다.
블록 타입별 카운트, stop_reason, usage, MCP 호출 목록을 정리합니다.
mcp_tool_use와 mcp_tool_result를 매칭해 입력과 결과, 에러 여부를 추적합니다.
4번 일반 에러를 정리합니다.
401은 token 확인, 404는 URL 확인, 500이나 502는 MCP 서버 자체 문제, Timeout은 서버 응답이 느리거나 도구 실행이 오래 걸리는 경우입니다.
5번 tools/list 캐시 주의가 필요합니다.
서버를 재배포해도 SDK는 기존 도구 목록을 보유할 수 있습니다.
새 세션을 만들거나 5분 대기 후 재시도합니다.
