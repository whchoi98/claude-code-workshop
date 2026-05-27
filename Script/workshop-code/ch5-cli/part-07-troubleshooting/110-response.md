# Slide 110: 응답 동작 문제

**Part 7: 디버깅과 트러블슈팅**

## Code Blocks

### response issues

```bash
# Symptom 1: 응답이 비어 있음 (.result is empty)

# 원인과 해결
$ claude -p "..." --output-format json | jq -r '.result'
# 빈 응답이면:

$ claude -p "..." --output-format json | jq '.subtype, .is_error'
# subtype이 error: 도구 실패나 권한 거부
# is_error: true: 시스템 에러

$ claude -p "..." --output-format json | jq '.num_turns'
# 0이면 모델이 응답하지 않음 (입력 문제 가능)


# Symptom 2: 결과가 이상함 (할루시네이션)

# 진단: 입력 컨텍스트 확인
$ claude --debug -p "..." 2>&1 | grep -i context
# 모델이 본 컨텍스트가 정확한가?

# 해결: 명시적 가이드 추가
$ claude -p "다음 데이터만 사용해 응답. 추측 금지:
$(cat data.json)
질문: ..."


# Symptom 3: 도구 호출 실패

$ claude --debug -p "..." 2>&1 | grep -i tool_use
$ claude --debug -p "..." 2>&1 | grep -i tool_result

# 결과 확인
{"type":"tool_result", "is_error": true, "content": "..."}
# error 내용에 단서

# 해결: 권한이나 매개변수 확인
$ claude -p "..." --allowed-tools "Read,Grep" --debug


# Symptom 4: 한도 도달 (max_turns_reached)

$ claude -p "..." --max-turns 50    # 더 많이 허용
# 또는 작업을 분할
$ S=$(claude -p "1단계" --output-format json | jq -r '.session_id')
$ claude --continue "$S" -p "2단계"
```

## Speaker Notes

응답 동작 문제 4가지를 정리합니다.
증상 1은 응답이 비어 있는 경우입니다.
result가 비었으면 subtype과 is_error를 함께 확인합니다.
subtype이 error면 도구 실패나 권한 거부, is_error true면 시스템 에러입니다.
num_turns가 0이면 모델이 응답하지 않은 것으로 입력 문제일 가능성이 높습니다.
증상 2는 결과가 이상한 할루시네이션 케이스입니다.
--debug에서 context를 grep으로 확인해 모델이 본 컨텍스트가 정확한지 봅니다.
해결은 명시적 가이드 추가로 다음 데이터만 사용하고 추측 금지를 명시합니다.
증상 3은 도구 호출 실패입니다.
tool_use와 tool_result를 추적해 어느 호출이 실패했는지 찾습니다.
is_error true 결과의 content에 에러 단서가 있습니다.
해결은 권한이나 매개변수를 확인합니다.
증상 4는 한도 도달입니다.
max_turns_reached subtype이 반환되면 --max-turns 값을 늘리거나 작업을 여러 세션으로 분할합니다.
session_id를 받아 --continue로 이어가는 패턴이 권장됩니다.
