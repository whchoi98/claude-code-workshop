# Slide 67: 스트림 중단

**Part 4: STREAMING**

## Code Blocks

### cancellation

```python
# 1. AbortController로 중단 (TS)
function ChatWithCancel() {
  const [abortController, setAbortController] = useState<AbortController | null>(null);

  async function send(prompt: string) {
    const controller = new AbortController();
    setAbortController(controller);

    try {
      const response = await fetch("/chat/stream", {
        method: "POST",
        body: JSON.stringify({ prompt }),
        signal: controller.signal,    // ← 중요
      });

      const reader = response.body!.getReader();
      // ... 스트림 처리 ...
    } catch (e) {
      if ((e as Error).name === "AbortError") {
        console.log("사용자 중단");
      }
    }
  }

  function cancel() {
    abortController?.abort();
  }

  return (
    <>
      <button onClick={cancel}>중단</button>
    </>
  );
}

# 2. Python 서버에서 disconnect 감지
from fastapi import Request

@app.post("/chat/stream")
async def chat_stream(req: ChatRequest, request: Request):
    async def gen():
        async with client.messages.stream(...) as stream:
            async for event in stream:
                # 클라이언트 연결 확인
                if await request.is_disconnected():
                    print("Client disconnected, stopping stream")
                    break

                # ... 이벤트 처리 ...
                yield ...

    return StreamingResponse(gen(), media_type="text/event-stream")

# 3. 타임아웃 적용
import asyncio

async def streamed_with_timeout(timeout_s=30):
    try:
        async with asyncio.timeout(timeout_s):
            async with client.messages.stream(...) as stream:
                async for event in stream:
                    yield event
    except asyncio.TimeoutError:
        yield {"type": "error", "message": "Timeout"}

# 4. 토큰 한도 도달 시 자동 중단
# max_tokens 도달 -> message_delta event.delta.stop_reason == "max_tokens"
# 처리:
if event.type == "message_delta":
    if event.delta.stop_reason == "max_tokens":
        # 잘림 알림
        send_to_client({"type": "warning", "message": "응답 잘림"})
```

## Speaker Notes

스트림 중단은 사용자 경험에 중요합니다.
1번 AbortController로 TypeScript에서 중단합니다.
fetch의 signal 옵션에 controller.signal을 전달합니다.
cancel 함수에서 controller.abort를 호출하면 fetch가 즉시 중단됩니다.
AbortError를 catch해 사용자 중단을 구분합니다.
2번 Python 서버에서 disconnect를 감지합니다.
Request 객체의 is_disconnected를 async로 호출해 클라이언트 연결 상태를 확인합니다.
연결이 끊어졌으면 break로 스트림을 중단해 불필요한 토큰 비용을 방지합니다.
3번 타임아웃 적용은 asyncio.timeout 사용합니다.
async context manager로 감싸면 시간 초과 시 자동으로 TimeoutError가 발생합니다.
에러 처리로 사용자에게 timeout 메시지를 보냅니다.
4번 토큰 한도 도달 시 자동 중단도 처리해야 합니다.
message_delta 이벤트의 stop_reason이 max_tokens면 응답이 잘렸음을 의미합니다.
사용자에게 응답이 잘렸다는 경고를 표시하고 더 큰 max_tokens로 재시도 옵션을 제공할 수 있습니다.
모든 중단 케이스를 처리하면 견고한 스트리밍 시스템이 완성됩니다.
