# Slide 141: Lab 4 / 프로덕션 운영

**Part 8: RECAP & 4 LABS**

## Code Blocks

### Lab 4

```python
# production_call.py - 프로덕션 패턴 통합
import time, logging, json
import structlog
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from anthropic import Anthropic, APIConnectionError, APITimeoutError, RateLimitError

structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ],
)
logger = structlog.get_logger()

client = Anthropic(timeout=30.0)

# 1. Retry with backoff
@retry(
    retry=retry_if_exception_type((APIConnectionError, APITimeoutError, RateLimitError)),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=2, min=2, max=30),
)
def call_with_retry(prompt, user_id):
    log = logger.bind(user_id=user_id)
    log.info("call_start", prompt_len=len(prompt))
    start = time.time()

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )

        # 메트릭 기록
        duration_ms = int((time.time() - start) * 1000)
        log.info("call_success",
            model=response.model,
            stop_reason=response.stop_reason,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
            duration_ms=duration_ms,
        )

        # 비용 계산
        cost = calculate_cost(response)
        log.info("cost", usd=cost)

        # 세부 메트릭 (CloudWatch나 Datadog로)
        emit_metric("claude.duration_ms", duration_ms,
                    tags=[f"model:{response.model}"])
        emit_metric("claude.cost_usd", cost)

        return response.content[0].text

    except Exception as e:
        log.error("call_failure", error_type=type(e).__name__,
                  duration_ms=int((time.time() - start) * 1000))
        raise

# 2. 비용 계산 헬퍼
def calculate_cost(response):
    u = response.usage
    rates = {"sonnet": (3, 15), "haiku": (1, 5), "opus": (15, 75)}
    rate = next((r for k, r in rates.items() if k in response.model), rates["sonnet"])
    return (u.input_tokens * rate[0] + u.output_tokens * rate[1]) / 1e6

# 3. 사용
try:
    result = call_with_retry("Hello", user_id="user_1")
    print(result)
except Exception as e:
    print(f"Failed: {e}")

# 도전 과제
# - Circuit Breaker 추가
# - Rate Limiter 통합 (Token Bucket)
# - Redis 캐싱 (Layer 1)
# - 사용량 DB 기록
# - Prometheus 메트릭
```

## Speaker Notes

Lab 4는 프로덕션 운영 통합입니다.
약 20분 소요됩니다.
Part 6에서 배운 패턴들을 한 코드에 결합합니다.
1번 Retry with backoff는 tenacity 데코레이터로 구현합니다.
APIConnectionError, APITimeoutError, RateLimitError 3가지를 재시도합니다.
stop_after_attempt 3, wait_exponential로 지수 backoff를 적용합니다.
call_with_retry 함수에서 structlog으로 구조화 로깅을 합니다.
user_id를 bind한 log로 사용자별 추적이 가능합니다.
call_start, call_success, call_failure 이벤트로 호출 생명주기를 기록합니다.
2번 비용 계산은 calculate_cost 헬퍼로 합니다.
모델별 단가에 input과 output 토큰을 곱해 USD로 계산합니다.
3번 메트릭 emit으로 외부 시스템에 전송합니다.
emit_metric 함수가 CloudWatch나 Datadog로 메트릭을 보냅니다.
duration_ms와 cost_usd 두 가지 핵심 메트릭을 보냅니다.
tags로 모델별 분류가 가능합니다.
사용은 try except로 감싸고 성공 시 응답을 사용합니다.
도전 과제 5가지를 제시합니다.
Circuit Breaker 추가, Rate Limiter 통합, Redis 캐싱, 사용량 DB 기록, Prometheus 메트릭입니다.
시간이 남으면 이 도전 과제 중 1-2개에 도전해 보시기 바랍니다.
프로덕션 수준의 코드 패턴을 직접 경험할 수 있습니다.
