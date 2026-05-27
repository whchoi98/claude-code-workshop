# Slide 144: 비용 통제 마지막 점검

**Part 8: RECAP & 4 LABS**

## Code Blocks

### budget check

```python
# 비용 통제 통합 호출
def call_with_budget(user_id, prompt, max_cost=0.10):
    # 1. 사전 토큰 추정
    estimate = client.messages.count_tokens(
        model="claude-sonnet-4-5",
        messages=[{"role": "user", "content": prompt}],
    )
    estimated_cost = (estimate.input_tokens * 3 + 1024 * 15) / 1e6

    if estimated_cost > max_cost:
        raise Exception(f"Cost limit: {estimated_cost} > {max_cost}")

    # 2. 사용자 budget 확인
    check_user_budget(user_id)

    # 3. 호출
    response = client.messages.create(...)

    # 4. 실제 비용 기록
    record_cost(user_id, calculate_cost(response))
    return response
```

## Speaker Notes

비용 통제 마지막 점검입니다.
실수 회피 체크리스트 4가지입니다.
첫째, 모델 선택입니다.
단순 작업은 Haiku로 1배 비용, 일반은 Sonnet으로 3배, 핵심만 Opus로 15배입니다.
10배 차이를 의식하고 선택하시기 바랍니다.
둘째, 캐싱 활용입니다.
Prompt caching으로 system을 90 퍼센트 절감하고 Result 캐시로 반복 호출을 차단합니다.
셋째, max_tokens는 필요한 만큼만 명시합니다.
짧은 응답에 8000은 낭비이고 1024로도 충분합니다.
넷째, 모니터링입니다.
일일과 월간 사용량 알람, 사용자별 budget 한도를 설정합니다.
call_with_budget 함수가 종합 패턴입니다.
사전 토큰 추정으로 예상 비용을 계산합니다.
임계치 초과 시 즉시 예외를 던집니다.
사용자 budget 확인 후 호출하고 실제 비용을 기록합니다.
이 패턴으로 비용 폭증을 사전에 방지할 수 있습니다.
