# Slide 42: Tool Use 개념

**Part 3: TOOL USE**

## Code Blocks

### concept

```bash
# Tool Use의 흐름
# 1. 도구 정의
tools = [
    {
        "name": "get_weather",
        "description": "특정 위치의 현재 날씨 조회",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "도시명"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
        },
    }
]

# 2. Claude 호출 (도구와 함께)
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "서울의 날씨"}],
)

# 3. Claude의 응답 분기
if response.stop_reason == "tool_use":
    # 도구 호출 필요
    pass
else:
    # 일반 응답
    print(response.content[0].text)
```

## Speaker Notes

Tool Use 개념은 에이전트 패턴의 핵심입니다.
흐름은 5단계입니다.
tools를 정의하고 호출하면 Claude가 도구 사용을 결정합니다.
프로그램이 함수를 실행하고 결과를 tool_result로 전달하면 Claude가 최종 응답을 생성합니다.
예시로 get_weather 도구를 봅니다.
name은 함수 이름, description은 언제 사용할지 설명, input_schema는 JSON Schema 형식의 입력 정의입니다.
properties에 각 파라미터의 type과 description, required에 필수 파라미터를 명시합니다.
Claude 호출 시 tools 매개변수에 정의 배열을 전달합니다.
응답의 stop_reason이 tool_use면 도구 호출이 필요하고 그렇지 않으면 일반 응답입니다.
stop_reason으로 분기 처리하는 패턴이 핵심입니다.
