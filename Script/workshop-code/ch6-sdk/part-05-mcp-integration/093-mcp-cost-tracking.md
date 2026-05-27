# Slide 93: MCP 비용 추적

**Part 5: MCP SDK 통합**

## Code Blocks

### MCP cost

```python
# MCP 도구 호출의 토큰도 비용에 포함됨

# 1. MCP 호출 비용 계산
def calculate_mcp_cost(response, model="claude-sonnet-4-5"):
    u = response.usage
    rates = {
        "sonnet": (3.0, 15.0),     # input, output ($/1M)
        "haiku":  (1.0, 5.0),
        "opus":   (15.0, 75.0),
    }
    rate = next((r for k, r in rates.items() if k in model), rates["sonnet"])

    total_cost = (
        u.input_tokens * rate[0]
        + u.output_tokens * rate[1]
        + u.cache_creation_input_tokens * rate[0] * 1.25
        + u.cache_read_input_tokens * rate[0] * 0.1
    ) / 1e6

    return {
        "total_usd": total_cost,
        "input_tokens": u.input_tokens,
        "output_tokens": u.output_tokens,
    }

# 2. MCP 도구별 토큰 사용량 추적
def track_mcp_tools(response):
    tools_stats = {}

    for block in response.content:
        if block.type == "mcp_tool_use":
            key = f"{block.server_name}.{block.name}"
            tools_stats.setdefault(key, {"count": 0, "tokens": 0})
            tools_stats[key]["count"] += 1

        elif block.type == "mcp_tool_result":
            # 이전 mcp_tool_use 블록의 결과
            # tool_use_id로 매칭해서 토큰 추정
            for content_block in block.content:
                if hasattr(content_block, "text"):
                    # 결과 텍스트 길이로 토큰 추정
                    approx_tokens = len(content_block.text) // 4
                    # 마지막 도구 사용에 추가
                    last_tool = list(tools_stats.keys())[-1]
                    tools_stats[last_tool]["tokens"] += approx_tokens

    return tools_stats

# 3. 일일 MCP 비용 모니터링
import json
from datetime import datetime

def log_mcp_call(response, user_id):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        "model": response.model,
        "mcp_tools_used": [
            {"server": b.server_name, "name": b.name}
            for b in response.content if b.type == "mcp_tool_use"
        ],
        "cost": calculate_mcp_cost(response, response.model),
        "stop_reason": response.stop_reason,
    }

    # 로그 시스템에 전송
    print(json.dumps(log_entry))

    # DB나 메트릭 시스템에도 전송
    # cloudwatch.put_metric_data(...)
```

## Speaker Notes

MCP 비용 추적은 운영에 필수입니다.
MCP 도구 호출의 입력과 결과 토큰이 모두 비용에 포함됩니다.
1번 MCP 호출 비용 계산은 calculate_mcp_cost 함수로 합니다.
모델별 단가에 input, output, cache 토큰을 곱해 합산합니다.
total_usd와 토큰 수를 반환합니다.
2번 MCP 도구별 토큰 사용량 추적입니다.
track_mcp_tools 함수에서 server.name 키로 도구별 통계를 누적합니다.
mcp_tool_use 블록에서 카운트를 증가시키고 mcp_tool_result에서 결과 텍스트 길이로 토큰을 추정합니다.
정확한 토큰 수는 응답의 usage에서 종합 확인합니다.
3번 일일 MCP 비용 모니터링은 log_mcp_call 함수로 합니다.
timestamp, user_id, model, 사용된 MCP 도구, 비용, stop_reason을 JSON으로 기록합니다.
stdout 로그뿐 아니라 DB와 CloudWatch 같은 메트릭 시스템에도 전송합니다.
도구별, 사용자별, 일별 비용 분포를 분석해 비용 폭증을 즉시 감지할 수 있습니다.
무거운 MCP 도구를 찾아 최적화하거나 사용량 제한을 적용하는 데이터 기반이 됩니다.
