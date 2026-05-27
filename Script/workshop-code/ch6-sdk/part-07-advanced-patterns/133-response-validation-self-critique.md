# Slide 133: 응답 검증과 자가 비평

**Part 7: 고급 패턴**

## Code Blocks

### self critique

```python
# 시나리오: Claude의 응답을 다시 Claude로 검증해 품질 향상

# 1. Self-Critique 패턴
async def critique_and_improve(prompt: str, initial: str) -> str:
    # Step 1: 자기 검토
    critique = await client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        system="""당신은 비평 전문가입니다.
        다음 응답의 문제점을 3가지 지적하세요:
        - 사실 오류
        - 논리 결함
        - 누락된 정보""",
        messages=[{"role": "user", "content": f"""
질문: {prompt}
응답: {initial}

위 응답을 비평해 주세요."""}],
    )

    # Step 2: 비평을 반영해 개선
    improved = await client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2048,
        system="비평을 받아 응답을 개선합니다.",
        messages=[{"role": "user", "content": f"""
원 질문: {prompt}
초기 응답: {initial}
비평: {critique.content[0].text}

비평을 반영해 개선된 응답을 작성해 주세요."""}],
    )

    return improved.content[0].text

# 2. JSON 구조 검증
import jsonschema

async def call_with_json_validation(prompt, schema, max_retries=3):
    for attempt in range(max_retries):
        response = await client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": f"{prompt}\n\n다음 schema에 맞는 JSON으로만 응답:\n{schema}"
            }],
        )

        text = response.content[0].text
        try:
            data = json.loads(text)
            jsonschema.validate(data, schema)
            return data
        except (json.JSONDecodeError, jsonschema.ValidationError) as e:
            if attempt < max_retries - 1:
                # 에러 메시지를 다음 prompt에 포함
                prompt = f"이전 응답이 schema에 안 맞음: {e}\n다시 작성: {prompt}"
            else:
                raise

# 3. 사실 검증 (Tool로)
TOOLS = [{
    "name": "verify_fact",
    "description": "사실 확인이 필요한 주장을 검증",
    "input_schema": {
        "type": "object",
        "properties": {"claim": {"type": "string"}},
    },
}]

async def fact_checked_call(prompt):
    response = await client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2048,
        tools=TOOLS,
        system="확실하지 않은 사실은 verify_fact 도구를 사용해 검증하세요.",
        messages=[{"role": "user", "content": prompt}],
    )
    # Tool use cycle 진행 (Part 3 참조)
    return response

# 4. 다중 응답 합의
async def consensus_call(prompt: str, n: int = 3) -> str:
    """N번 호출 후 다수결로 결정"""
    responses = await asyncio.gather(*[
        client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            temperature=0.7,    # 다양성 위해
            messages=[{"role": "user", "content": prompt}],
        )
        for _ in range(n)
    ])

    # 분류 작업은 다수결 가능
    answers = [r.content[0].text.strip() for r in responses]
    from collections import Counter
    return Counter(answers).most_common(1)[0][0]
```

## Speaker Notes

응답 검증과 자가 비평 패턴입니다.
첫째, Self-Critique 패턴입니다.
초기 응답을 받은 후 비평 전문가로 다시 호출해 사실 오류, 논리 결함, 누락 정보 3가지 지적합니다.
비평을 반영해 개선된 응답을 다시 받습니다.
품질이 크게 향상되지만 비용은 3배가 됩니다.
중요한 응답에만 적용하시기 바랍니다.
둘째, JSON 구조 검증입니다.
call_with_json_validation에서 jsonschema로 응답을 검증합니다.
실패 시 에러 메시지를 다음 prompt에 포함시켜 재시도합니다.
Claude가 에러를 보고 자동으로 형식을 수정합니다.
셋째, 사실 검증은 Tool로 합니다.
verify_fact 도구를 정의하고 확실하지 않은 사실은 도구로 검증하라고 system에 명시합니다.
Claude가 자율적으로 의심스러운 주장에 대해 검증을 요청합니다.
넷째, 다중 응답 합의입니다.
consensus_call에서 같은 prompt를 N번 호출해 다수결로 결정합니다.
temperature 0.7로 다양성을 보장합니다.
분류나 yes/no 같은 작업에 효과적입니다.
사실의 정확성이 매우 중요한 의료나 법률 같은 도메인에서 권장됩니다.
비용은 N배지만 정확도가 크게 향상됩니다.
