# Slide 92: MCP + Streaming

**Part 5: MCP SDK 통합**

## Code Blocks

### MCP + stream

```python
# MCP를 사용하면서 진행 상황을 실시간 표시

# Note: 현재 client.beta.messages.stream에서 mcp_servers 직접 지원이 제한적
# 일반 호출 + WebSocket으로 진행 상황 표시 패턴 권장

import anthropic
import asyncio

client = anthropic.AsyncAnthropic()

async def mcp_with_progress(prompt: str, websocket):
    """MCP 호출 진행 상황을 WebSocket으로 전송"""
    await websocket.send_json({"type": "start"})

    # 1. MCP 호출 (await으로 응답 대기)
    response = await client.beta.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2048,
        mcp_servers=[{
            "type": "url",
            "url": "https://mcp.github.com/mcp",
            "name": "github",
            "authorization_token": GH_TOKEN,
        }],
        messages=[{"role": "user", "content": prompt}],
        betas=["mcp-client-2025-04-04"],
    )

    # 2. 응답을 분석하면서 사용자에게 진행 상황 표시
    for block in response.content:
        if block.type == "text":
            # 텍스트 청크 단위로 전송
            for i in range(0, len(block.text), 50):
                chunk = block.text[i:i+50]
                await websocket.send_json({
                    "type": "text",
                    "text": chunk,
                })
                await asyncio.sleep(0.02)   # 타이핑 효과

        elif block.type == "mcp_tool_use":
            # 도구 호출 정보 표시
            await websocket.send_json({
                "type": "mcp_tool",
                "server": block.server_name,
                "name": block.name,
                "input": block.input,
            })

        elif block.type == "mcp_tool_result":
            # 도구 결과 표시 (truncated)
            content_text = ""
            if isinstance(block.content, list):
                content_text = "".join(
                    c.text for c in block.content if hasattr(c, "text")
                )
            await websocket.send_json({
                "type": "mcp_result",
                "tool_use_id": block.tool_use_id,
                "preview": content_text[:200],
                "is_error": getattr(block, "is_error", False),
            })

    await websocket.send_json({
        "type": "done",
        "usage": response.usage.model_dump(),
    })

# 클라이언트 측 UI
# - "🔍 GitHub에서 PR 조회 중..."
# - "📊 변경 파일 확인 중..."
# - 점진적 텍스트 출력
# - 완료 시 토큰 사용량 표시
```

## Speaker Notes

MCP와 Streaming을 결합하는 패턴입니다.
현재 client.beta.messages.stream에서 mcp_servers의 직접 지원은 제한적입니다.
일반 호출과 WebSocket을 결합한 패턴이 권장됩니다.
mcp_with_progress 함수에서 진행 상황을 WebSocket으로 전송합니다.
start 이벤트로 시작을 알리고 MCP 호출을 await으로 대기합니다.
응답을 받은 후 각 블록을 순회하면서 사용자에게 진행 상황을 표시합니다.
text 블록은 50자씩 청크로 분할해 전송합니다.
0.02초 sleep으로 타이핑 효과를 만들어 자연스러운 UX를 만듭니다.
mcp_tool_use 블록은 어떤 도구가 호출됐는지 즉시 표시합니다.
사용자는 GitHub의 어떤 도구가 호출됐는지 알 수 있습니다.
mcp_tool_result는 결과를 200자 미리보기로 보여줍니다.
is_error도 함께 전송해 에러를 시각화할 수 있게 합니다.
final은 done 이벤트와 함께 토큰 사용량을 전송합니다.
클라이언트 UI에서 GitHub에서 PR 조회 중, 변경 파일 확인 중 같은 진행 메시지를 표시합니다.
점진적 텍스트 출력과 완료 시 토큰 사용량을 보여주면 일반 스트리밍과 거의 동일한 UX가 가능합니다.
