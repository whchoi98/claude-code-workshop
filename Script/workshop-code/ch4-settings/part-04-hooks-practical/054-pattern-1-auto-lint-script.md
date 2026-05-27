# Slide 54: Pattern 1 / Auto Lint - script

**Part 4: HOOKS 실전 패턴**

## Code Blocks

### auto-lint.sh

```bash
#!/bin/bash
# /opt/claude/hooks/auto-lint.sh

INPUT=$(cat)
TOOL=$(echo "$INPUT" | jq -r '.tool_name')
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Write/Edit가 아니면 종료
[ "$TOOL" != "Write" ] && [ "$TOOL" != "Edit" ] && exit 0
[ -z "$FILE" ] && exit 0

# 파일이 존재하지 않으면 종료
[ ! -f "$FILE" ] && exit 0

# 확장자 추출
EXT="${FILE##*.}"

case "$EXT" in
  js|jsx|mjs|ts|tsx)
    if command -v prettier >/dev/null; then
      prettier --write "$FILE" 2>/dev/null
    fi
    if command -v eslint >/dev/null; then
      eslint --fix "$FILE" 2>/dev/null
    fi
    ;;
  py)
    command -v black >/dev/null && black "$FILE" 2>/dev/null
    command -v ruff  >/dev/null && ruff check --fix "$FILE" 2>/dev/null
    ;;
  go)
    command -v gofmt >/dev/null && gofmt -w "$FILE" 2>/dev/null
    ;;
  rs)
    command -v rustfmt >/dev/null && rustfmt "$FILE" 2>/dev/null
    ;;
  json)
    command -v jq >/dev/null && \
      jq . "$FILE" > "${FILE}.tmp" && mv "${FILE}.tmp" "$FILE"
    ;;
esac

exit 0
```

## Speaker Notes

Pattern 1의 완성 스크립트입니다.
stdin으로 INPUT을 받고 jq로 tool_name과 file_path를 추출합니다.
Write나 Edit이 아니거나 file_path가 비어 있으면 즉시 종료합니다.
파일이 존재하지 않으면 종료합니다.
확장자를 추출해 case문으로 분기합니다.
JS, JSX, MJS, TS, TSX는 prettier로 포맷 후 eslint --fix를 실행합니다.
각 명령 앞에 command -v로 도구 존재 여부를 확인합니다.
Python은 black으로 포맷 후 ruff check --fix를 실행합니다.
Go는 gofmt -w를 실행합니다.
Rust는 rustfmt를 실행합니다.
JSON은 jq를 사용한 표준 포맷팅을 적용합니다.
2>/dev/null로 에러 출력을 모두 숨기고 항상 exit 0으로 종료합니다.
PostToolUse는 차단할 수 없으므로 항상 통과시키는 것이 옳습니다.
포맷터 실행 실패가 사용자 작업을 방해하지 않게 합니다.
