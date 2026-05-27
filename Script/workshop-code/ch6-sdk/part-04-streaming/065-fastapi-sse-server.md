# Slide 65: FastAPI SSE 서버

**Part 4: STREAMING**

## Code Blocks

### FastAPI SSE

```python
# server.py - FastAPI로 SSE 스트림 서버
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import anthropic
import json

app = FastAPI()
client = anthropic.AsyncAnthropic()

class ChatRequest(BaseModel):
    prompt: str
    model: str = "claude-sonnet-4-5"
    max_tokens: int = 1024

@app.post("/chat/stream")
async def chat_stream(req: ChatRequest):
    async def event_generator():
        async with client.messages.stream(
            model=req.model,
            max_tokens=req.max_tokens,
            messages=[{"role": "user", "content": req.prompt}],
        ) as stream:
            async for event in stream:
                if event.type == "content_block_delta":
                    if event.delta.type == "text_delta":
                        data = json.dumps({
                            "type": "text",
                            "text": event.delta.text,
                        })
                        yield f"data: {data}\n\n"

                elif event.type == "message_stop":
                    final = await stream.get_final_message()
                    data = json.dumps({
                        "type": "done",
                        "usage": {
                            "input": final.usage.input_tokens,
                            "output": final.usage.output_tokens,
                        },
                    })
                    yield f"data: {data}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",  # nginx 버퍼링 비활성화
        },
    )

# 실행
# $ uvicorn server:app --reload
```

## Speaker Notes

FastAPI로 SSE 스트림 서버를 만듭니다.
async 환경이므로 AsyncAnthropic을 사용합니다.
ChatRequest pydantic 모델로 요청 검증을 자동화합니다.
chat_stream endpoint에서 event_generator async function을 정의합니다.
async with client.messages.stream으로 스트림을 시작합니다.
async for로 이벤트를 순회하며 SSE 형식으로 전송합니다.
content_block_delta의 text_delta를 JSON으로 직렬화해 data: 형식으로 yield합니다.
각 메시지는 빈 줄 두 개로 구분되는 SSE 표준입니다.
message_stop 이벤트에서 최종 토큰 사용량을 done 이벤트로 전송합니다.
StreamingResponse로 event_generator를 감싸 반환합니다.
media_type은 text event-stream으로 SSE를 명시합니다.
Cache-Control no-cache와 X-Accel-Buffering no를 헤더에 추가합니다.
nginx 같은 프록시의 버퍼링을 비활성화해 실시간성을 보장합니다.
uvicorn으로 서버를 실행하면 즉시 SSE 기반 채팅 API가 작동합니다.
