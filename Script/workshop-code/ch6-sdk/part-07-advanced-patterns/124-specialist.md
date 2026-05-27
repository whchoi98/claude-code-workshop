# Slide 124: Specialist 분리

**Part 7: 고급 패턴**

## Code Blocks

### specialists

```python
# specialists.py - 전문 분야별 에이전트
import asyncio
from anthropic import AsyncAnthropic
client = AsyncAnthropic()

# 1. 각 전문가 정의
SPECIALISTS = {
    "security": {
        "model": "claude-sonnet-4-5",
        "system": """당신은 시니어 보안 엔지니어입니다.
        OWASP Top 10, CWE, 보안 베스트 프랙티스 전문가.
        코드의 보안 취약점만 분석합니다.""",
    },
    "performance": {
        "model": "claude-sonnet-4-5",
        "system": """당신은 성능 최적화 전문가입니다.
        시간 복잡도, 메모리 사용, 캐싱, DB 쿼리 최적화 전문.
        코드의 성능 문제만 분석합니다.""",
    },
    "code_quality": {
        "model": "claude-sonnet-4-5",
        "system": """당신은 코드 품질 전문가입니다.
        SOLID 원칙, 리팩토링, 가독성, 유지보수성 전문.
        코드의 품질 문제만 분석합니다.""",
    },
    "testing": {
        "model": "claude-sonnet-4-5",
        "system": """당신은 테스트 전문가입니다.
        단위 테스트, 통합 테스트, 엣지 케이스, 커버리지 전문.
        테스트 누락과 개선점만 분석합니다.""",
    },
}

# 2. 전문가 호출
async def call_specialist(name: str, code: str) -> dict:
    spec = SPECIALISTS[name]
    response = await client.messages.create(
        model=spec["model"],
        max_tokens=1024,
        system=spec["system"],
        messages=[{"role": "user", "content": f"코드 분석:\n{code}"}],
    )
    return {
        "specialist": name,
        "analysis": response.content[0].text,
        "tokens": response.usage.output_tokens,
    }

# 3. 병렬 호출
async def comprehensive_review(code: str) -> dict:
    results = await asyncio.gather(*[
        call_specialist(name, code) for name in SPECIALISTS
    ])

    return {
        spec["specialist"]: spec["analysis"]
        for spec in results
    }

# 사용
review = asyncio.run(comprehensive_review(open("app.py").read()))
print("=== Security ===")
print(review["security"])
print("=== Performance ===")
print(review["performance"])

# 4. Aggregator로 최종 결합
async def final_summary(reviews: dict) -> str:
    response = await client.messages.create(
        model="claude-opus-4-5",     # 종합은 Opus
        max_tokens=2048,
        system="여러 전문가의 분석을 받아 우선순위가 있는 종합 결론을 작성합니다.",
        messages=[{"role": "user", "content": json.dumps(reviews, ensure_ascii=False)}],
    )
    return response.content[0].text
```

## Speaker Notes

Specialist 분리 패턴입니다.
각자 전문 분야가 있는 에이전트들을 정의합니다.
SPECIALISTS dict에 4개 전문가를 정의합니다.
security는 OWASP와 CWE 전문가, performance는 시간 복잡도와 메모리 전문가, code_quality는 SOLID와 리팩토링 전문가, testing은 단위 테스트와 엣지 케이스 전문가입니다.
각 전문가의 system prompt는 자기 분야에만 집중하도록 명시합니다.
call_specialist 함수에서 이름으로 전문가를 호출합니다.
결과는 specialist 이름, 분석 내용, 토큰 사용량을 포함합니다.
comprehensive_review에서 모든 전문가를 병렬 호출합니다.
asyncio.gather로 4개 전문가가 동시에 분석합니다.
총 응답 시간이 가장 느린 한 명의 시간만 걸립니다.
security와 performance, code_quality, testing 각각의 분석이 한 번에 옵니다.
final_summary는 Aggregator로 Opus 모델을 사용합니다.
여러 전문가의 분석을 받아 우선순위가 있는 종합 결론을 작성합니다.
Opus의 추론 능력으로 분야 간 의존성을 고려한 종합이 가능합니다.
이 패턴으로 한 모델로는 어려운 깊이있는 다각도 분석이 가능합니다.
