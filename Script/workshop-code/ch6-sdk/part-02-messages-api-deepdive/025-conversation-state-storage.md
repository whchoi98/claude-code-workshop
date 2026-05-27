# Slide 25: 대화 상태 보관

**Part 2: MESSAGES API 심화**

## Code Blocks

### state mgmt

```python
# 시나리오: 웹 서비스에서 사용자별 대화 유지

# 1. Redis 보관 (간단)
import json
import redis
from anthropic import Anthropic

client = Anthropic()
r = redis.Redis(host="localhost", port=6379)

def get_messages(user_id: str) -> list:
    raw = r.get(f"chat:{user_id}")
    return json.loads(raw) if raw else []

def save_messages(user_id: str, messages: list):
    r.set(f"chat:{user_id}", json.dumps(messages, default=str),
          ex=3600)    # 1시간 TTL

def chat(user_id: str, user_input: str) -> str:
    messages = get_messages(user_id)
    messages.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=messages,
    )

    # ContentBlock을 JSON 직렬화 가능 형태로
    serialized = [
        {"type": b.type, "text": b.text} if b.type == "text"
        else b.model_dump()
        for b in response.content
    ]
    messages.append({"role": "assistant", "content": serialized})

    save_messages(user_id, messages)
    return response.content[0].text

# 2. PostgreSQL 보관 (영구)
# 테이블 schema
# CREATE TABLE conversations (
#   user_id TEXT,
#   created_at TIMESTAMP,
#   messages JSONB,
#   PRIMARY KEY (user_id, created_at)
# );

# 3. 대화 길이 관리 (트리밍)
def trim_messages(messages: list, max_pairs: int = 20) -> list:
    # 최근 N개의 user/assistant 쌍만 유지
    if len(messages) > max_pairs * 2:
        return messages[-(max_pairs * 2):]
    return messages

# 4. 요약 기반 압축
def compress_old_messages(messages: list) -> list:
    if len(messages) < 40:
        return messages

    # 오래된 메시지를 요약
    old = messages[:-20]
    summary = summarize(old)
    return [
        {"role": "user", "content": f"이전 대화 요약: {summary}"},
        *messages[-20:],
    ]
```

## Speaker Notes

대화 상태 보관 패턴입니다.
1번 Redis 보관은 간단합니다.
user_id를 키로 하여 messages를 JSON으로 저장합니다.
TTL 1시간으로 자동 만료시킬 수 있습니다.
get_messages와 save_messages 함수를 만들어 재사용합니다.
chat 함수에서 호출 전후로 상태를 로드하고 저장합니다.
ContentBlock을 JSON 직렬화 가능한 형태로 변환하는 것이 중요합니다.
type과 text 같은 필드를 직접 추출하거나 model_dump를 사용합니다.
2번 PostgreSQL 보관은 영구 저장에 적합합니다.
conversations 테이블에 user_id, created_at, messages JSONB로 저장합니다.
분석과 audit이 필요할 때 유용합니다.
3번 대화 길이 관리는 트리밍 패턴입니다.
최근 N개의 user assistant 쌍만 유지해 토큰 비용을 통제합니다.
4번 요약 기반 압축은 더 정교한 방식입니다.
오래된 메시지를 Claude로 요약해서 짧은 컨텍스트로 만들고 최근 메시지와 함께 전달합니다.
중요한 정보를 잃지 않으면서 토큰을 절약할 수 있습니다.
