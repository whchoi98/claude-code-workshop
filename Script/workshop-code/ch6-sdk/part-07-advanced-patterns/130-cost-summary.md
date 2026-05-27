# Slide 130: 비용 최적화 종합

**Part 7: 고급 패턴**

## Code Blocks

### batch API

```bash
# 핵심 원리
# 1. 가장 적합한 모델 선택
# 2. 같은 컨텍스트는 캐시
# 3. 입력과 출력을 모두 최소화
# 4. 묶을 수 있으면 배치

# Batch API 예시 (50% 할인)
batch = client.messages.batches.create(
    requests=[
        {"custom_id": f"task-{i}",
         "params": {"model": "claude-haiku-4-5", "max_tokens": 1024,
                    "messages": [{"role": "user", "content": prompts[i]}]}}
        for i in range(100)
    ]
)
# 24시간 안에 완료, 비용 50%
```

## Speaker Notes

비용 최적화 종합 7가지 전략입니다.
첫째, 모델 적합으로 단순 작업은 Haiku를 사용하면 Opus 대비 75배 절감 가능합니다.
둘째, Prompt caching으로 시스템 프롬프트를 5분 캐시하면 90 퍼센트 절감입니다.
셋째, Result 캐시로 정확히 같은 호출은 Redis에서 즉시 응답하면 30에서 50 퍼센트 hit이 가능합니다.
넷째, Semantic 캐시로 의미 유사 매칭하면 20에서 40 퍼센트 추가 hit입니다.
다섯째, max_tokens 최적화로 불필요하게 큰 한도를 줄이면 출력 토큰을 20에서 50 퍼센트 절감합니다.
여섯째, 컨텍스트 압축으로 큰 입력을 요약하거나 청크 분할하면 30에서 70 퍼센트 절감 가능합니다.
일곱째, 배치 처리는 Batch API를 사용하면 50 퍼센트 할인입니다.
핵심 원리 4가지를 정리합니다.
가장 적합한 모델 선택, 같은 컨텍스트는 캐시, 입력과 출력 모두 최소화, 묶을 수 있으면 배치입니다.
Batch API 예시를 봅니다.
batches.create로 100개 요청을 한 번에 제출합니다.
24시간 안에 완료되고 비용은 50 퍼센트입니다.
실시간성이 필요 없는 분류, 라벨링, 요약 같은 작업에 매우 효과적입니다.
7가지 전략을 모두 적용하면 같은 작업에서 비용을 10분의 1 수준까지 줄일 수 있습니다.
