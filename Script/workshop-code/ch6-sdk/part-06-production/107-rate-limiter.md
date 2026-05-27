# Slide 107: Rate Limiter 구현

**Part 6: PRODUCTION 운영**

## Code Blocks

### rate limiter

```python
# 1. Token Bucket (Python)
import time, threading

class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill = time.time()
        self.lock = threading.Lock()

    def acquire(self, n=1, blocking=True):
        with self.lock:
            self._refill()
            if self.tokens >= n:
                self.tokens -= n
                return True
            if not blocking: return False

        wait = (n - self.tokens) / self.refill_rate
        time.sleep(wait)
        with self.lock:
            self.tokens -= n
            return True

    def _refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
        self.last_refill = now

# 사용: 50 RPM = 초당 0.83 토큰
limiter = TokenBucket(capacity=10, refill_rate=50/60)

def call_with_limit(prompt):
    limiter.acquire(1)
    return client.messages.create(...)

# 2. Redis 기반 분산 rate limiter
import redis
r = redis.Redis()

def acquire_distributed(user_id, limit_per_minute):
    key = f"ratelimit:{user_id}:{int(time.time() / 60)}"
    current = r.incr(key)
    if current == 1: r.expire(key, 60)
    return current <= limit_per_minute

# 사용
if not acquire_distributed("user_1", 50):
    raise Exception("Rate limit exceeded")

# 3. Token-aware Limiter (RPM + TPM)
class TokenAwareLimiter:
    def __init__(self, rpm, tpm):
        self.rpm = TokenBucket(rpm, rpm/60)
        self.tpm = TokenBucket(tpm, tpm/60)

    def acquire(self, estimated_tokens):
        self.rpm.acquire(1)
        self.tpm.acquire(estimated_tokens)

# 사용
estimate = client.messages.count_tokens(...)
limiter.acquire(estimate.input_tokens + 1024)
response = client.messages.create(...)
```

## Speaker Notes

Rate Limiter 구현 패턴입니다.
1번 Token Bucket을 Python으로 구현합니다.
capacity는 최대 토큰 수로 burst를 허용하고 refill_rate는 초당 충전 속도입니다.
acquire 메서드에서 _refill로 시간 경과만큼 토큰을 채우고 요청 수만큼 차감합니다.
토큰이 부족하면 충전될 때까지 대기합니다.
threading.Lock으로 thread-safe하게 만듭니다.
사용은 50 RPM의 경우 capacity 10, refill_rate 50/60으로 설정합니다.
2번 Redis 기반 분산 rate limiter는 멀티 프로세스 환경에 필요합니다.
키는 user_id와 1분 단위 timestamp를 포함합니다.
incr로 카운트를 증가시키고 첫 호출에 60초 expire를 설정합니다.
3번 Token-aware Limiter는 RPM과 TPM 두 bucket을 함께 관리합니다.
acquire 시 호출 수 1개와 예상 토큰 수만큼 두 bucket에서 차감합니다.
사용은 count_tokens로 input을 사전 추정하고 예상 output을 더해 acquire합니다.
Anthropic의 RPM과 TPM 한도를 정확히 따르는 클라이언트 측 제한입니다.
