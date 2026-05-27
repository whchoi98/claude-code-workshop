# Slide 11: hooks options overview

**Part 1: settings.json 구조**

## Code Blocks

### hooks

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash|Edit|Write",
        "hooks": [{
          "type": "command",
          "command": "/opt/check.sh"
        }]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [{
          "type": "command",
          "command": "prettier --write $(jq -r '.tool_input.file_path')"
        }]
      }
    ],
    "SessionStart": [
      {
        "hooks": [{
          "type": "command",
          "command": "echo 'Session started'"
        }]
      }
    ],
    "Stop": [
      { "hooks": [{ "type": "command", "command": "/opt/cleanup.sh" }] }
    ]
  }
}
```

## Speaker Notes

hooks 옵션의 4가지 시점을 살펴봅니다.
PreToolUse는 도구 호출 직전에 실행됩니다.
matcher로 어느 도구에 적용할지 정규식으로 명시합니다.
Bash 또는 Edit 또는 Write 같은 패턴입니다.
hooks 배열에 실행할 명령을 지정합니다.
PostToolUse는 도구 호출 직후 실행됩니다.
Write 후 prettier로 자동 포맷팅 같은 작업에 적합합니다.
jq로 stdin에서 도구 입력 정보를 추출할 수 있습니다.
SessionStart는 세션 시작 시 한 번 실행됩니다.
환영 메시지나 정책 안내, 환경 초기화에 사용합니다.
Stop은 Claude의 응답 종료 시 실행됩니다.
정리 작업이나 알림 발송에 사용합니다.
Part 3과 4에서 각 시점을 자세히 다룹니다.
