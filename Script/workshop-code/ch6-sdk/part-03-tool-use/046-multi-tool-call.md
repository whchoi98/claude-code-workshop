# Slide 46: 멀티 도구 호출

**Part 3: TOOL USE**

## Code Blocks

### multi-tool

```python
# 1. 여러 도구 정의
TOOLS = [
    {"name": "get_weather", "description": "...", "input_schema": {...}},
    {"name": "search_users", "description": "...", "input_schema": {...}},
    {"name": "create_ticket", "description": "...", "input_schema": {...}},
    {"name": "send_email", "description": "...", "input_schema": {...}},
]

# 2. Claude가 여러 도구를 한 번에 호출
# response.content에 여러 tool_use 블록이 동시에 나올 수 있음
# 예시: "서울 날씨와 김씨 정보 확인" -> 2개 도구 동시 호출

response = client.messages.create(...)

# 처리
for block in response.content:
    if block.type == "tool_use":
        # 각각 처리
        result = TOOL_FUNCTIONS[block.name](**block.input)
        ...

# 3. 병렬 실행 (async)
import asyncio
from anthropic import AsyncAnthropic

async def run_tool(block):
    return await asyncio.to_thread(
        TOOL_FUNCTIONS[block.name], **block.input
    )

async def process_tools(response):
    tool_blocks = [b for b in response.content if b.type == "tool_use"]
    results = await asyncio.gather(*[
        run_tool(b) for b in tool_blocks
    ])

    return [
        {
            "type": "tool_result",
            "tool_use_id": block.id,
            "content": json.dumps(result),
        }
        for block, result in zip(tool_blocks, results)
    ]

# 4. 도구 호출 횟수 제한
MAX_TOOL_CALLS = 10
call_count = 0

while call_count < MAX_TOOL_CALLS:
    response = client.messages.create(...)
    if response.stop_reason != "tool_use":
        break
    # 도구 처리
    for block in response.content:
        if block.type == "tool_use":
            call_count += 1
    ...

# 5. 멀티턴에서 도구 사용 추적
tool_history = []
for block in response.content:
    if block.type == "tool_use":
        tool_history.append({
            "name": block.name,
            "input": block.input,
            "timestamp": time.time(),
        })
```

## Speaker Notes

멀티 도구 호출 패턴입니다.
1번 여러 도구 정의는 tools 배열에 추가하면 됩니다.
Claude가 모든 도구를 알고 상황에 맞게 선택합니다.
2번 Claude가 여러 도구를 한 번에 호출할 수 있습니다.
response.content에 여러 tool_use 블록이 동시에 나올 수 있습니다.
서울 날씨와 김씨 정보 확인 같은 복합 질문에서 발생합니다.
각 블록을 순회하면서 처리합니다.
3번 병렬 실행은 async로 구현합니다.
asyncio.to_thread로 동기 함수를 비동기로 변환하고 asyncio.gather로 동시 실행합니다.
결과를 tool_use_id로 매칭해 tool_result 배열을 만듭니다.
여러 도구의 응답 시간 합산이 아닌 가장 느린 도구의 시간만 걸립니다.
4번 도구 호출 횟수 제한은 무한 루프 방지에 필수입니다.
MAX_TOOL_CALLS를 10 정도로 두고 도달하면 강제 종료합니다.
5번 멀티턴에서 도구 사용 추적은 로깅과 디버깅에 유용합니다.
tool_history에 name, input, timestamp를 기록해 어떤 도구가 언제 호출됐는지 추적할 수 있습니다.
