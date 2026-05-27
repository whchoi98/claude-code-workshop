# Slide 94: MCP 캐싱 결합

**Part 5: MCP SDK 통합**

## Code Blocks

### MCP cache

```python
# 시나리오: 같은 system prompt + MCP 조합을 반복 호출
# system prompt에 cache_control 적용해 비용 절감

# 1. 캐시 적용 패턴
response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=2048,
    mcp_servers=[{
        "type": "url",
        "url": "https://mcp.github.com/mcp",
        "name": "github",
        "authorization_token": GH_TOKEN,
    }],
    system=[
        {
            "type": "text",
            "text": LARGE_SYSTEM_PROMPT,    # 2000+ 토큰
            "cache_control": {"type": "ephemeral"},
        }
    ],
    messages=[{"role": "user", "content": prompt}],
    betas=["mcp-client-2025-04-04"],
)

# 2. 5분 안에 같은 system으로 다시 호출
# 두 번째부터 cache_read_input_tokens 카운트 (90% 절감)

# 3. 비용 시뮬레이션
# 시나리오: GitHub MCP + 큰 system prompt + 100회 호출
# - System prompt: 2000 토큰
# - User prompt: 평균 100 토큰
# - 응답: 평균 500 토큰
# - MCP 도구 호출: 평균 3회 (호출당 ~500 토큰)

# 캐시 없음 (100회 호출)
# Input: (2000 + 100) * 100 = 210,000 토큰
# Output + MCP: ~150,000 토큰
# 비용 (Sonnet): 210k * 3/1M + 150k * 15/1M = $2.88

# 캐시 있음 (100회 호출)
# Cache creation (첫 호출): 2000 * 3.75/1M = $0.0075
# Cache read (99회): 2000 * 99 * 0.3/1M = $0.0594
# 일반 input (100회 user): 100 * 100 * 3/1M = $0.030
# Output + MCP: 150,000 * 15/1M = $2.25
# 총합: $2.35
# 절감: $0.53 (18%)

# 4. cache_control이 효과적인 경우
# - 동일한 system prompt를 자주 사용
# - 동일한 큰 컨텍스트를 반복 분석
# - 같은 MCP 서버 세트로 여러 작업

# 5. cache 적용 전략
SYSTEM_PROMPTS = {
    "code_reviewer": (LARGE_REVIEWER_PROMPT, True),    # 캐시
    "translator":    (LARGE_TRANSLATOR_PROMPT, True),  # 캐시
    "summarizer":    ("간단한 요약", False),            # 너무 짧음
}

def make_call(role, user_prompt, mcp_servers):
    prompt, use_cache = SYSTEM_PROMPTS[role]
    system = [{"type": "text", "text": prompt}]
    if use_cache:
        system[0]["cache_control"] = {"type": "ephemeral"}

    return client.beta.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2048,
        mcp_servers=mcp_servers,
        system=system,
        messages=[{"role": "user", "content": user_prompt}],
        betas=["mcp-client-2025-04-04"],
    )
```

## Speaker Notes

MCP와 Prompt Caching을 결합해 비용을 절감합니다.
시나리오는 같은 system prompt와 MCP 조합을 반복 호출하는 경우입니다.
system prompt에 cache_control을 명시하면 일반 호출과 동일하게 작동합니다.
1번 캐시 적용 패턴은 mcp_servers와 함께 system 배열에 cache_control을 명시합니다.
2번 5분 안에 같은 system으로 다시 호출하면 cache_read_input_tokens가 카운트됩니다.
90 퍼센트 비용 절감 효과가 있습니다.
3번 비용 시뮬레이션이 인상적입니다.
GitHub MCP에 2000 토큰 system prompt, 100회 호출 시나리오입니다.
캐시 없으면 2.88달러, 캐시 있으면 2.35달러로 18 퍼센트 절감됩니다.
MCP 도구 호출 토큰이 많아 절감률이 일반 호출보다 낮습니다.
그래도 자주 호출되는 endpoint에서는 의미 있는 절감입니다.
4번 cache_control이 효과적인 경우는 동일한 system prompt를 자주 사용하거나 동일한 큰 컨텍스트를 반복 분석하거나 같은 MCP 서버 세트로 여러 작업을 하는 경우입니다.
5번 cache 적용 전략은 SYSTEM_PROMPTS dict로 관리합니다.
역할별로 prompt 텍스트와 캐시 여부를 함께 정의합니다.
make_call 함수에서 use_cache에 따라 동적으로 cache_control을 명시합니다.
짧은 프롬프트는 캐시 오버헤드가 절감을 초과하므로 캐시하지 않습니다.
