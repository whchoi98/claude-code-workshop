# Slide 51: 도구 응답 캐싱

**Part 3: TOOL USE**

## Code Blocks

### tool caching

```python
# 시나리오: 같은 도구 호출이 자주 반복됨

# 1. 단순 함수 캐싱 (Python)
from functools import lru_cache

@lru_cache(maxsize=128)
def get_weather(location: str, unit: str = "celsius"):
    # 실제 API 호출 (비싼 작업)
    return fetch_weather_from_api(location, unit)

# 2. TTL 캐시 (cachetools)
from cachetools import TTLCache

weather_cache = TTLCache(maxsize=100, ttl=600)  # 10분 캐시

def get_weather(location, unit="celsius"):
    key = (location, unit)
    if key not in weather_cache:
        weather_cache[key] = fetch_weather_from_api(location, unit)
    return weather_cache[key]

# 3. Redis 분산 캐시
import redis
import json
r = redis.Redis()

def get_weather(location, unit="celsius"):
    key = f"weather:{location}:{unit}"
    cached = r.get(key)
    if cached:
        return json.loads(cached)
    data = fetch_weather_from_api(location, unit)
    r.setex(key, 600, json.dumps(data))   # 10분 TTL
    return data

# 4. tool_result에 caching control
# Claude의 prompt caching과 결합
{
    "type": "tool_result",
    "tool_use_id": "...",
    "content": [
        {"type": "text", "text": large_result,
         "cache_control": {"type": "ephemeral"}},
    ],
}
# 다음 호출 시 같은 결과는 캐시에서 읽음

# 5. 캐시 효과 측정
import time

def measure_tool_call(name, func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    elapsed = time.time() - start
    print(f"{name}: {elapsed*1000:.0f}ms")
    return result

# 첫 호출: 200ms (API)
# 두 번째: 0.1ms (cache)
```

## Speaker Notes

도구 응답 캐싱으로 반복 호출 비용을 절감합니다.
1번 functools.lru_cache는 가장 단순한 메모리 캐시입니다.
데코레이터 한 줄로 자동 캐싱됩니다.
maxsize 128 정도가 일반적입니다.
2번 cachetools의 TTLCache는 시간 기반 만료를 제공합니다.
10분 ttl로 두면 그 시간 후 자동 갱신됩니다.
3번 Redis 분산 캐시는 멀티 프로세스 환경에 필수입니다.
key 생성 시 위치와 단위 같은 모든 입력 인자를 포함시켜 충돌을 방지합니다.
setex로 TTL과 함께 저장합니다.
4번 tool_result에 cache_control을 명시할 수도 있습니다.
Claude의 prompt caching과 결합해 큰 도구 결과를 캐시합니다.
다음 호출 시 같은 결과를 캐시에서 읽어 토큰 비용을 절감합니다.
5번 캐시 효과 측정으로 실제 절감을 확인합니다.
measure_tool_call 함수로 시간을 측정합니다.
첫 호출은 200밀리초 정도 걸리지만 두 번째부터 0.1밀리초로 1000배 빠릅니다.
비용도 외부 API 호출이 없으니 절감됩니다.
