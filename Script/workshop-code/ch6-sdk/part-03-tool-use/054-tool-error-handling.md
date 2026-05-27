# Slide 54: 도구 에러 처리

**Part 3: TOOL USE**

## Code Blocks

### tool errors

```python
# 1. 안전한 도구 실행 wrapper
def safe_execute_tool(name: str, input: dict, funcs: dict) -> dict:
    if name not in funcs:
        return {"error": f"Unknown tool: {name}", "is_error": True}

    try:
        result = funcs[name](**input)
        return {"result": result, "is_error": False}
    except KeyError as e:
        return {
            "error": f"Missing parameter: {e}",
            "is_error": True,
        }
    except ValueError as e:
        return {
            "error": f"Invalid value: {e}",
            "is_error": True,
        }
    except Exception as e:
        return {
            "error": f"Tool failed: {type(e).__name__}: {e}",
            "is_error": True,
        }

# 2. tool_result에 is_error 명시
for b in r.content:
    if b.type == "tool_use":
        result = safe_execute_tool(b.name, b.input, FUNCS)
        if result["is_error"]:
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": b.id,
                "content": result["error"],
                "is_error": True,
            })
        else:
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": b.id,
                "content": json.dumps(result["result"]),
            })

# 3. 재시도 가능한 에러
class RetriableError(Exception): pass

def call_api(url):
    r = requests.get(url, timeout=5)
    if r.status_code == 429:
        raise RetriableError("Rate limited")
    if r.status_code >= 500:
        raise RetriableError(f"Server error {r.status_code}")
    r.raise_for_status()
    return r.json()

def tool_with_retry(name, input, funcs, max_retries=3):
    for attempt in range(max_retries):
        try:
            return funcs[name](**input)
        except RetriableError as e:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)   # exponential backoff
                continue
            raise

# 4. 에러 후 Claude의 대응
# is_error: True 시 Claude는:
# - 다른 인자로 재시도
# - 다른 도구 사용
# - 사용자에게 명확히 보고
```

## Speaker Notes

도구 에러 처리로 Claude가 회복할 수 있게 만듭니다.
1번 안전한 도구 실행 wrapper입니다.
safe_execute_tool 함수에서 name과 input을 받아 정확한 에러 정보와 함께 결과를 반환합니다.
도구를 찾을 수 없으면 Unknown tool 에러, 누락된 파라미터는 KeyError, 잘못된 값은 ValueError로 구분합니다.
그 외 예외는 일반 에러로 처리합니다.
에러 메시지에 예외 타입 이름을 포함시켜 Claude가 더 잘 이해하게 합니다.
2번 tool_result에 is_error를 명시합니다.
에러일 때 is_error true로 content에 에러 메시지를 담습니다.
성공 시는 일반적인 content만 전달합니다.
3번 재시도 가능한 에러를 구분합니다.
RetriableError를 만들어 rate limit이나 서버 에러에 사용합니다.
tool_with_retry 함수에서 exponential backoff로 최대 3회 재시도합니다.
4번 에러 후 Claude의 대응이 중요합니다.
is_error true를 받으면 Claude는 다른 인자로 재시도하거나 다른 도구를 사용하거나 사용자에게 명확히 보고합니다.
에러를 숨기지 않고 정확히 전달하는 것이 Claude의 회복력을 높입니다.
