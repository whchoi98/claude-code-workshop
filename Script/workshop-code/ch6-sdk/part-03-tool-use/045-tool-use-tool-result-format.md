# Slide 45: tool_use와 tool_result 형식

**Part 3: TOOL USE**

## Code Blocks

### block formats

```bash
# 1. Claude가 생성하는 tool_use 블록
{
    "type": "tool_use",
    "id": "toolu_01abc...",        # 호출 식별자
    "name": "get_weather",          # 함수 이름
    "input": {                       # 함수 인자
        "location": "Seoul",
        "unit": "celsius",
    }
}

# 2. 프로그램이 만드는 tool_result 블록
{
    "type": "tool_result",
    "tool_use_id": "toolu_01abc...",   # 매칭 ID
    "content": "Temperature: 22°C",     # 결과 (string 또는 array)
    "is_error": False,                  # 선택, 에러 여부
}

# 3. content가 멀티 블록인 경우
{
    "type": "tool_result",
    "tool_use_id": "toolu_xyz",
    "content": [
        {"type": "text", "text": "다음 차트 참조:"},
        {"type": "image", "source": {...}},
    ],
}

# 4. 에러 처리
try:
    result = TOOL_FUNCTIONS[block.name](**block.input)
    tool_results.append({
        "type": "tool_result",
        "tool_use_id": block.id,
        "content": json.dumps(result),
    })
except Exception as e:
    tool_results.append({
        "type": "tool_result",
        "tool_use_id": block.id,
        "content": f"Error: {str(e)}",
        "is_error": True,
    })
# is_error: True면 Claude가 에러 인식하고 다르게 처리

# 5. 응답에서 tool_use 추출
for block in response.content:
    if block.type == "tool_use":
        print(f"Call {block.name} with {block.input}")
        print(f"  ID: {block.id}")
    elif block.type == "text":
        print(f"Text: {block.text}")
```

## Speaker Notes

tool_use와 tool_result 블록 형식입니다.
1번 Claude가 생성하는 tool_use 블록은 type, id, name, input 4가지 필드를 갖습니다.
id는 toolu prefix로 시작하는 고유 식별자입니다.
name은 호출할 함수 이름이고 input은 함수 인자 객체입니다.
2번 프로그램이 만드는 tool_result 블록입니다.
tool_use_id로 어느 호출의 결과인지 매칭합니다.
content는 string 또는 array입니다.
is_error는 선택이고 true면 에러 결과임을 표시합니다.
3번 content가 멀티 블록인 경우도 가능합니다.
text와 image를 함께 결과로 반환할 수 있습니다.
예를 들어 차트 데이터와 그래프 이미지를 함께 반환할 때 유용합니다.
4번 에러 처리는 try except로 합니다.
예외 발생 시 is_error를 true로 명시하고 에러 메시지를 content에 담습니다.
Claude가 이를 인식하고 다른 접근법을 시도하거나 사용자에게 에러를 보고합니다.
5번 응답에서 tool_use 추출은 type으로 분기합니다.
type이 tool_use면 name, input, id에 접근하고 text면 .text에 접근합니다.
