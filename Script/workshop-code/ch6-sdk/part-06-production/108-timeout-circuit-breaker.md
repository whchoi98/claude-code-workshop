# Slide 108: Timeout과 Circuit Breaker

**Part 6: PRODUCTION 운영**

## Code Blocks

### timeout/CB

```python
# 1. Timeout 설정
from anthropic import Anthropic

client = Anthropic(timeout=30.0, max_retries=0)

# 호출별 timeout 오버라이드
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[...],
    timeout=60.0,
)

# asyncio timeout
import asyncio
async def call_with_timeout(prompt, timeout_s=30):
    try:
        async with asyncio.timeout(timeout_s):
            return await async_client.messages.create(...)
    except asyncio.TimeoutError:
        raise Exception(f"Timeout after {timeout_s}s")

# 2. Circuit Breaker 패턴
from enum import Enum
from datetime import datetime, timedelta

class CircuitState(Enum):
    CLOSED = "closed"        # 정상
    OPEN = "open"            # 차단
    HALF_OPEN = "half_open"  # 시험

class CircuitBreaker:
    def __init__(self, failure_threshold=5, recovery_timeout=60):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED

    def call(self, fn, *args, **kwargs):
        if self.state == CircuitState.OPEN:
            if datetime.utcnow() - self.last_failure_time < timedelta(seconds=self.recovery_timeout):
                raise Exception("Circuit breaker OPEN")
            self.state = CircuitState.HALF_OPEN

        try:
            result = fn(*args, **kwargs)
            if self.state == CircuitState.HALF_OPEN:
                self.state = CircuitState.CLOSED
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = datetime.utcnow()
            if self.failure_count >= self.failure_threshold:
                self.state = CircuitState.OPEN
            raise

# 사용
breaker = CircuitBreaker(failure_threshold=5, recovery_timeout=60)
def call_claude(prompt):
    return breaker.call(
        client.messages.create,
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )

# 효과: 5회 연속 실패 -> 60초 차단 -> 1회 시도 -> 결과별 결정
```

## Speaker Notes

Timeout과 Circuit Breaker로 장애 전파를 방지합니다.
1번 Timeout 설정은 클라이언트 생성 시 또는 호출별로 오버라이드 가능합니다.
max_retries는 0으로 두고 tenacity 같은 외부 라이브러리로 재시도를 관리하는 것이 권장됩니다.
asyncio timeout은 async 환경에서 async with asyncio.timeout으로 사용합니다.
시간 초과 시 TimeoutError 발생합니다.
2번 Circuit Breaker 패턴은 핵심입니다.
3가지 상태가 있습니다.
CLOSED는 정상, OPEN은 차단, HALF_OPEN은 시험 상태입니다.
CircuitBreaker 클래스에서 failure_threshold와 recovery_timeout을 정의합니다.
call 메서드는 OPEN 상태이고 recovery_timeout이 경과 안 됐으면 즉시 실패합니다.
경과했으면 HALF_OPEN으로 전환합니다.
호출 성공 시 CLOSED로 복귀하고 실패 카운트를 초기화합니다.
실패 시 카운트 증가하고 threshold 도달 시 OPEN으로 전환합니다.
효과가 명확합니다.
5회 연속 실패 시 60초 동안 모든 호출이 즉시 실패합니다.
60초 후 1회 시도해 성공이면 정상화, 실패면 다시 차단합니다.
장애 전파를 차단하고 빠른 복구를 가능하게 합니다.
