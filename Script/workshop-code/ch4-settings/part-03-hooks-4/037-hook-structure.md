# Slide 37: Hook structure

**Part 3: HOOKS 4가지 시점**

## Code Blocks

### Hook structure

```bash
# 일반 구조
{
  "hooks": {
    "<hook-type>": [
      {
        "matcher": "<pattern>",       // 어느 도구에 적용
        "hooks": [
          {
            "type": "command",
            "command": "<script-path>",
            "timeout": 5000             // 옵션: ms 단위
          }
        ]
      }
    ]
  }
}

# 실제 예시
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash|Edit|Write",   // 정규식
        "hooks": [
          {
            "type": "command",
            "command": "/opt/claude/dlp-check.sh",
            "timeout": 3000
          }
        ]
      }
    ]
  }
}

# matcher 예시
# "Bash"           - Bash 도구만
# "Bash|Edit"      - Bash 또는 Edit
# ".*"             - 모든 도구
# "Write"          - Write만
```

## Speaker Notes

Hook의 일반 구조를 살펴봅니다.
hooks 객체 안에 hook-type 키로 PreToolUse, PostToolUse 같은 시점을 명시합니다.
각 시점은 배열이며 여러 hook 객체를 가질 수 있습니다.
matcher 필드는 어느 도구에 적용할지 정규식으로 명시합니다.
hooks 배열에 실제 실행할 명령들을 정의합니다.
각 명령은 type, command, timeout 필드를 갖습니다.
type은 보통 command를 사용해 외부 스크립트를 실행합니다.
command는 실행할 스크립트의 절대 경로입니다.
timeout은 ms 단위 제한 시간으로 옵션입니다.
실제 예시를 봅니다.
PreToolUse에 Bash, Edit, Write 도구를 매처로 잡고 dlp-check.sh를 3초 제한으로 실행합니다.
matcher 예시도 참고합니다.
Bash만, Bash 또는 Edit, 모든 도구, Write만 같은 다양한 패턴이 가능합니다.
