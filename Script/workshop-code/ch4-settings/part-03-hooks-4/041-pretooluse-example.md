# Slide 41: PreToolUse example

**Part 3: HOOKS 4가지 시점**

## Code Blocks

### DLP example

```bash
#!/bin/bash
# /opt/claude/hooks/pre-tool-use-dlp.sh

INPUT=$(cat)
TOOL=$(echo "$INPUT" | jq -r '.tool_name')

# Bash 명령 검사
if [ "$TOOL" = "Bash" ]; then
  CMD=$(echo "$INPUT" | jq -r '.tool_input.command')
  
  # 위험 명령 차단
  if echo "$CMD" | grep -qE 'rm -rf|chmod 777|sudo'; then
    echo '{"action":"block","reason":"위험 명령"}' >&2
    exit 1
  fi
fi

# Write/Edit 콘텐츠 검사
if [ "$TOOL" = "Write" ] || [ "$TOOL" = "Edit" ]; then
  CONTENT=$(echo "$INPUT" | jq -r \
    '.tool_input.content // .tool_input.new_string')
  
  # AWS Key 패턴
  if echo "$CONTENT" | grep -qE 'AKIA[0-9A-Z]{16}'; then
    echo '{"action":"block","reason":"AWS Key 감지"}' >&2
    exit 1
  fi
  
  # SSH Private Key
  if echo "$CONTENT" | grep -q 'BEGIN RSA PRIVATE KEY'; then
    echo '{"action":"block","reason":"SSH key 감지"}' >&2
    exit 1
  fi
fi

exit 0
```

## Speaker Notes

PreToolUse 실전 예시 DLP 스크립트입니다.
stdin으로 INPUT을 받고 jq로 tool_name을 추출합니다.
Bash 도구 호출 시 command를 검사합니다.
rm -rf, chmod 777, sudo 패턴이 발견되면 위험 명령으로 차단합니다.
Write나 Edit 호출 시는 콘텐츠를 검사합니다.
content 필드 또는 new_string 필드를 추출합니다.
AWS Key 패턴은 AKIA로 시작하는 16자 영숫자입니다.
SSH Private Key는 BEGIN RSA PRIVATE KEY 헤더 라인으로 식별합니다.
이런 민감 정보가 발견되면 즉시 차단합니다.
패턴이 일치하지 않으면 exit 0으로 통과시킵니다.
이 스크립트를 /opt/claude/hooks 디렉토리에 두고 chmod +x로 실행 권한을 주면 됩니다.
managed-settings에 등록해 조직 전체에 강제 적용할 수 있습니다.
