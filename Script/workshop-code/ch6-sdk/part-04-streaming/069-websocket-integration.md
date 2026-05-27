# Slide 69: WebSocket 통합

**Part 4: STREAMING**

## Code Blocks

### WebSocket

```python
# server.py - FastAPI WebSocket
from fastapi import FastAPI, WebSocket
from fastapi.websockets import WebSocketDisconnect
import anthropic
import json

app = FastAPI()
client = anthropic.AsyncAnthropic()

@app.websocket("/chat/ws")
async def chat_ws(websocket: WebSocket):
    await websocket.accept()
    messages = []    # 세션별 대화 누적

    try:
        while True:
            # 클라이언트로부터 메시지 수신
            data = await websocket.receive_json()
            user_input = data["prompt"]

            messages.append({"role": "user", "content": user_input})

            # Claude 호출 (스트림)
            full_response = ""
            async with client.messages.stream(
                model="claude-sonnet-4-5",
                max_tokens=2048,
                messages=messages,
            ) as stream:
                async for event in stream:
                    if event.type == "content_block_delta":
                        if event.delta.type == "text_delta":
                            text = event.delta.text
                            full_response += text
                            # 클라이언트로 전송
                            await websocket.send_json({
                                "type": "delta",
                                "text": text,
                            })

                final = await stream.get_final_message()
                messages.append({
                    "role": "assistant",
                    "content": full_response,
                })

                await websocket.send_json({
                    "type": "done",
                    "usage": {
                        "input": final.usage.input_tokens,
                        "output": final.usage.output_tokens,
                    },
                })

    except WebSocketDisconnect:
        print(f"Client disconnected, conversation length: {len(messages)}")

# 클라이언트 (JavaScript)
const ws = new WebSocket("ws://localhost:8000/chat/ws");

ws.onopen = () => ws.send(JSON.stringify({prompt: "Hi"}));

ws.onmessage = (e) => {
  const msg = JSON.parse(e.data);
  if (msg.type === "delta") {
    appendText(msg.text);
  } else if (msg.type === "done") {
    console.log("Tokens:", msg.usage);
  }
};
```

## Speaker Notes

WebSocket 통합으로 양방향 실시간 통신을 구현합니다.
FastAPI의 WebSocket 지원으로 chat/ws endpoint를 만듭니다.
websocket.accept로 연결을 수락하고 messages list로 세션별 대화를 누적 관리합니다.
while True 루프에서 receive_json으로 클라이언트 메시지를 받습니다.
user_input을 messages에 추가하고 Claude를 스트림으로 호출합니다.
async for로 이벤트를 순회하며 content_block_delta의 text_delta를 websocket.send_json으로 클라이언트에 전송합니다.
type을 delta로 두고 text를 함께 보냅니다.
응답 완료 후 full_response를 messages에 추가해 다음 턴의 컨텍스트로 사용합니다.
done 이벤트로 토큰 사용량을 전송합니다.
WebSocketDisconnect 예외로 클라이언트 연결 해제를 감지합니다.
클라이언트는 JavaScript의 WebSocket API를 사용합니다.
onopen에서 첫 메시지를 보내고 onmessage에서 type별 분기 처리합니다.
delta는 텍스트 추가, done은 완료 처리입니다.
WebSocket은 SSE보다 양방향이고 헤더 오버헤드가 적습니다.
실시간 양방향 통신이 필요한 멀티턴 채팅에 적합합니다.
