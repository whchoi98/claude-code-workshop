# Slide 140: Lab 3 / Streaming 챗봇

**Part 8: RECAP & 4 LABS**

## Code Blocks

### Lab 3

```python
# server.py - FastAPI SSE 서버
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import anthropic
import json

app = FastAPI()
client = anthropic.AsyncAnthropic()

# 세션 보관 (실무는 Redis)
sessions = {}

@app.websocket("/chat/{session_id}")
async def chat(ws: WebSocket, session_id: str):
    await ws.accept()
    if session_id not in sessions:
        sessions[session_id] = {"messages": []}

    try:
        while True:
            data = await ws.receive_json()
            user_input = data["prompt"]
            sessions[session_id]["messages"].append({
                "role": "user", "content": user_input,
            })

            full_response = ""
            await ws.send_json({"type": "start"})

            try:
                async with client.messages.stream(
                    model="claude-sonnet-4-5",
                    max_tokens=2048,
                    messages=sessions[session_id]["messages"],
                ) as stream:
                    async for text in stream.text_stream:
                        full_response += text
                        await ws.send_json({"type": "delta", "text": text})

                    final = await stream.get_final_message()
                    sessions[session_id]["messages"].append({
                        "role": "assistant", "content": full_response,
                    })

                    await ws.send_json({
                        "type": "done",
                        "tokens": final.usage.output_tokens,
                    })
            except Exception as e:
                await ws.send_json({"type": "error", "message": str(e)})

    except WebSocketDisconnect:
        print(f"Session {session_id} disconnected")

# 실행: uvicorn server:app --reload

# index.html - 간단한 클라이언트
<!DOCTYPE html>
<html><body>
<div id="chat"></div>
<input id="prompt" />
<button onclick="send()">Send</button>
<script>
const ws = new WebSocket("ws://localhost:8000/chat/sess1");
let currentMsg = null;
ws.onmessage = (e) => {
  const msg = JSON.parse(e.data);
  if (msg.type === "start") {
    currentMsg = document.createElement("p");
    document.getElementById("chat").appendChild(currentMsg);
  } else if (msg.type === "delta") {
    currentMsg.innerText += msg.text;
  } else if (msg.type === "done") {
    currentMsg = null;
  }
};
function send() {
  const p = document.getElementById("prompt").value;
  ws.send(JSON.stringify({prompt: p}));
  document.getElementById("prompt").value = "";
}
</script>
</body></html>
```

## Speaker Notes

Lab 3는 Streaming 챗봇입니다.
약 30분 소요됩니다.
FastAPI와 간단한 HTML 클라이언트를 만듭니다.
서버는 WebSocket으로 양방향 통신을 구현합니다.
sessions dict에 세션별 messages를 보관합니다.
실무에서는 Redis 같은 외부 저장소를 사용해야 합니다.
chat endpoint에서 session_id를 path parameter로 받습니다.
클라이언트에서 prompt를 받으면 messages에 추가하고 client.messages.stream으로 호출합니다.
async for로 text_stream을 순회하며 delta 이벤트를 클라이언트에 전송합니다.
full_response를 누적해 stream 종료 후 assistant 메시지로 messages에 추가합니다.
done 이벤트에 토큰 정보를 포함시킵니다.
예외 발생 시 error 이벤트로 알립니다.
WebSocketDisconnect로 정상 연결 해제를 감지합니다.
클라이언트는 간단한 HTML 페이지입니다.
WebSocket 객체를 만들고 onmessage 핸들러로 delta를 처리합니다.
currentMsg에 텍스트를 점진적으로 추가하고 done에서 새 메시지를 준비합니다.
send 함수로 prompt를 전송합니다.
uvicorn으로 서버를 실행하고 브라우저에서 index.html을 열면 동작 확인 가능합니다.
ChatGPT 같은 인터랙티브 챗봇이 30분 만에 완성됩니다.
