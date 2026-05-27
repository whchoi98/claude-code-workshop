# Slide 104: Retry Python

**Part 6: PRODUCTION 운영**

## Code Blocks

### retry Python

```python
# 1. tenacity 라이브러리 활용
from tenacity import (
    retry, stop_after_attempt, wait_exponential,
    retry_if_exception_type, before_sleep_log,
)
import logging

logger = logging.getLogger(__name__)

@retry(
    retry=retry_if_exception_type((
        APIConnectionError, APITimeoutError, RateLimitError,
    )),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=60),
    before_sleep=before_sleep_log(logger, logging.WARNING),
)
def call_claude(prompt):
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text

# 2. 수동 구현 (라이브러리 없이)
import time, random

def call_with_backoff(prompt, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            return client.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}],
            )
        except (APIConnectionError, APITimeoutError) as e:
            wait = 2 ** attempt + random.uniform(0, 1)
            logger.warning(f"Attempt {attempt+1}: {e}, retry in {wait:.1f}s")
            time.sleep(wait)
        except RateLimitError as e:
            wait = int(e.response.headers.get("retry-after", "60"))
            time.sleep(wait)
    raise Exception("Max retries exceeded")

# 3. async 버전
import asyncio

async def call_async_retry(prompt, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            return await async_client.messages.create(...)
        except (APIConnectionError, APITimeoutError):
            await asyncio.sleep(2 ** attempt + random.uniform(0, 1))
        except RateLimitError as e:
            await asyncio.sleep(int(e.response.headers.get("retry-after", "60")))
    raise Exception("Max retries")
```

## Speaker Notes

Python에서 Retry with Backoff 패턴입니다.
1번 tenacity 라이브러리가 가장 깔끔합니다.
@retry 데코레이터로 함수를 감싸면 자동 재시도가 적용됩니다.
retry_if_exception_type으로 재시도할 에러 타입을 명시합니다.
stop_after_attempt 3으로 최대 3회 시도합니다.
wait_exponential로 지수 backoff를 적용합니다.
min 2초에서 max 60초 사이로 제한합니다.
before_sleep_log로 재시도 직전에 로깅합니다.
2번 수동 구현은 라이브러리 없이 직접 작성합니다.
for 루프에서 max_attempts만큼 반복합니다.
APIConnectionError와 APITimeoutError는 exponential backoff와 jitter를 적용합니다.
jitter는 random uniform 0에서 1초로 thundering herd를 방지합니다.
RateLimitError는 retry-after 헤더를 우선 사용합니다.
3번 async 버전은 time.sleep을 await asyncio.sleep으로 바꾸기만 하면 됩니다.
비동기 클라이언트도 동일한 패턴이 적용됩니다.
