# Slide 26: max_tokens와 stop_reason

**Part 2: MESSAGES API 심화**

## Code Blocks

### max_tokens

```bash
# 1. max_tokens 의미
# - 모델이 생성할 최대 토큰 수 (응답만, 입력은 별도)
# - 도달하면 응답이 잘릴 수 있음
# - 모델별 최대값:
#   - claude-sonnet-4-5: 64000
#   - claude-opus-4-5: 32000
#   - claude-haiku-4-5: 8192

# 2. stop_reason 종류
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=100,
    messages=[{"role": "user", "content": "긴 응답 생성"}],
)

print(response.stop_reason)
# "end_turn"       - 모델이 자연스럽게 응답을 마침
# "max_tokens"     - max_tokens에 도달해 잘림
# "stop_sequence"  - stop_sequences 매칭
# "tool_use"       - tool_use 블록 생성

# 3. max_tokens 적용 패턴
# 짧은 응답 강제 (분류, yes/no)
client.messages.create(max_tokens=10, ...)

# 일반 응답
client.messages.create(max_tokens=1024, ...)

# 긴 생성 (보고서, 코드)
client.messages.create(max_tokens=8000, ...)

# 4. 잘린 응답 처리
if response.stop_reason == "max_tokens":
    # 옵션 A: max_tokens 늘려 재시도
    # 옵션 B: 이어서 응답 받기
    messages.append({"role": "assistant", "content": response.content})
    messages.append({"role": "user", "content": "계속해 주세요"})
    response2 = client.messages.create(messages=messages, ...)

# 5. 비용 영향
# - max_tokens는 비용에 직접 영향 (output token은 비쌈)
# - Sonnet 출력: $15/1M tokens
# - 1024 tokens = $0.015 (호출당)
# - 8000 tokens = $0.12 (8배 비싸짐)
```

## Speaker Notes

max_tokens와 stop_reason입니다.
1번 max_tokens의 의미는 모델이 생성할 최대 토큰 수입니다.
응답에만 적용되고 입력 토큰은 별도입니다.
도달하면 응답이 잘릴 수 있습니다.
모델별 최대값이 다릅니다.
Sonnet 4.5는 64000, Opus는 32000, Haiku는 8192입니다.
2번 stop_reason은 4가지입니다.
end_turn은 모델이 자연스럽게 응답을 마친 경우입니다.
max_tokens는 한도에 도달해 잘린 경우입니다.
stop_sequence는 stop_sequences 매칭, tool_use는 도구 호출 블록 생성입니다.
3번 max_tokens 적용 패턴은 용도별로 다릅니다.
분류나 yes/no 같은 짧은 응답은 10, 일반은 1024, 긴 생성은 8000이 권장입니다.
4번 잘린 응답 처리는 두 가지 옵션이 있습니다.
max_tokens를 늘려 재시도하거나 user 메시지 계속해 주세요를 추가해 이어서 응답을 받습니다.
5번 비용 영향이 중요합니다.
Sonnet 출력은 1M 토큰당 15달러이고 1024 토큰은 0.015달러, 8000 토큰은 0.12달러로 8배 비쌉니다.
불필요하게 큰 값으로 두지 마시기 바랍니다.
