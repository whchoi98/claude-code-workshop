# Slide 22: 메시지 형식과 role

**Part 2: MESSAGES API 심화**

## Code Blocks

### message format

```bash
# 1. 기본 메시지 구조
messages = [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi there!"},
    {"role": "user", "content": "What's the weather?"},
]

client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=messages,
)

# 2. role 규칙
# - 첫 메시지는 반드시 "user"
# - role은 user와 assistant가 번갈아야 함
# - 마지막은 "user"여야 응답을 받을 수 있음
# - "system" 역할은 없음 (별도 system 매개변수)

# 3. content는 string 또는 ContentBlock 배열
# 단순한 경우
{"role": "user", "content": "Hello"}

# 복잡한 경우 (이미지나 도구 결과 포함)
{
    "role": "user",
    "content": [
        {"type": "text", "text": "이 이미지 분석"},
        {"type": "image", "source": {...}},
    ]
}

# 4. assistant 응답을 messages에 추가
response = client.messages.create(messages=messages, ...)
messages.append({
    "role": "assistant",
    "content": response.content,    # ContentBlock 배열
})

# 5. assistant 미리 시작 (prefill)
messages = [
    {"role": "user", "content": "JSON으로 응답"},
    {"role": "assistant", "content": "{"},    # 응답을 { 로 시작
]
# Claude가 { 다음부터 이어 응답해 JSON 보장
```

## Speaker Notes

메시지 형식과 role의 규칙입니다.
1번 기본 메시지 구조는 role과 content를 가진 dict의 list입니다.
user와 assistant가 번갈아 등장합니다.
2번 role 규칙이 엄격합니다.
첫 메시지는 반드시 user여야 합니다.
role은 user와 assistant가 번갈아야 합니다.
마지막은 user여야 응답을 받을 수 있습니다.
system 역할은 messages 안에 없고 별도 system 매개변수를 사용합니다.
3번 content는 string 또는 ContentBlock 배열입니다.
단순 텍스트는 string으로 충분합니다.
복잡한 경우 type별 객체의 배열로 작성합니다.
이미지나 도구 결과를 포함할 때 필요합니다.
4번 assistant 응답을 messages에 추가해 대화를 이어갑니다.
response.content가 ContentBlock 배열이므로 그대로 추가합니다.
5번 assistant 미리 시작은 prefill 패턴입니다.
응답을 중괄호로 시작하면 Claude가 그 다음부터 이어 응답해 JSON 형식이 보장됩니다.
구조화 응답을 강제하는 강력한 패턴입니다.
