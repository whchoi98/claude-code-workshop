# Slide 39: Hook output format

**Part 3: HOOKS 4가지 시점**

## Code Blocks

### output format

```bash
# Hook 출력은 exit code와 stderr JSON으로 결정

# 통과 (도구 호출 진행)
exit 0
# stderr에 아무것도 출력 안 함

# 차단 (도구 호출 거부)
echo '{"action":"block","reason":"위험 명령 감지"}' >&2
exit 1

# 경고만 (도구는 진행, 사용자에게 알림)
echo '{"action":"warn","message":"이 명령은 위험할 수 있습니다"}' >&2
exit 0

# 입력 변환 (PreToolUse에서 가능)
echo '{
  "action":"modify",
  "tool_input": {
    "command": "npm test -- --silent"
  }
}' >&2
exit 0

# 일반적인 패턴
case "$DECISION" in
  safe)     exit 0 ;;
  block)    echo '{"action":"block","reason":"..."}' >&2; exit 1 ;;
  warn)     echo '{"action":"warn","message":"..."}' >&2; exit 0 ;;
esac

# 비동기 외부 호출 (SIEM 전송 등)도 가능
# 단, timeout 내에 끝나야 함
```

## Speaker Notes

Hook 출력 형식을 정확히 이해해야 합니다.
exit code와 stderr JSON으로 결정됩니다.
통과는 exit 0이며 stderr에 아무것도 출력하지 않습니다.
차단은 stderr에 action block과 reason을 JSON으로 출력하고 exit 1로 종료합니다.
Claude Code가 이 결과를 받아 도구 호출을 거부합니다.
경고만 하는 경우는 action warn과 message를 JSON으로 출력하고 exit 0으로 종료합니다.
도구는 진행되지만 사용자에게 알림이 표시됩니다.
PreToolUse에서는 입력 변환도 가능합니다.
action modify와 변환된 tool_input을 JSON으로 출력하면 그 값으로 도구 호출이 진행됩니다.
예시처럼 npm test에 --silent 옵션을 자동 추가하는 식입니다.
일반적인 패턴은 case 문으로 결정 변수에 따라 분기 처리하는 것입니다.
safe, block, warn 같은 결정에 따라 적절한 출력과 exit code를 사용합니다.
비동기 외부 호출도 가능하지만 timeout 내에 끝나야 합니다.
