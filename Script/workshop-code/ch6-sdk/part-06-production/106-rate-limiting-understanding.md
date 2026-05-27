# Slide 106: Rate Limiting 이해

**Part 6: PRODUCTION 운영**

## Code Blocks

### rate limits

```python
# Anthropic API의 Rate Limit (예시, plan에 따라 다름)

# 1. RPM (Requests Per Minute)
#    일반: 50 RPM, 기업: 4000+ RPM
# 2. TPM (Tokens Per Minute) - Input + Output 합산
#    일반: 50,000 TPM, 기업: 400,000+ TPM
# 3. 동시 요청 제한
#    일반: 5-10, 기업: 50+

# 4. 응답 헤더에서 확인
response = client.messages.create(...)
headers = response.response.headers
print("RPM-Limit:", headers.get("anthropic-ratelimit-requests-limit"))
print("RPM-Remaining:", headers.get("anthropic-ratelimit-requests-remaining"))
print("Reset:", headers.get("anthropic-ratelimit-requests-reset"))
print("TPM-Limit:", headers.get("anthropic-ratelimit-tokens-limit"))
print("TPM-Remaining:", headers.get("anthropic-ratelimit-tokens-remaining"))

# 5. Rate limit 도달 시 처리
try:
    response = client.messages.create(...)
except RateLimitError as e:
    retry_after = int(e.response.headers.get("retry-after", "60"))
    print(f"Rate limited. Wait {retry_after}s")
    time.sleep(retry_after)
    response = client.messages.create(...)   # 재시도

# 6. 사전 모니터링 패턴
def check_rate_limit(response):
    h = response.response.headers
    remaining = int(h.get("anthropic-ratelimit-requests-remaining", 0))
    limit = int(h.get("anthropic-ratelimit-requests-limit", 1))
    ratio = remaining / limit if limit > 0 else 0

    if ratio < 0.1:    # 10% 미만 남음
        logger.warning(f"Rate limit close: {remaining}/{limit}")
        # 잠시 throttle 또는 다른 모델로 분산

# 7. 클라이언트 측 사전 제한 (다음 슬라이드에서)
# - 서버 한도 도달 전에 미리 throttle
# - 사용자 경험 개선 (429 안 만남)
# - 비용 통제
```

## Speaker Notes

Anthropic API의 Rate Limit 이해입니다.
API에는 3가지 주요 한도가 있습니다.
RPM은 분당 호출 수로 일반 50, 기업 4000+입니다.
TPM은 분당 토큰 수로 일반 5만, 기업 40만+입니다.
동시 요청은 일반 5-10, 기업 50+입니다.
응답 헤더에서 현재 사용량을 확인할 수 있습니다.
anthropic-ratelimit-requests-limit, remaining, reset 헤더로 RPM 정보를 봅니다.
tokens 관련 헤더도 함께 있습니다.
Rate limit 도달 시 HTTP 429 응답이 옵니다.
retry-after 헤더에 대기 시간이 초 단위로 명시됩니다.
exponential backoff와 결합해 처리합니다.
사전 모니터링 패턴이 중요합니다.
check_rate_limit 함수에서 remaining과 limit의 비율을 확인해 10 퍼센트 미만 남았을 때 경고를 발생시키고 throttle합니다.
다음 슬라이드에서 클라이언트 측 사전 제한 구현을 다룹니다.
