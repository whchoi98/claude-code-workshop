# Slide 29: 메시지 메타데이터

**Part 2: MESSAGES API 심화**

## Code Blocks

### metadata

```python
# 1. metadata 매개변수
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    metadata={
        "user_id": "user_12345",
    },
    messages=[{"role": "user", "content": "Hi"}],
)

# 2. 활용
# - 호출별 추적
# - rate limit 분리
# - 비용 attribution

# 3. user_id 베스트 프랙티스
# - 안정적인 사용자 식별자
# - 익명 ID나 hash 권장 (PII 회피)
# - 같은 사용자는 같은 ID 사용

import hashlib

def safe_user_id(email: str) -> str:
    # 이메일을 hash해서 추적용 ID로
    return hashlib.sha256(email.encode()).hexdigest()[:16]

response = client.messages.create(
    metadata={"user_id": safe_user_id("user@example.com")},
    ...
)

# 4. 자체 메타데이터 추적 (DB 기록)
import time

def call_with_tracking(user_id, request_id, prompt):
    start = time.time()

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        metadata={"user_id": user_id},
        messages=[{"role": "user", "content": prompt}],
    )

    # DB에 기록
    db.calls.insert({
        "user_id": user_id,
        "request_id": request_id,
        "model": response.model,
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
        "duration_ms": int((time.time() - start) * 1000),
        "stop_reason": response.stop_reason,
        "timestamp": time.time(),
    })
    return response

# 5. Console에서 보기
# https://console.anthropic.com/dashboard
# user_id별 토큰 사용량과 비용 확인 가능
```

## Speaker Notes

메시지 메타데이터로 호출을 추적합니다.
1번 metadata 매개변수에 user_id를 명시합니다.
2번 활용은 3가지입니다.
호출별 추적, rate limit 분리, 비용 attribution입니다.
같은 사용자의 여러 호출을 그룹화할 수 있습니다.
3번 user_id 베스트 프랙티스는 안정적인 식별자를 사용하는 것입니다.
PII 회피를 위해 익명 ID나 hash를 권장합니다.
email을 SHA256 hash로 변환해 처음 16자만 사용하는 패턴이 일반적입니다.
4번 자체 메타데이터 추적은 DB 기록 패턴입니다.
call_with_tracking 함수로 호출 전후 시간을 측정하고 토큰, 모델, stop_reason을 모두 DB에 기록합니다.
비용 분석과 사용 패턴 추적에 활용됩니다.
5번 Console에서 보기는 Anthropic Console 대시보드를 활용하는 것입니다.
user_id별 토큰 사용량과 비용을 확인할 수 있습니다.
메타데이터는 운영 시 필수 기능입니다.
