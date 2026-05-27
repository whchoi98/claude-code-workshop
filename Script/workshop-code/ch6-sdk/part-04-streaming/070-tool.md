# Slide 70: 스트림과 도구 결합

**Part 4: STREAMING**

## Code Blocks

### agent stream

```python
# 스트리밍 + Tool Use 결합 (Agent loop)

async def streaming_agent(user_input, tools, funcs, websocket):
    messages = [{"role": "user", "content": user_input}]

    while True:
        # 1. Claude 스트림 호출
        async with client.messages.stream(
            model="claude-sonnet-4-5",
            max_tokens=2048,
            tools=tools,
            messages=messages,
        ) as stream:

            current_text = ""
            current_tool = None
            current_input_json = ""

            async for event in stream:
                if event.type == "content_block_start":
                    if event.content_block.type == "tool_use":
                        current_tool = {
                            "name": event.content_block.name,
                            "id": event.content_block.id,
                        }
                        await websocket.send_json({
                            "type": "tool_start",
                            "tool": current_tool["name"],
                        })

                elif event.type == "content_block_delta":
                    if event.delta.type == "text_delta":
                        current_text += event.delta.text
                        await websocket.send_json({
                            "type": "text",
                            "text": event.delta.text,
                        })
                    elif event.delta.type == "input_json_delta":
                        current_input_json += event.delta.partial_json

            final = await stream.get_final_message()
            messages.append({
                "role": "assistant",
                "content": final.content,
            })

            # 2. stop_reason 분기
            if final.stop_reason != "tool_use":
                await websocket.send_json({"type": "done"})
                return current_text

            # 3. 도구 호출 처리
            tool_results = []
            for b in final.content:
                if b.type == "tool_use":
                    await websocket.send_json({
                        "type": "tool_executing",
                        "tool": b.name,
                        "input": b.input,
                    })
                    result = funcs[b.name](**b.input)
                    await websocket.send_json({
                        "type": "tool_result",
                        "tool": b.name,
                        "result": str(result)[:200],
                    })
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": b.id,
                        "content": json.dumps(result),
                    })

            messages.append({"role": "user", "content": tool_results})
```

## Speaker Notes

스트림과 도구 호출을 결합한 에이전트 스트리밍입니다.
streaming_agent 함수는 websocket을 받아 실시간 진행을 전송합니다.
while 루프에서 Claude 스트림을 시작합니다.
각 이벤트를 처리하면서 적절한 이벤트를 websocket으로 전송합니다.
content_block_start의 tool_use는 tool_start 이벤트로 변환됩니다.
사용자는 어떤 도구가 호출되기 시작하는지 즉시 알 수 있습니다.
text_delta는 text 이벤트로 점진적으로 전달됩니다.
input_json_delta는 누적해서 도구 인자를 완성합니다.
스트림 종료 후 final 메시지에서 stop_reason을 확인합니다.
tool_use가 아니면 done 이벤트로 종료합니다.
tool_use면 각 도구를 실행하면서 tool_executing, tool_result 이벤트를 전송합니다.
결과의 일부를 미리보기로 전송해 사용자가 진행을 확인할 수 있게 합니다.
전체 결과는 tool_results에 누적해 다음 호출에 전달합니다.
사용자 UI에서 보면 Claude가 생각하고 도구를 호출하고 결과를 받아 다시 응답하는 전 과정이 실시간으로 표시됩니다.
ChatGPT의 tool use UI와 유사한 경험이 완성됩니다.
