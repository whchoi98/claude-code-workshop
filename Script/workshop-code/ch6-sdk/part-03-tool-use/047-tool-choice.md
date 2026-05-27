# Slide 47: tool_choice 제어

**Part 3: TOOL USE**

## Code Blocks

### tool_choice

```python
# 1. tool_choice 옵션 4가지

# auto (기본): Claude가 자율 결정
response = client.messages.create(
    tools=TOOLS,
    tool_choice={"type": "auto"},
    ...
)

# any: 반드시 어떤 도구든 호출 (응답 없음)
response = client.messages.create(
    tools=TOOLS,
    tool_choice={"type": "any"},
    ...
)

# tool: 특정 도구 강제
response = client.messages.create(
    tools=TOOLS,
    tool_choice={"type": "tool", "name": "search_database"},
    ...
)

# none: 도구 호출 금지 (일반 응답만)
response = client.messages.create(
    tools=TOOLS,
    tool_choice={"type": "none"},
    ...
)

# 2. 활용 예시

# 검색이 필요한 게 확실한 경우
def must_search(query: str):
    return client.messages.create(
        tools=[SEARCH_TOOL],
        tool_choice={"type": "tool", "name": "search_database"},
        messages=[{"role": "user", "content": query}],
        ...
    )
# Claude가 반드시 search_database를 호출하게 됨

# 분류 작업 (도구 없이 응답만)
def classify(text: str):
    return client.messages.create(
        tools=TOOLS,
        tool_choice={"type": "none"},   # 도구 사용 안 함
        messages=[{"role": "user", "content": f"분류: {text}"}],
        ...
    )

# 3. disable_parallel_tool_use (병렬 차단)
# 일부 시나리오에서 도구를 순차 호출하게 강제
response = client.messages.create(
    tools=TOOLS,
    tool_choice={
        "type": "auto",
        "disable_parallel_tool_use": True,
    },
    ...
)
# 의존성이 있는 도구 호출에 유용
```

## Speaker Notes

tool_choice로 도구 사용을 제어합니다.
1번 옵션 4가지가 있습니다.
auto는 기본으로 Claude가 자율 결정합니다.
any는 반드시 어떤 도구든 호출하며 일반 응답을 하지 않습니다.
tool은 특정 도구 강제로 name 명시가 필요합니다.
none은 도구 호출 금지로 일반 응답만 받습니다.
2번 활용 예시를 봅니다.
must_search 함수는 검색이 필요한 게 확실한 경우 type tool로 search_database를 강제합니다.
응답이 반드시 그 도구 호출이 됩니다.
classify 함수는 도구를 정의해 두었지만 type none으로 도구 호출을 차단합니다.
분류 같은 작업은 도구 없이 텍스트 응답만 받습니다.
3번 disable_parallel_tool_use 옵션이 있습니다.
tool_choice에 함께 명시해 병렬 호출을 차단합니다.
도구를 순차 호출하게 강제할 때 사용합니다.
예를 들어 search 결과로 다음 호출 인자가 결정되는 경우 의존성 있는 호출에 유용합니다.
