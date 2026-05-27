# Slide 64: 도구 호출 스트리밍

**Part 4: STREAMING**

## Code Blocks

### tool streaming

```bash
# Tool Use 응답도 스트리밍 가능

# 이벤트 흐름 (도구 호출 시)
# 1. message_start
# 2. content_block_start (type: tool_use)
# 3. content_block_delta (delta: input_json_delta)
#    -> JSON이 부분적으로 누적됨
# 4. content_block_stop
# 5. message_delta (stop_reason: tool_use)
# 6. message_stop

# 코드 예시
with client.messages.stream(
    model="claude-sonnet-4-5",
    max_tokens=2048,
    tools=TOOLS,
    messages=[{"role": "user", "content": "서울 날씨"}],
) as stream:
    current_tool = None
    current_input_json = ""

    for event in stream:
        if event.type == "content_block_start":
            if event.content_block.type == "tool_use":
                current_tool = {
                    "name": event.content_block.name,
                    "id": event.content_block.id,
                }
                print(f"\n[도구 호출 시작: {current_tool['name']}]")

        elif event.type == "content_block_delta":
            if event.delta.type == "input_json_delta":
                current_input_json += event.delta.partial_json
                # 부분 JSON 표시 (디버깅용)
                print(event.delta.partial_json, end="", flush=True)
            elif event.delta.type == "text_delta":
                print(event.delta.text, end="", flush=True)

        elif event.type == "content_block_stop":
            if current_tool:
                # JSON 완성
                import json
                input_obj = json.loads(current_input_json)
                print(f"\n[도구 입력 완성: {input_obj}]")
                # 실제로는 여기서 도구 실행
                current_tool = None
                current_input_json = ""

# 활용: UI에 도구 호출 진행 표시
# "🔧 get_weather 호출 중... location: 'S' -> 'Se' -> ... -> 'Seoul'"
```

## Speaker Notes

도구 호출도 스트리밍됩니다.
이벤트 흐름은 일반 응답과 유사하지만 차이가 있습니다.
message_start, content_block_start type tool_use, content_block_delta input_json_delta, content_block_stop, message_delta stop_reason tool_use, message_stop 순서입니다.
중요한 차이는 input_json_delta입니다.
JSON이 부분적으로 누적되어 전달됩니다.
예를 들어 location 키의 값이 S, Se, Seoul로 점진적으로 완성됩니다.
코드 예시에서 current_tool과 current_input_json을 변수로 유지합니다.
content_block_start에서 tool_use 타입을 감지해 도구 정보를 저장합니다.
content_block_delta에서 input_json_delta type인 경우 partial_json을 누적합니다.
content_block_stop에서 완성된 JSON을 파싱해 도구 실행에 사용합니다.
실제 운영에서는 UI에 도구 호출 진행을 시각화할 수 있습니다.
get_weather 호출 중 location 값이 점진적으로 완성되는 모습을 보여주면 사용자가 무엇을 하는지 즉각 이해할 수 있습니다.
이런 진행 표시는 사용자 신뢰를 크게 높입니다.
