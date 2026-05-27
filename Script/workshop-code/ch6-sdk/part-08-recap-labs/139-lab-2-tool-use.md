# Slide 139: Lab 2 / Tool Use 봇

**Part 8: RECAP & 4 LABS**

## Code Blocks

### Lab 2

```python
# my_tool_bot.py - Tool Use 봇 직접 구현
import json
from anthropic import Anthropic

client = Anthropic()

# Step 1: 도구 정의
TOOLS = [
    {
        "name": "get_weather",
        "description": "도시의 현재 날씨 조회",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string"},
                "unit": {"type": "string", "enum": ["c", "f"]},
            },
            "required": ["city"],
        },
    },
    {
        "name": "calculate",
        "description": "수학 계산 수행",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {"type": "string"},
            },
            "required": ["expression"],
        },
    },
]

# Step 2: 실제 함수 (mock 또는 실제 API)
def get_weather(city, unit="c"):
    return {"city": city, "temp": 22, "unit": unit, "condition": "맑음"}

def calculate(expression):
    try:
        return {"result": eval(expression, {"__builtins__": {}})}
    except: return {"error": "Invalid expression"}

FUNCS = {"get_weather": get_weather, "calculate": calculate}

# Step 3: 사이클 구현
def run_bot(user_input):
    messages = [{"role": "user", "content": user_input}]

    for iteration in range(10):    # 최대 10회
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=2048,
            tools=TOOLS,
            messages=messages,
        )

        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason != "tool_use":
            return "".join(b.text for b in response.content if b.type=="text")

        # Tool use 처리
        results = []
        for block in response.content:
            if block.type == "tool_use":
                print(f"Calling {block.name}({block.input})")
                try:
                    output = FUNCS[block.name](**block.input)
                    results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": json.dumps(output),
                    })
                except Exception as e:
                    results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(e),
                        "is_error": True,
                    })

        messages.append({"role": "user", "content": results})

    return "Max iterations"

# Step 4: 테스트
print(run_bot("서울 날씨와 100*25 계산"))

# 도전 과제
# - 자신만의 도구 3개 추가
# - 에러 케이스 만들기 (잘못된 도시명)
# - 멀티턴 대화 지원
# - 도구 사용 통계 추적
# - 권한 제한 (DANGEROUS_TOOLS)
```

## Speaker Notes

Lab 2는 Tool Use 봇 직접 구현입니다.
약 30분 소요됩니다.
4단계로 진행합니다.
Step 1 도구 정의에서 get_weather와 calculate 두 도구를 정의합니다.
JSON Schema로 입력 형식을 명시합니다.
Step 2 실제 함수를 구현합니다.
get_weather는 mock 응답을 반환하고 calculate는 eval로 수식을 평가합니다.
FUNCS dict로 매핑합니다.
Step 3 사이클 구현이 핵심입니다.
for 루프로 최대 10회 반복하고 각 iteration에서 messages.create를 호출합니다.
stop_reason이 tool_use가 아니면 text를 반환하고 종료합니다.
tool_use면 각 블록을 처리하고 결과를 tool_result로 다음 호출에 전달합니다.
에러는 is_error true로 명시합니다.
Step 4 테스트로 서울 날씨와 100 곱하기 25 같은 복합 질문을 던집니다.
Claude가 두 도구를 모두 호출하는 흐름을 확인합니다.
도전 과제 5가지를 제시합니다.
자신만의 도구 3개 추가, 에러 케이스 만들기, 멀티턴 대화 지원, 도구 사용 통계, 권한 제한입니다.
시간이 남으면 도전 과제도 시도해 보시기 바랍니다.
