# Slide 128: 캐싱 전략 종합

**Part 7: 고급 패턴**

## Code Blocks

### layered cache

```python
# 3-Layer 캐싱으로 비용과 응답 시간 최소화

# Layer 1: 정확히 같은 prompt -> 즉시 응답 (Redis)
import hashlib, redis, json
r = redis.Redis()

def get_result_cache(prompt: str, model: str):
    key = f"result:{hashlib.sha256((prompt+model).encode()).hexdigest()}"
    cached = r.get(key)
    return json.loads(cached) if cached else None

def set_result_cache(prompt, model, response, ttl=3600):
    key = f"result:{hashlib.sha256((prompt+model).encode()).hexdigest()}"
    r.setex(key, ttl, json.dumps({
        "text": response.content[0].text,
        "tokens": response.usage.output_tokens,
    }))

# Layer 2: 의미 유사 prompt -> 임베딩 기반 매칭 (다음 슬라이드)

# Layer 3: Prompt caching (Anthropic 기능)
client.messages.create(
    system=[{"type": "text", "text": LARGE_SYSTEM,
             "cache_control": {"type": "ephemeral"}}],
    ...
)

# 통합 호출
def smart_call(prompt: str, model: str = "claude-sonnet-4-5"):
    # Layer 1: 정확 매칭
    cached = get_result_cache(prompt, model)
    if cached:
        log_cache_hit("L1_exact")
        return cached["text"]

    # Layer 2: semantic 검색 (생략)
    # similar = semantic_search(prompt)
    # if similar.score > 0.95: return similar.result

    # Layer 3: Anthropic prompt caching이 적용된 호출
    response = client.messages.create(
        model=model,
        max_tokens=1024,
        system=[{"type": "text", "text": SYSTEM_PROMPT,
                 "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": prompt}],
    )

    # Layer 1 캐시 저장
    set_result_cache(prompt, model, response)

    return response.content[0].text
```

## Speaker Notes

캐싱 전략 종합 3-Layer 캐싱입니다.
Layer 1은 Result 캐시입니다.
정확히 같은 prompt에 대해 Redis로 즉시 응답합니다.
SHA256 해시를 키로 사용해 prompt와 model 조합을 식별합니다.
TTL은 1시간 정도가 일반적입니다.
Layer 2는 Semantic 캐시입니다.
의미 유사한 prompt를 임베딩 기반으로 매칭합니다.
다음 슬라이드에서 상세히 다룹니다.
Layer 3는 Prompt 캐시입니다.
Anthropic의 cache_control 기능을 활용합니다.
시스템 프롬프트나 큰 컨텍스트를 5분 캐시해 90 퍼센트 비용 절감합니다.
통합 호출 함수 smart_call에서 3-Layer를 순차 적용합니다.
먼저 Layer 1 정확 매칭을 확인합니다.
hit이면 즉시 반환하고 cache hit 로그를 남깁니다.
miss면 Layer 2 semantic 검색을 시도합니다.
0.95 이상 유사도면 캐시된 결과를 사용합니다.
모두 miss면 Layer 3 prompt caching이 적용된 실제 호출을 합니다.
응답을 Layer 1 캐시에 저장해 다음 동일 호출은 즉시 응답합니다.
실무에서 L1 hit rate가 30 퍼센트 정도이면 비용을 크게 줄일 수 있습니다.
