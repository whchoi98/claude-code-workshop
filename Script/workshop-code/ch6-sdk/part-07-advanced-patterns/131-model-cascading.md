# Slide 131: 모델 캐스케이딩

**Part 7: 고급 패턴**

## Code Blocks

### cascading

```python
# 시나리오: 단순 작업은 Haiku, 어려운 것만 상위 모델

# 1. 신뢰도 기반 캐스케이딩
async def cascaded_call(prompt: str):
    # Step 1: Haiku로 먼저 시도
    haiku_response = await client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        system="""답변과 함께 confidence를 JSON으로 반환:
        {"answer": "...", "confidence": 0.0-1.0,
         "reasoning": "..."}""",
        messages=[{"role": "user", "content": prompt}],
    )

    result = parse_json(haiku_response.content[0].text)

    # 신뢰도 높음 -> Haiku 결과 사용
    if result["confidence"] >= 0.8:
        return result["answer"]

    # 신뢰도 낮음 -> Sonnet으로 재시도
    sonnet_response = await client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2048,
        system="이전 Haiku의 답변을 검토하고 개선:",
        messages=[
            {"role": "user", "content": f"질문: {prompt}\n\nHaiku 답변: {result}"}
        ],
    )

    sonnet_result = parse_json(sonnet_response.content[0].text)

    if sonnet_result["confidence"] >= 0.9:
        return sonnet_result["answer"]

    # 더 어려움 -> Opus
    opus_response = await client.messages.create(
        model="claude-opus-4-5",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )
    return opus_response.content[0].text

# 2. 작업 분류기 패턴 (Haiku가 분류)
async def classify_complexity(prompt: str) -> str:
    response = await client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=50,
        system="""분류: simple/medium/complex 중 하나만 응답
        simple: 사실 질문, 단순 계산
        medium: 분석, 글쓰기
        complex: 복잡한 추론, 다단계""",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text.strip().lower()

async def smart_route(prompt: str):
    complexity = await classify_complexity(prompt)
    model = {
        "simple": "claude-haiku-4-5",
        "medium": "claude-sonnet-4-5",
        "complex": "claude-opus-4-5",
    }[complexity]

    return await client.messages.create(
        model=model,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )

# 3. 비용 비교 (1000회 호출 평균)
# 전체 Sonnet: $30
# 캐스케이딩 (70% Haiku, 25% Sonnet, 5% Opus):
# 0.7*$10 + 0.25*$30 + 0.05*$150 = $7 + $7.5 + $7.5 = $22
# 약 27% 절감, 품질 유지
```

## Speaker Notes

모델 캐스케이딩은 Haiku에서 Sonnet, Opus로 점진 escalation입니다.
단순 작업은 Haiku로, 어려운 것만 상위 모델로 처리합니다.
첫째, 신뢰도 기반 캐스케이딩입니다.
Haiku에 답변과 confidence를 JSON으로 요청합니다.
confidence 0.8 이상이면 Haiku 결과를 사용합니다.
낮으면 Sonnet으로 재시도하고 이전 Haiku 답변을 컨텍스트로 제공합니다.
Sonnet도 confidence 0.9 미만이면 Opus로 escalate합니다.
둘째, 작업 분류기 패턴입니다.
Haiku로 prompt의 복잡도를 simple, medium, complex로 분류합니다.
분류 결과에 따라 적절한 모델로 라우팅합니다.
smart_route에서 분류 후 자동 라우팅합니다.
classifier는 매우 짧은 max_tokens 50이므로 비용이 거의 안 듭니다.
비용 비교 시뮬레이션을 봅니다.
1000회 호출 시 전체 Sonnet 사용은 30달러입니다.
캐스케이딩으로 70 퍼센트가 Haiku, 25 퍼센트가 Sonnet, 5 퍼센트가 Opus면 22달러로 27 퍼센트 절감됩니다.
품질은 유지되면서 비용을 크게 줄일 수 있습니다.
특히 사용자 질문의 복잡도가 다양한 챗봇에 매우 효과적입니다.
