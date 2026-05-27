# Slide 55: 도구 호출 검증

**Part 3: TOOL USE**

## Code Blocks

### validation

```python
# 1. 입력 검증 (JSON Schema)
from jsonschema import validate, ValidationError

def validate_tool_input(tool: dict, input: dict) -> bool:
    try:
        validate(instance=input, schema=tool["input_schema"])
        return True
    except ValidationError as e:
        print(f"Invalid input: {e.message}")
        return False

# 2. 위험한 작업은 사용자 확인
DANGEROUS_TOOLS = {"delete_file", "send_email", "transfer_money"}

def execute_with_confirm(name, input, funcs):
    if name in DANGEROUS_TOOLS:
        # 사용자 확인 요청
        print(f"⚠️  도구 '{name}' 호출 ({input})")
        ans = input("실행할까요? (y/N): ")
        if ans.lower() != "y":
            return {"error": "User cancelled"}

    return funcs[name](**input)

# 3. 도구별 권한 확인
TOOL_PERMISSIONS = {
    "read_file": "files.read",
    "write_file": "files.write",
    "delete_file": "files.delete",
    "send_email": "comms.send",
}

def check_permission(tool: str, user) -> bool:
    required = TOOL_PERMISSIONS.get(tool)
    if not required:
        return True
    return required in user.permissions

# 4. 호출 빈도 제한
from collections import deque, defaultdict
import time

rate_limits = defaultdict(lambda: deque(maxlen=100))

def check_rate_limit(tool: str, max_per_minute=10) -> bool:
    now = time.time()
    calls = rate_limits[tool]
    # 1분 이전 호출 제거
    while calls and calls[0] < now - 60:
        calls.popleft()
    if len(calls) >= max_per_minute:
        return False
    calls.append(now)
    return True

# 5. 종합 검증
def safe_tool_call(name, input, funcs, user):
    if not check_permission(name, user):
        return {"error": "Permission denied", "is_error": True}

    if not check_rate_limit(name):
        return {"error": "Rate limit", "is_error": True}

    if not validate_tool_input({"input_schema": TOOLS[name]}, input):
        return {"error": "Invalid input", "is_error": True}

    return funcs[name](**input)
```

## Speaker Notes

도구 호출 검증으로 안전한 자동 실행을 만듭니다.
1번 입력 검증은 jsonschema 라이브러리로 합니다.
validate_tool_input 함수에서 input이 schema에 맞는지 확인합니다.
ValidationError를 잡아 false를 반환합니다.
2번 위험한 작업은 사용자 확인을 요청합니다.
DANGEROUS_TOOLS set에 delete_file, send_email, transfer_money 같은 도구를 등록합니다.
execute_with_confirm 함수에서 위험 도구는 사용자 input을 받아 확인 후 실행합니다.
3번 도구별 권한 확인은 TOOL_PERMISSIONS mapping을 사용합니다.
각 도구가 요구하는 권한을 정의하고 user.permissions에 포함되는지 검사합니다.
4번 호출 빈도 제한은 deque로 슬라이딩 윈도우를 구현합니다.
도구별로 최근 호출 시각을 기록하고 1분 이내 max_per_minute 초과 시 차단합니다.
5번 종합 검증으로 모든 안전 장치를 한 번에 적용합니다.
safe_tool_call에서 권한, rate limit, schema 순서로 확인 후 실패 시 즉시 에러 결과를 반환합니다.
프로덕션에서 모든 도구 호출이 이 단일 함수를 통과하도록 강제하는 것이 권장됩니다.
