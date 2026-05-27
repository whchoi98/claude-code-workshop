# Slide 61: Pattern 5 / Auto Format combined

**Part 4: HOOKS 실전 패턴**

## Code Blocks

### auto-format-pro

```bash
#!/bin/bash
# /opt/claude/hooks/auto-format-pro.sh
# 사내 표준 도구 강제 + 다양한 언어 지원

INPUT=$(cat)
TOOL=$(echo "$INPUT" | jq -r '.tool_name')
[ "$TOOL" != "Write" ] && [ "$TOOL" != "Edit" ] && \
  [ "$TOOL" != "MultiEdit" ] && exit 0

FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
[ -z "$FILE" ] || [ ! -f "$FILE" ] && exit 0

# 사내 표준 도구 경로 (PATH 우회)
COMPANY_BIN="/opt/company/bin"

# 프로젝트 root 찾기 (config 파일 우선)
ROOT=$(cd "$(dirname "$FILE")" && \
  while [ ! -f .prettierrc ] && [ ! -f pyproject.toml ] && \
        [ "$PWD" != "/" ]; do
    cd ..
  done && pwd)

EXT="${FILE##*.}"
case "$EXT" in
  js|jsx|mjs|cjs|ts|tsx)
    (cd "$ROOT" && "$COMPANY_BIN/prettier" --write "$FILE")
    (cd "$ROOT" && "$COMPANY_BIN/eslint" --fix "$FILE")
    ;;
  py)
    (cd "$ROOT" && "$COMPANY_BIN/black" "$FILE")
    (cd "$ROOT" && "$COMPANY_BIN/ruff" check --fix "$FILE")
    ;;
  go)  gofmt -w "$FILE" ;;
  rs)  rustfmt --edition 2021 "$FILE" ;;
  java) "$COMPANY_BIN/google-java-format" -i "$FILE" ;;
  sql) "$COMPANY_BIN/sqlfluff" fix --dialect postgres "$FILE" ;;
esac

exit 0
```

## Speaker Notes

Pattern 5 Auto Format 완전판입니다.
사내 표준 도구 강제와 다양한 언어 지원을 결합합니다.
Write, Edit, MultiEdit 호출 후만 처리합니다.
사내 표준 도구 경로를 /opt/company/bin으로 강제 지정합니다.
PATH에 다른 버전이 있어도 사내 표준만 사용됩니다.
프로젝트 root를 찾는 로직이 추가되었습니다.
파일 디렉토리에서 시작해 상위로 올라가며 .prettierrc나 pyproject.toml 같은 config 파일을 찾습니다.
config 파일이 있는 디렉토리가 프로젝트 root입니다.
포맷터를 그 root에서 실행해 config 자동 적용을 보장합니다.
언어별 처리는 풍부합니다.
JS, TS 변형들은 prettier와 eslint를 모두 적용합니다.
Python은 black과 ruff를 적용합니다.
Go, Rust, Java, SQL까지 지원합니다.
실무에서 그대로 사용할 수 있는 완성도입니다.
