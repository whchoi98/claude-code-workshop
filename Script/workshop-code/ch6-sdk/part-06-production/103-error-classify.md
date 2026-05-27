# Slide 103: 에러 분류와 대응

**Part 6: PRODUCTION 운영**

## Code Blocks

### error classification

```python
from anthropic import (
    APIError, APIConnectionError, APITimeoutError,
    APIStatusError, BadRequestError, AuthenticationError,
    PermissionDeniedError, NotFoundError, RateLimitError,
)

# 카테고리 1: 재시도 가능 (transient)
RETRIABLE_ERRORS = (
    APIConnectionError,    # 네트워크 일시적
    APITimeoutError,       # timeout
    RateLimitError,        # 429 (delay 후 재시도)
)

# 카테고리 2: 재시도 무의미 (permanent)
PERMANENT_ERRORS = (
    AuthenticationError,    # 401, key 교체 필요
    PermissionDeniedError,  # 403, 권한 부여 필요
    NotFoundError,           # 404, URL 확인
    BadRequestError,         # 400, 요청 수정 필요
)

# 카테고리 3: 서버 에러 (조건부 재시도)
def is_server_error(e):
    return isinstance(e, APIStatusError) and 500 <= e.status_code < 600

def classify_error(e):
    if isinstance(e, PERMANENT_ERRORS): return "permanent"
    if isinstance(e, RETRIABLE_ERRORS): return "retriable"
    if is_server_error(e): return "server_error"
    return "unknown"

def handle_error(e, attempt):
    cat = classify_error(e)
    if cat == "permanent":
        return {"action": "fail", "msg": "요청 처리 실패"}
    if cat == "retriable" and attempt < 3:
        wait = 2 ** attempt
        if isinstance(e, RateLimitError):
            wait = max(wait, int(e.response.headers.get("retry-after", "60")))
        return {"action": "retry", "wait": wait}
    if cat == "server_error" and attempt < 2:
        return {"action": "retry", "wait": 5}
    return {"action": "fail", "msg": "처리 불가"}
```

## Speaker Notes

에러 분류와 대응 전략입니다.
Anthropic SDK 에러를 3가지 카테고리로 분류합니다.
카테고리 1은 재시도 가능 transient 에러입니다.
APIConnectionError, APITimeoutError, RateLimitError가 해당됩니다.
네트워크 일시 문제나 timeout, rate limit은 잠시 후 재시도하면 성공 가능합니다.
카테고리 2는 재시도 무의미 permanent 에러입니다.
AuthenticationError는 key를 바꿔야 하고 PermissionDeniedError는 권한 부여가 필요합니다.
NotFoundError는 URL을 확인해야 하고 BadRequestError는 요청 자체를 수정해야 합니다.
카테고리 3은 서버 에러로 조건부 재시도입니다.
5xx 상태 코드인 경우입니다.
classify_error 함수에서 isinstance로 카테고리를 결정합니다.
handle_error 함수에서 카테고리별 대응을 합니다.
permanent는 즉시 실패하고 retriable은 최대 3회 exponential backoff로 재시도하며 server_error는 짧은 간격으로 최대 2회 재시도합니다.
이런 차등 처리가 안정성의 핵심입니다.
