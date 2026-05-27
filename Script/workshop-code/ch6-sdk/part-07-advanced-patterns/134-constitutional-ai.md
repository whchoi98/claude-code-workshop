# Slide 134: Constitutional AI 패턴

**Part 7: 고급 패턴**

## Code Blocks

### constitutional

```python
# Anthropic의 Constitutional AI 원칙을 자체 앱에 적용

# 1. 원칙 정의
CONSTITUTION = """
당신은 다음 원칙을 따릅니다:

1. 정직: 거짓 정보나 추측을 사실처럼 말하지 않음
2. 도움: 사용자의 실제 이익에 부합하는 응답
3. 안전: 위험하거나 해로운 정보 제공 금지
4. 프라이버시: 개인정보 추측이나 노출 회피
5. 균형: 단일 관점이 아닌 다양한 시각 제시
6. 명확성: 불확실한 부분은 명시
7. 한계 인정: 모르는 것은 모른다고
"""

# 2. 모든 호출에 원칙 적용
def call_with_constitution(prompt: str):
    return client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2048,
        system=[{
            "type": "text",
            "text": CONSTITUTION,
            "cache_control": {"type": "ephemeral"},  # 캐시
        }],
        messages=[{"role": "user", "content": prompt}],
    )

# 3. 응답 자가 평가
async def evaluate_against_constitution(response_text: str) -> dict:
    eval_response = await client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=512,
        system=f"""다음 응답이 이 원칙을 따르는지 평가하세요:

{CONSTITUTION}

JSON 응답: {{"adheres": bool, "violations": [str], "score": 0-10}}""",
        messages=[{"role": "user", "content": response_text}],
    )
    return parse_json(eval_response.content[0].text)

# 4. 위반 시 재작성
async def safe_call(prompt: str, max_retries: int = 2):
    for attempt in range(max_retries):
        response = call_with_constitution(prompt)
        text = response.content[0].text

        evaluation = await evaluate_against_constitution(text)
        if evaluation["adheres"]:
            return text

        # 위반 항목을 알리고 재작성
        violations = ", ".join(evaluation["violations"])
        prompt = f"""이전 응답이 원칙을 위반: {violations}
원 질문: {prompt}
다시 작성해 주세요. 원칙을 엄격히 따르세요."""

    raise Exception("Failed to produce compliant response")

# 5. 도메인별 원칙 추가
LEGAL_CONSTITUTION = CONSTITUTION + """
추가 (법률 도메인):
- 법률 조언이 아닌 정보 제공임을 명시
- 변호사 상담 권유
- 법령은 정확히 인용
"""

MEDICAL_CONSTITUTION = CONSTITUTION + """
추가 (의료 도메인):
- 진단이 아닌 일반 정보 제공
- 의료 전문가 상담 권유
- 약물 정보는 신중하게
"""

# 6. 효과
# - 일관된 응답 품질
# - 안전성 향상
# - 도메인별 맞춤 가능
# - 비용은 약간 증가 (system prompt 길이 + 검증)
```

## Speaker Notes

Constitutional AI 패턴은 원칙 기반 응답 통제입니다.
Anthropic의 핵심 접근법을 자체 앱에 적용합니다.
첫째, 원칙을 정의합니다.
CONSTITUTION에 7가지 원칙을 명시합니다.
정직, 도움, 안전, 프라이버시, 균형, 명확성, 한계 인정입니다.
둘째, 모든 호출에 원칙을 적용합니다.
call_with_constitution 함수에서 CONSTITUTION을 system으로 전달합니다.
cache_control로 system을 캐시해 비용을 절감합니다.
셋째, 응답 자가 평가입니다.
evaluate_against_constitution에서 Haiku로 응답이 원칙을 따르는지 평가합니다.
adheres boolean, violations list, score를 JSON으로 받습니다.
넷째, 위반 시 재작성입니다.
safe_call에서 평가 결과가 위반이면 위반 항목을 명시하고 재작성을 요청합니다.
최대 2회 재시도로 원칙 준수 응답을 보장합니다.
다섯째, 도메인별 원칙 추가가 가능합니다.
법률 도메인은 법률 조언이 아닌 정보 제공임을 명시, 변호사 상담 권유 같은 추가 원칙을 더합니다.
의료 도메인도 유사한 패턴입니다.
여섯째, 효과는 일관된 응답 품질, 안전성 향상, 도메인별 맞춤, 약간의 비용 증가입니다.
공공 서비스나 책임 있는 AI 사용이 필요한 곳에 매우 효과적입니다.
