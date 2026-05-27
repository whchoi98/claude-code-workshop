# Slide 44: 호출 사이클 구현

**Part 3: TOOL USE**

## Code Blocks

### tool cycle

```python
# 도구 매핑
def get_weather(location: str, unit: str = "celsius") -> dict:
    # 실제 API 호출 등
    return {"temp": 22, "condition": "맑음", "unit": unit}

def search_database(query: str, limit: int = 10, **kwargs):
    # DB 검색
    return [{"id": 1, "name": "..."}]

TOOL_FUNCTIONS = {
    "get_weather": get_weather,
    "search_database": search_database,
}

# 도구 호출 사이클
def run_agent(user_input: str) -> str:
    messages = [{"role": "user", "content": user_input}]

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=2048,
            tools=TOOLS,
            messages=messages,
        )

        # 응답을 messages에 추가
        messages.append({
            "role": "assistant",
            "content": response.content,
        })

        # stop_reason 분기
        if response.stop_reason != "tool_use":
            # 도구 호출 완료. 최종 응답 추출
            text_blocks = [
                b.text for b in response.content if b.type == "text"
            ]
            return "\n".join(text_blocks)

        # tool_use 블록 처리
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                # 함수 실행
                result = TOOL_FUNCTIONS[block.name](**block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(result),
                })

        # 결과를 다음 user 메시지로
        messages.append({
            "role": "user",
            "content": tool_results,
        })

# 사용
result = run_agent("서울 날씨와 김씨의 정보 알려줘")
```

## Speaker Notes

호출 사이클 구현은 while 루프 패턴이 핵심입니다.
먼저 TOOL_FUNCTIONS에 함수 매핑을 정의합니다.
get_weather와 search_database 같은 실제 함수를 dict로 매핑합니다.
run_agent 함수에서 user_input으로 시작하고 while True 루프에 들어갑니다.
client.messages.create로 호출하고 응답을 messages에 추가합니다.
stop_reason이 tool_use가 아니면 도구 호출이 끝난 것이므로 text 블록을 추출해 반환합니다.
text 블록만 필터링해서 join합니다.
stop_reason이 tool_use면 도구 호출 처리가 필요합니다.
response.content를 순회하면서 type이 tool_use인 블록을 찾습니다.
각 블록의 name과 input으로 함수를 실행합니다.
결과를 tool_result block으로 변환하고 tool_use_id로 매칭합니다.
결과 배열을 다음 user 메시지로 추가하고 루프를 계속합니다.
Claude가 여러 도구를 순차 또는 병렬 호출하더라도 이 패턴으로 모두 처리 가능합니다.
최종적으로 stop_reason이 end_turn이 되면 루프가 종료됩니다.
