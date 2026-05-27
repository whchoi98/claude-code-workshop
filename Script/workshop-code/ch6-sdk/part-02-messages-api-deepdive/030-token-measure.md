# Slide 30: 토큰 측정

**Part 2: MESSAGES API 심화**

## Code Blocks

### count_tokens

```python
# 1. 호출 후 토큰 (정확)
response = client.messages.create(...)
print(response.usage.input_tokens)
print(response.usage.output_tokens)

# 2. 호출 전 토큰 추정
# count_tokens API
result = client.messages.count_tokens(
    model="claude-sonnet-4-5",
    system="당신은 도우미입니다.",
    messages=[{"role": "user", "content": "Hello"}],
)
print(f"Input tokens: {result.input_tokens}")
# 실제 호출 전에 입력 토큰 수 정확히 확인

# 3. 비용 사전 추정
def estimate_cost(messages, system=None, model="claude-sonnet-4-5"):
    result = client.messages.count_tokens(
        model=model,
        system=system,
        messages=messages,
    )
    input_tokens = result.input_tokens

    # 단가 (Sonnet 기준)
    if "sonnet" in model:
        input_rate = 3.0   # $/1M
        output_rate = 15.0
    elif "haiku" in model:
        input_rate = 1.0
        output_rate = 5.0
    elif "opus" in model:
        input_rate = 15.0
        output_rate = 75.0

    # 출력은 추정 (max_tokens의 50% 가정)
    estimated_output = 1024 * 0.5
    cost = (input_tokens * input_rate +
            estimated_output * output_rate) / 1e6
    return f"~${cost:.4f} per call"

# 4. 큰 입력 사전 차단
def safe_call(messages):
    result = client.messages.count_tokens(
        model="claude-sonnet-4-5",
        messages=messages,
    )
    if result.input_tokens > 180_000:    # 200K 한계
        raise ValueError(
            f"Input too large: {result.input_tokens} tokens"
        )

    return client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=messages,
    )

# 5. 캐시 토큰 별도 추적
response = client.messages.create(...)
print(f"Input: {response.usage.input_tokens}")
print(f"Cache creation: {response.usage.cache_creation_input_tokens}")
print(f"Cache read: {response.usage.cache_read_input_tokens}")
# 합산 = 실제 input 토큰
```

## Speaker Notes

토큰 측정 방법입니다.
1번 호출 후 토큰은 response.usage로 정확히 받을 수 있습니다.
input_tokens와 output_tokens가 핵심입니다.
2번 호출 전 토큰 추정은 count_tokens API를 사용합니다.
client.messages.count_tokens로 같은 매개변수를 전달하면 input_tokens를 반환합니다.
실제 호출 전에 정확한 입력 토큰 수를 확인할 수 있습니다.
3번 비용 사전 추정에 활용합니다.
estimate_cost 함수에서 count_tokens 결과와 모델별 단가로 호출당 비용을 계산합니다.
출력은 max_tokens의 50 퍼센트로 추정합니다.
4번 큰 입력 사전 차단도 가능합니다.
200K 한계의 90 퍼센트인 180000을 초과하면 호출 전에 예외를 던집니다.
비용 폭증이나 한계 초과를 사전에 방지합니다.
5번 캐시 토큰은 별도로 추적됩니다.
cache_creation_input_tokens와 cache_read_input_tokens가 분리되어 있습니다.
합산이 실제 input 토큰이 됩니다.
prompt caching 활용 시 정확한 비용 계산에 필요합니다.
