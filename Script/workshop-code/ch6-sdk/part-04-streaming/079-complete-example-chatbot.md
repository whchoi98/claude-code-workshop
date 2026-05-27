# Slide 79: 완성 예시 / 스트리밍 챗봇

**Part 4: STREAMING**

## Code Blocks

### complete example

```python
# server.py - 완성된 스트리밍 챗봇
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import anthropic
import json

app = FastAPI()
client = anthropic.AsyncAnthropic()

# 세션별 대화 보관
sessions = {}

@app.websocket("/chat/{session_id}")
async def chat(ws: WebSocket, session_id: str):
    await ws.accept()

    # 세션 초기화 또는 복원
    if session_id not in sessions:
        sessions[session_id] = {
            "messages": [],
            "system": "당신은 친절한 한국어 도우미입니다.",
        }
    session = sessions[session_id]

    try:
        while True:
            data = await ws.receive_json()
            user_input = data["prompt"]

            session["messages"].append({
                "role": "user", "content": user_input,
            })

            # 응답 스트리밍
            full_response = ""
            await ws.send_json({"type": "start"})

            try:
                async with client.messages.stream(
                    model="claude-sonnet-4-5",
                    max_tokens=2048,
                    system=[{
                        "type": "text",
                        "text": session["system"],
                        "cache_control": {"type": "ephemeral"},
                    }],
                    messages=session["messages"],
                ) as stream:
                    async for text in stream.text_stream:
                        full_response += text
                        await ws.send_json({
                            "type": "delta",
                            "text": text,
                        })

                    final = await stream.get_final_message()
                    session["messages"].append({
                        "role": "assistant",
                        "content": full_response,
                    })

                    await ws.send_json({
                        "type": "done",
                        "usage": {
                            "in": final.usage.input_tokens,
                            "out": final.usage.output_tokens,
                            "cache_read": final.usage.cache_read_input_tokens,
                        },
                    })

            except anthropic.APIError as e:
                await ws.send_json({"type": "error", "message": str(e)})

    except WebSocketDisconnect:
        print(f"Session {session_id} disconnected")

# 실행: uvicorn server:app --reload
```

## Speaker Notes

완성 예시는 풀스택 스트리밍 챗봇 서버입니다.
FastAPI WebSocket으로 양방향 통신을 구현합니다.
sessions dict로 세션 ID별 대화를 메모리에 보관합니다.
실무에서는 Redis 같은 외부 저장소를 사용해야 합니다.
chat endpoint에서 session_id를 path parameter로 받습니다.
ws.accept 후 세션 초기화 또는 복원을 합니다.
새 세션은 빈 messages와 기본 system prompt로 시작합니다.
while 루프에서 클라이언트 메시지를 받고 user 메시지를 messages에 추가합니다.
type start로 응답 시작을 알린 후 스트림을 시작합니다.
system에 cache_control을 명시해 prompt caching을 활용합니다.
같은 세션의 후속 호출에서 system이 캐시됩니다.
async for로 text_stream을 순회하며 delta 이벤트를 클라이언트에 전송합니다.
full_response를 누적하고 stream 종료 후 assistant 메시지로 messages에 추가합니다.
done 이벤트에 usage 정보를 포함시키되 cache_read 토큰도 함께 보냅니다.
클라이언트가 캐시 효과를 확인할 수 있습니다.
APIError 처리로 일반적 에러에 대응합니다.
WebSocketDisconnect로 정상 연결 해제를 감지합니다.
이 코드 하나로 ChatGPT 수준의 인터랙티브 챗봇 백엔드가 완성됩니다.
