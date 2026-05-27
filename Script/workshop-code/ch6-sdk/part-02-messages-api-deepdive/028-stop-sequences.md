# Slide 28: stop_sequences

**Part 2: MESSAGES API 심화**

## Code Blocks

### stop_sequences

```bash
# 1. stop_sequences 의미
# - 모델이 이 문자열을 생성하면 즉시 응답 중단
# - 응답에 이 문자열은 포함되지 않음

# 2. 단일 stop sequence
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    stop_sequences=["END"],
    messages=[{
        "role": "user",
        "content": "리스트로 답하고 마지막에 END 표시"
    }],
)
# Claude가 "END"를 생성하면 즉시 중단
# response.stop_reason == "stop_sequence"
# response.stop_sequence == "END"

# 3. 다중 stop sequences
client.messages.create(
    stop_sequences=["</response>", "[STOP]", "---"],
    ...
)

# 4. JSON 응답 강제 (prefill + stop_sequence)
messages = [
    {"role": "user", "content": "JSON 객체로 응답"},
    {"role": "assistant", "content": "{"},
]
response = client.messages.create(
    messages=messages,
    stop_sequences=["}"],    # 첫 } 에서 중단
    max_tokens=500,
)
# 결과: {"key": "value"
# 결과를 { + result + } 로 결합해 완전한 JSON

# 5. 멀티턴에서 활용
# 대화 분할 마커
client.messages.create(
    stop_sequences=["사용자:", "Human:"],
    messages=[{"role": "user", "content":
        "대화 시뮬레이션. 다음 발화자가 '사용자:'로 시작하면 중단."
    }],
)

# 6. 주의사항
# - 너무 일반적인 문자열은 의도하지 않은 중단 유발
# - "the" 같은 단어는 위험
# - 명확한 구분자 사용 권장 (XML 태그, 특수 문자열)
```

## Speaker Notes

stop_sequences는 응답 중단 조건입니다.
1번 의미는 모델이 이 문자열을 생성하면 즉시 응답을 중단하는 것입니다.
응답에 이 문자열은 포함되지 않습니다.
2번 단일 stop sequence는 stop_sequences 배열에 한 요소만 둡니다.
Claude가 END를 생성하면 즉시 중단되며 stop_reason이 stop_sequence가 됩니다.
stop_sequence 필드에 어떤 문자열이 매칭됐는지 표시됩니다.
3번 다중 stop sequences로 여러 종료 조건을 둘 수 있습니다.
어느 하나라도 매칭되면 중단됩니다.
4번 JSON 응답 강제 패턴은 prefill과 stop_sequence를 결합합니다.
assistant 메시지를 중괄호로 시작하고 닫는 중괄호에서 중단합니다.
결과를 중괄호와 결과와 닫는 중괄호로 결합해 완전한 JSON을 만듭니다.
5번 멀티턴에서 활용은 대화 분할 마커로 사용합니다.
대화 시뮬레이션에서 다음 발화자 마커에 도달하면 중단합니다.
6번 주의사항이 중요합니다.
너무 일반적인 문자열은 의도하지 않은 중단을 유발합니다.
명확한 구분자나 XML 태그를 사용하시기 바랍니다.
