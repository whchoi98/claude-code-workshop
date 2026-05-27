# Slide 75: 스트림 캐싱

**Part 4: STREAMING**

## Code Blocks

### stream + cache

```bash
# 스트림에서도 Prompt Caching 사용 가능

# 1. system prompt에 cache 적용
async with client.messages.stream(
    model="claude-sonnet-4-5",
    max_tokens=2048,
    system=[
        {
            "type": "text",
            "text": LARGE_SYSTEM_PROMPT,    # 1000+ 토큰
            "cache_control": {"type": "ephemeral"},
        },
    ],
    messages=[{"role": "user", "content": user_input}],
) as stream:
    async for text in stream.text_stream:
        print(text, end="", flush=True)

    final = await stream.get_final_message()
    # 캐시 정보도 응답에 포함
    print(f"Cache read: {final.usage.cache_read_input_tokens}")
    print(f"Cache create: {final.usage.cache_creation_input_tokens}")

# 2. 멀티 메시지 + 캐싱 + 스트림
async with client.messages.stream(
    model="claude-sonnet-4-5",
    max_tokens=2048,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": LARGE_DOCUMENT,
                    "cache_control": {"type": "ephemeral"},
                },
            ],
        },
        {"role": "assistant", "content": "..."},
        {"role": "user", "content": "Q2: ..."},
    ],
) as stream:
    async for text in stream.text_stream:
        ...

# 3. 5분 안에 같은 캐시 키 사용 시
# - 첫 호출: cache_creation_input_tokens 카운트
# - 두 번째 호출 이후: cache_read_input_tokens 카운트 (90% 절감)

# 4. TTFT 영향
# 캐시 없음: TTFT 500-800ms
# 캐시 hit: TTFT 200-300ms (약 2배 빨라짐)
# 캐시도 응답 속도에 긍정적 영향

# 5. 비용 비교 (Sonnet, 1000 토큰 시스템 프롬프트, 100회 호출)
# 캐시 없음: 1000 × 100 × $3/1M = $0.30
# 캐시 있음: $3.75/1M × 1000 (1회)
#         + $0.30/1M × 1000 × 99 = $0.034
# 절감: $0.27 (88%)
```

## Speaker Notes

스트림에서도 Prompt Caching을 사용할 수 있습니다.
1번 system prompt에 cache 적용은 일반 호출과 동일합니다.
stream 메서드에 system 배열로 전달하고 cache_control을 명시합니다.
final 메시지에서 cache_read와 cache_creation 토큰을 확인 가능합니다.
2번 멀티 메시지에 캐싱과 스트림을 결합할 수도 있습니다.
큰 문서를 user 메시지에 두고 cache_control을 명시하면 후속 질문에서 캐시 활용됩니다.
3번 5분 안에 같은 캐시 키 사용 시 첫 호출은 cache_creation, 두 번째 이후는 cache_read로 90 퍼센트 절감됩니다.
4번 TTFT 영향이 흥미롭습니다.
캐시 없으면 500에서 800 밀리초, 캐시 hit이면 200에서 300 밀리초로 약 2배 빨라집니다.
캐시는 비용뿐 아니라 응답 속도에도 긍정적 영향을 줍니다.
5번 비용 비교 예시를 봅니다.
Sonnet 모델, 1000 토큰 시스템 프롬프트, 100회 호출 시나리오입니다.
캐시 없음은 0.30달러, 캐시 있음은 0.034달러로 88 퍼센트 절감됩니다.
자주 호출되는 스트림 endpoint에 캐싱을 적용하면 비용과 사용자 경험 모두 개선됩니다.
