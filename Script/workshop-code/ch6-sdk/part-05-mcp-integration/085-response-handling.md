# Slide 85: 응답 처리

**Part 5: MCP SDK 통합**

## Code Blocks

### response

```python
# 응답 ContentBlock 타입들 (MCP 사용 시)
response = client.beta.messages.create(...)

# 1. content 배열 순회
for block in response.content:
    # text 블록
    if block.type == "text":
        print(block.text)

    # MCP 도구 호출 (Claude가 한 것)
    elif block.type == "mcp_tool_use":
        print(f"MCP Tool: {block.server_name}.{block.name}")
        print(f"  ID: {block.id}")
        print(f"  Input: {block.input}")

    # MCP 도구 결과 (자동으로 포함됨)
    elif block.type == "mcp_tool_result":
        print(f"  Tool Use ID: {block.tool_use_id}")
        for sub in block.content:
            if sub.type == "text":
                print(f"  Result: {sub.text[:200]}")

# 2. 도구 사용 통계
def analyze_mcp_usage(response):
    tools_used = {}
    for block in response.content:
        if block.type == "mcp_tool_use":
            key = f"{block.server_name}.{block.name}"
            tools_used[key] = tools_used.get(key, 0) + 1
    return tools_used

# 사용 예시
stats = analyze_mcp_usage(response)
# {"github.list_issues": 1, "slack.send_message": 1}

# 3. 결과 텍스트만 추출
def get_final_text(response):
    texts = [b.text for b in response.content if b.type == "text"]
    return "".join(texts)

# 4. MCP 에러 처리
for block in response.content:
    if block.type == "mcp_tool_result":
        if block.is_error:
            print(f"MCP error: {block.content[0].text}")
            # 사용자에게 알림 또는 재시도

# 5. usage 정보
# MCP 도구 호출의 토큰도 usage에 포함됨
print(f"Total tokens: {response.usage.input_tokens + response.usage.output_tokens}")
print(f"Stop reason: {response.stop_reason}")
```

## Speaker Notes

MCP 응답 처리는 일반 응답과 유사하지만 차이가 있습니다.
응답 ContentBlock에 새로운 타입이 추가됩니다.
1번 content 배열 순회 시 3가지 새 타입을 처리합니다.
text는 일반 텍스트로 동일합니다.
mcp_tool_use는 Claude가 호출한 MCP 도구입니다.
server_name으로 어느 서버의 도구인지, name으로 도구 이름을 알 수 있습니다.
mcp_tool_result는 도구 호출 결과입니다.
tool_use_id로 어느 호출의 결과인지 매칭됩니다.
중요한 점은 mcp_tool_result가 자동으로 응답에 포함된다는 것입니다.
우리가 따로 처리할 필요가 없습니다.
2번 도구 사용 통계는 analyze_mcp_usage 함수로 추적합니다.
server_name과 name 조합으로 어떤 도구가 얼마나 사용됐는지 카운트합니다.
3번 결과 텍스트만 추출은 text 블록만 필터링해서 join합니다.
사용자에게 보여줄 최종 응답입니다.
4번 MCP 에러 처리는 is_error 필드로 확인합니다.
MCP 서버가 에러를 반환하면 이 필드가 true가 됩니다.
5번 usage 정보에 MCP 도구 호출의 토큰도 포함됩니다.
비용 추적 시 함께 고려해야 합니다.
