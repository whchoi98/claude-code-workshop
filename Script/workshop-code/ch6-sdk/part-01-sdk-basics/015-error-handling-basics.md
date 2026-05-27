# Slide 15: 에러 처리 기본

**Part 1: SDK 기본**

## Code Blocks

### error handling

```python
# Python 에러 클래스
from anthropic import (
    Anthropic,
    APIError,                    # 일반 API 에러
    APIConnectionError,          # 네트워크 연결 실패
    APITimeoutError,             # 응답 timeout
    BadRequestError,             # 400 잘못된 요청
    AuthenticationError,         # 401 인증 실패
    PermissionDeniedError,       # 403 권한 거부
    NotFoundError,               # 404
    RateLimitError,              # 429 너무 많은 요청
    APIStatusError,              # 5xx 서버 에러
)

client = Anthropic()

try:
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": "Hi"}],
    )
    print(message.content[0].text)

except AuthenticationError as e:
    print(f"인증 실패: API key 확인. {e}")
    # 재시도 의미 없음. 사람 개입 필요.

except RateLimitError as e:
    # 헤더에서 retry-after 확인 가능
    retry_after = int(e.response.headers.get("retry-after", "60"))
    print(f"Rate limited. {retry_after}초 후 재시도")
    time.sleep(retry_after)
    # 재시도

except APIConnectionError as e:
    print(f"연결 실패: 네트워크 확인. {e}")
    # exponential backoff로 재시도

except APITimeoutError as e:
    print(f"Timeout: 작업이 너무 오래 걸림. {e}")
    # max_tokens 줄이거나 입력 분할

except BadRequestError as e:
    print(f"잘못된 요청: 인자 확인. {e}")
    # 코드 버그 가능성

except APIStatusError as e:
    print(f"서버 에러 {e.status_code}: 재시도")

except APIError as e:
    print(f"일반 API 에러: {e}")
```

## Speaker Notes

Python 에러 처리 기본 패턴입니다.
anthropic 패키지가 제공하는 에러 클래스 7가지 이상을 import합니다.
APIError는 일반 API 에러의 부모 클래스입니다.
APIConnectionError는 네트워크 연결 실패입니다.
APITimeoutError는 응답 timeout입니다.
BadRequestError는 400으로 잘못된 요청입니다.
AuthenticationError는 401 인증 실패입니다.
PermissionDeniedError는 403 권한 거부입니다.
NotFoundError는 404, RateLimitError는 429, APIStatusError는 5xx 서버 에러입니다.
try except 블록에서 구체적인 에러부터 잡습니다.
AuthenticationError는 재시도 의미가 없으므로 사람 개입이 필요합니다.
RateLimitError는 헤더의 retry-after를 확인해 적절한 시간만 대기합니다.
APIConnectionError는 exponential backoff로 재시도합니다.
APITimeoutError는 max_tokens를 줄이거나 입력을 분할해 해결합니다.
BadRequestError는 코드 버그 가능성이 높으므로 인자 검증이 필요합니다.
APIStatusError는 서버 에러로 재시도가 효과적입니다.
마지막 APIError는 catch-all로 두어 미예상 에러도 처리합니다.
