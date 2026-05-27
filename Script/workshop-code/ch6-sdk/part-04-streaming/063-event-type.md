# Slide 63: 스트림 이벤트 타입

**Part 4: STREAMING**

## Code Blocks

### event types

```bash
# Anthropic SSE 이벤트 6가지

# 1. message_start: 메시지 시작
{
    "type": "message_start",
    "message": {
        "id": "msg_...",
        "type": "message",
        "role": "assistant",
        "content": [],
        "model": "claude-sonnet-4-5",
        "stop_reason": null,
        "usage": {"input_tokens": 25, "output_tokens": 1},
    }
}

# 2. content_block_start: 콘텐츠 블록 시작
{
    "type": "content_block_start",
    "index": 0,
    "content_block": {"type": "text", "text": ""}
}

# 3. content_block_delta: 콘텐츠 증분 (가장 자주)
{
    "type": "content_block_delta",
    "index": 0,
    "delta": {"type": "text_delta", "text": "Hello"}
}

# 4. content_block_stop: 콘텐츠 블록 종료
{
    "type": "content_block_stop",
    "index": 0
}

# 5. message_delta: 메시지 메타 업데이트
{
    "type": "message_delta",
    "delta": {"stop_reason": "end_turn", "stop_sequence": null},
    "usage": {"output_tokens": 42}
}

# 6. message_stop: 메시지 완료
{
    "type": "message_stop"
}

# 저수준 처리 (Python)
with client.messages.stream(...) as stream:
    for event in stream:
        if event.type == "message_start":
            print(f"Start: {event.message.id}")
        elif event.type == "content_block_delta":
            if event.delta.type == "text_delta":
                print(event.delta.text, end="", flush=True)
        elif event.type == "message_stop":
            print("\n[완료]")
```

## Speaker Notes

스트림 이벤트 타입 6가지를 정리합니다.
1번 message_start는 메시지 시작 이벤트입니다.
message 객체에 id, model, 초기 usage 정보가 포함됩니다.
2번 content_block_start는 콘텐츠 블록의 시작입니다.
index와 content_block type을 포함합니다.
텍스트 블록이나 tool_use 블록의 시작에 발생합니다.
3번 content_block_delta는 가장 자주 발생하는 이벤트입니다.
delta type이 text_delta인 경우 텍스트 청크가 포함됩니다.
4번 content_block_stop은 콘텐츠 블록 종료입니다.
5번 message_delta는 메시지 메타 업데이트입니다.
stop_reason과 누적 usage가 포함됩니다.
6번 message_stop은 메시지 완료입니다.
저수준 처리는 for event in stream으로 순회하며 type별 분기합니다.
event.type 확인 후 message_start, content_block_delta, message_stop 같은 케이스로 처리합니다.
content_block_delta는 delta.type이 text_delta인 경우만 텍스트로 출력합니다.
이런 저수준 처리가 필요한 경우는 도구 호출 추적이나 진행 상황 UI 같은 정밀한 제어가 필요할 때입니다.
