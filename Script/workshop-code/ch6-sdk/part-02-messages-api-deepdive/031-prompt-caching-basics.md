# Slide 31: Prompt Caching 기본

**Part 2: MESSAGES API 심화**

## Code Blocks

### caching basic

```bash
# 1. Prompt Caching이란?
# - 자주 사용되는 큰 프롬프트를 캐시해 재사용
# - 캐시된 토큰은 입력 단가의 10%만 청구
# - 5분 TTL (사용 시 갱신)

# 2. 캐시 적용 예시
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": "당신은 우리 회사 코드 리뷰어입니다."
                    "다음 코딩 규칙을 따라야 합니다: ...",
            "cache_control": {"type": "ephemeral"},
        }
    ],
    messages=[{"role": "user", "content": "이 코드 리뷰"}],
)

# 3. 첫 호출 후 5분 안에 같은 시스템 프롬프트로 호출
# 두 번째부터 cache hit -> 비용 절감

response.usage.cache_creation_input_tokens   # 첫 호출
response.usage.cache_read_input_tokens       # 두 번째 이후

# 4. 비용 비교 (Sonnet 기준, 1M 토큰)
# 일반 input:        $3.00
# Cache 생성 input:  $3.75 (25% 더 비쌈, 1회만)
# Cache 읽기 input:  $0.30 (90% 절감)

# 5. 캐시 가능 영역
# - system 프롬프트
# - 멀티 메시지의 일부
# - tools 정의
# - 도구 결과

# 6. 캐시 활용 적합 사례
# - 긴 시스템 프롬프트 (>1024 토큰)
# - 자주 호출되는 RAG 컨텍스트
# - 여러 사용자가 공유하는 지식 베이스
# - 대화 초기 컨텍스트

# 7. 캐시 부적합
# - 매번 다른 프롬프트
# - 짧은 프롬프트 (오버헤드가 절감 초과)
# - 한 번만 사용하는 호출
```

## Speaker Notes

Prompt Caching은 비용을 90 퍼센트까지 절감할 수 있는 강력한 기능입니다.
1번 의미는 자주 사용되는 큰 프롬프트를 캐시해 재사용하는 것입니다.
캐시된 토큰은 입력 단가의 10 퍼센트만 청구되고 TTL은 5분이며 사용 시 갱신됩니다.
2번 캐시 적용 예시는 system을 배열 형식으로 작성하고 각 요소에 cache_control을 명시합니다.
type은 ephemeral로 5분 캐시를 의미합니다.
3번 첫 호출 후 5분 안에 같은 시스템 프롬프트로 호출하면 두 번째부터 cache hit이 발생합니다.
cache_creation_input_tokens가 첫 호출 시, cache_read_input_tokens가 두 번째 이후입니다.
4번 비용 비교를 Sonnet 기준으로 보면 명확합니다.
일반 input 3달러, Cache 생성 3.75달러로 25 퍼센트 더 비싸지만 1회만 발생합니다.
Cache 읽기는 0.30달러로 90 퍼센트 절감됩니다.
5번 캐시 가능 영역은 system 프롬프트, 멀티 메시지 일부, tools 정의, 도구 결과 4가지입니다.
6번 캐시 활용 적합 사례는 긴 시스템 프롬프트, 자주 호출되는 RAG 컨텍스트, 공유 지식 베이스, 대화 초기 컨텍스트입니다.
7번 부적합한 경우는 매번 다른 프롬프트, 짧은 프롬프트, 한 번만 사용하는 호출입니다.
