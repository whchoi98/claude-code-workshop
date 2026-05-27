# Slide 43: PostToolUse example

**Part 3: HOOKS 4가지 시점**

## Code Blocks

### auto format

```bash
#!/bin/bash
# /opt/claude/hooks/post-tool-use-format.sh

INPUT=$(cat)
TOOL=$(echo "$INPUT" | jq -r '.tool_name')

# Write 또는 Edit 호출 후만 처리
if [ "$TOOL" != "Write" ] && [ "$TOOL" != "Edit" ]; then
  exit 0
fi

FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path')

# 확장자별 포맷터 선택
case "$FILE" in
  *.js|*.jsx|*.ts|*.tsx)
    if command -v prettier >/dev/null; then
      prettier --write "$FILE" 2>/dev/null
      eslint --fix "$FILE" 2>/dev/null
    fi
    ;;
  *.py)
    if command -v black >/dev/null; then
      black "$FILE" 2>/dev/null
      ruff check --fix "$FILE" 2>/dev/null
    fi
    ;;
  *.go)
    gofmt -w "$FILE" 2>/dev/null
    ;;
  *.rs)
    rustfmt "$FILE" 2>/dev/null
    ;;
esac

exit 0
```

## Speaker Notes

PostToolUse 실전 예시 자동 포맷 스크립트입니다.
Write나 Edit 호출 후에만 처리하도록 필터링합니다.
file_path를 추출해 어느 파일이 변경되었는지 파악합니다.
확장자별로 적절한 포맷터를 선택합니다.
.js, .jsx, .ts, .tsx는 prettier로 포맷 후 eslint --fix를 실행합니다.
.py 파일은 black으로 포맷 후 ruff check --fix를 실행합니다.
.go 파일은 gofmt -w를 실행합니다.
.rs 파일은 rustfmt를 실행합니다.
2>/dev/null로 에러를 숨겨 포맷터가 설치되어 있지 않거나 실패해도 무중단 진행합니다.
command -v로 도구 존재 여부를 확인해 더 안전하게 처리합니다.
이 스크립트를 PostToolUse 후크로 등록하면 Claude가 코드를 수정할 때마다 자동으로 일관된 스타일이 적용됩니다.
팀 코드 스타일 통일에 매우 효과적인 패턴입니다.
