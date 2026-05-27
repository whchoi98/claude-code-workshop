# Slide 32: Prompt Caching 심화

**Part 2: MESSAGES API 심화**

## Code Blocks

### caching advanced

```python
# 1. 다중 캐시 포인트 (최대 4개)
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    system=[
        # 캐시 포인트 1: 거의 변하지 않는 역할
        {"type": "text", "text": SYSTEM_ROLE,
         "cache_control": {"type": "ephemeral"}},

        # 캐시 포인트 2: 자주 사용되는 지식
        {"type": "text", "text": COMPANY_KNOWLEDGE,
         "cache_control": {"type": "ephemeral"}},
    ],
    messages=[
        # 캐시 포인트 3: 대화 초기 컨텍스트
        {"role": "user", "content": [
            {"type": "text", "text": LONG_CONTEXT,
             "cache_control": {"type": "ephemeral"}},
        ]},
        {"role": "assistant", "content": "..."},
        # 캐시 포인트 4: 멀티턴의 중간
        {"role": "user", "content": [
            {"type": "text", "text": prior_qa,
             "cache_control": {"type": "ephemeral"}},
        ]},
        # 마지막은 동적 (캐시 안 함)
        {"role": "assistant", "content": "..."},
        {"role": "user", "content": current_question},
    ],
)

# 2. 캐시 검사 (도구 정의 캐시)
client.messages.create(
    tools=[
        {
            "name": "get_weather",
            "description": "...",
            "input_schema": {...},
            "cache_control": {"type": "ephemeral"},
        },
    ],
    ...
)

# 3. 캐시 효과 측정
def calculate_cache_savings(response):
    cache_read = response.usage.cache_read_input_tokens
    cache_create = response.usage.cache_creation_input_tokens
    regular = response.usage.input_tokens

    # Sonnet 단가
    saved = cache_read * (3.0 - 0.30) / 1e6
    cost_premium = cache_create * (3.75 - 3.0) / 1e6
    net_saved = saved - cost_premium

    return {
        "saved_usd": saved,
        "premium_usd": cost_premium,
        "net_saved_usd": net_saved,
        "hit_rate": cache_read / (cache_read + regular)
            if (cache_read + regular) > 0 else 0,
    }
```

## Speaker Notes

Prompt Caching 심화입니다.
1번 다중 캐시 포인트는 최대 4개까지 지정 가능합니다.
system에 2개, messages에 2개까지 cache_control을 명시할 수 있습니다.
계층별로 변경 빈도가 다른 부분을 분리합니다.
역할은 거의 안 변하고 지식은 일주일 단위로 변하고 컨텍스트는 더 자주 변합니다.
마지막 user 메시지는 동적이므로 캐시하지 않습니다.
2번 도구 정의도 캐시할 수 있습니다.
tools 배열의 각 도구에 cache_control을 명시합니다.
복잡한 도구 정의가 많을 때 유용합니다.
3번 캐시 효과 측정은 calculate_cache_savings 함수로 구현합니다.
cache_read와 cache_creation, 일반 input 토큰을 모두 받아 절감액과 프리미엄, 순 절감액, hit_rate를 계산합니다.
hit_rate가 70 퍼센트 이상이면 매우 효과적이고 30 퍼센트 이하면 캐시 전략을 재검토해야 합니다.
다층 캐시는 큰 RAG 시스템이나 코드 리뷰 봇 같은 반복 사용 사례에서 비용을 크게 줄입니다.
