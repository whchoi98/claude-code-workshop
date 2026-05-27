# Slide 11: 클라이언트 구조 깊이 이해

**Part 1: SDK 기본**

## Code Blocks

### client structure

```python
# Python 클라이언트의 핵심 구조

from anthropic import Anthropic

client = Anthropic()

# 1. 주요 리소스
client.messages           # Messages API (가장 자주 사용)
client.beta              # Beta 기능
client.completions        # Legacy (사용 비권장)

# 2. messages 메서드
client.messages.create(...)   # 동기 호출
client.messages.stream(...)   # 스트리밍 (Part 4에서)

# 3. 주요 인자
client.messages.create(
    model="...",              # 필수
    messages=[...],            # 필수
    max_tokens=1024,           # 필수
    system="...",              # 선택
    temperature=0.7,           # 선택 (0.0 ~ 1.0)
    top_p=0.95,                # 선택
    stop_sequences=["END"],    # 선택
    metadata={"user_id": "u1"},# 선택 (감사용)
    tools=[...],               # 선택 (Part 3)
    tool_choice={...},         # 선택
    stream=False,              # 기본 (Part 4에서 True)
)

# 4. 응답 객체 구조
message.id              # 메시지 ID
message.role            # "assistant"
message.content         # ContentBlock 배열
message.content[0].type # "text" | "tool_use"
message.content[0].text # text 타입일 때
message.model           # 사용된 모델
message.stop_reason     # "end_turn" | "max_tokens" | "stop_sequence" | "tool_use"
message.stop_sequence   # 어떤 stop_sequence 매칭
message.usage           # 토큰 사용량
message.usage.input_tokens
message.usage.output_tokens
message.usage.cache_creation_input_tokens
message.usage.cache_read_input_tokens
```

## Speaker Notes

클라이언트의 핵심 구조를 깊이 이해합니다.
1번 주요 리소스로 client.messages, client.beta, client.completions가 있습니다.
messages가 가장 자주 사용되며 completions는 legacy로 비권장입니다.
2번 messages의 주요 메서드는 create와 stream입니다.
create는 동기 호출이고 stream은 Part 4에서 다룰 스트리밍입니다.
3번 주요 인자는 11개입니다.
model, messages, max_tokens는 필수입니다.
system으로 시스템 프롬프트를 추가합니다.
temperature는 0에서 1 사이로 창의성을 조절합니다.
stop_sequences로 특정 문자열에서 응답을 중단시킬 수 있습니다.
metadata는 user_id 같은 추적 정보를 포함합니다.
tools와 tool_choice는 Part 3 Tool Use에서 다룹니다.
stream은 기본 false이고 true면 SSE 스트림이 반환됩니다.
4번 응답 객체 구조입니다.
id, role, content, model, stop_reason, usage가 핵심 필드입니다.
content는 ContentBlock 배열로 type이 text나 tool_use 같은 종류로 분기됩니다.
stop_reason은 응답이 왜 끝났는지 알려줍니다.
usage에는 input과 output 토큰뿐 아니라 캐시 관련 토큰도 포함됩니다.
