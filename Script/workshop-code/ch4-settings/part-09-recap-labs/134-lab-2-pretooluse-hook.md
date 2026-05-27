# Slide 134: Lab 2 / PreToolUse Hook

**Part 9: RECAP & 4 LABS**

## Code Blocks

### Lab 2

```typescript
# 1. Hook 스크립트 작성
$ mkdir -p ~/.claude/hooks
$ cat > ~/.claude/hooks/my-dlp.sh <<'EOF'
#!/bin/bash
INPUT=$(cat)
TOOL=$(echo "$INPUT" | jq -r '.tool_name')

# Bash 명령 검사
if [ "$TOOL" = "Bash" ]; then
  CMD=$(echo "$INPUT" | jq -r '.tool_input.command')
  if echo "$CMD" | grep -qE 'rm -rf|chmod 777'; then
    echo '{"action":"block","reason":"위험 명령 감지"}' >&2
    exit 1
  fi
fi

# Edit/Write 콘텐츠 검사
if [ "$TOOL" = "Write" ] || [ "$TOOL" = "Edit" ]; then
  CONTENT=$(echo "$INPUT" | jq -r \
    '.tool_input.content // .tool_input.new_string')
  if echo "$CONTENT" | grep -qE 'AKIA[0-9A-Z]{16}'; then
    echo '{"action":"block","reason":"AWS Key 감지"}' >&2
    exit 1
  fi
fi
exit 0
EOF
$ chmod +x ~/.claude/hooks/my-dlp.sh

# 2. settings.json에 Hook 등록
$ cat >> ~/.claude/settings.json   # 또는 직접 편집
# hooks 필드 추가: PreToolUse matcher "Bash|Edit|Write"
# command: "~/.claude/hooks/my-dlp.sh"

# 3. 차단 검증
$ claude
> 다음을 src/aws.js에 작성해줘:
  const key = "AKIAIOSFODNN7EXAMPLE";
# 결과: Hook이 차단해야 정상

# 4. 통과 검증
> README.md에 "Hello World"를 추가해줘
# 결과: 정상 통과
```

## Speaker Notes

Lab 2는 PreToolUse Hook 구현 실습입니다.
약 25분 소요됩니다.
1단계 Hook 스크립트를 작성합니다.
~/.claude/hooks 디렉토리에 my-dlp.sh를 만듭니다.
stdin INPUT을 받고 jq로 tool_name을 추출합니다.
Bash 호출 시 rm -rf와 chmod 777 같은 위험 명령을 차단합니다.
Write와 Edit 시 AKIA로 시작하는 AWS Key 패턴을 차단합니다.
chmod +x로 실행 권한을 부여합니다.
2단계 settings.json에 Hook을 등록합니다.
PreToolUse에 matcher Bash 또는 Edit 또는 Write와 command 경로를 명시합니다.
3단계 차단 검증입니다.
Claude에게 AWS Key가 포함된 코드 작성을 요청합니다.
Hook이 차단해야 정상입니다.
4단계 통과 검증입니다.
안전한 콘텐츠 작성을 요청해 정상 통과를 확인합니다.
첫 DLP Hook을 직접 만들고 동작하는 것을 확인하는 경험을 얻습니다.
