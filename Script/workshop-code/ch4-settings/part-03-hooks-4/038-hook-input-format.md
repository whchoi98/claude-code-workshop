# Slide 38: Hook input format

**Part 3: HOOKS 4가지 시점**

## Code Blocks

### input format

```bash
# Hook 스크립트는 stdin으로 JSON 받음

# PreToolUse 입력 예시
{
  "session_id": "ses_abc123",
  "tool_name": "Bash",
  "tool_input": {
    "command": "npm test",
    "description": "Run test suite"
  }
}

# Edit 도구 호출 시
{
  "session_id": "ses_abc123",
  "tool_name": "Edit",
  "tool_input": {
    "file_path": "/path/to/file.js",
    "old_string": "...",
    "new_string": "..."
  }
}

# 스크립트에서 파싱 (bash + jq)
#!/bin/bash
INPUT=$(cat)
TOOL=$(echo "$INPUT" | jq -r '.tool_name')
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

if [ "$TOOL" = "Bash" ] && echo "$COMMAND" | grep -q 'rm -rf'; then
  echo '{"action":"block","reason":"위험 명령"}' >&2
  exit 1
fi
exit 0
```

## Speaker Notes

Hook 입력 형식을 자세히 살펴봅니다.
Hook 스크립트는 stdin으로 JSON 데이터를 받습니다.
PreToolUse 입력 예시를 봅니다.
session_id로 어느 세션인지 구분합니다.
tool_name에 호출되는 도구 이름이 들어옵니다.
tool_input에 도구별 입력 파라미터가 객체로 들어옵니다.
Bash의 경우 command와 description이 들어옵니다.
Edit 도구의 경우 file_path, old_string, new_string이 들어옵니다.
스크립트에서 파싱하는 방법은 jq를 사용하는 것이 표준입니다.
bash 스크립트에서 INPUT 변수에 cat으로 stdin을 받습니다.
jq -r로 필드를 추출합니다.
예시처럼 Bash 도구이고 command에 rm -rf가 포함되면 차단 액션을 JSON으로 출력하고 exit 1로 종료합니다.
exit 0으로 종료하면 통과를 의미합니다.
