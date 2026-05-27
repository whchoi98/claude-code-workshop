# Slide 56: Pattern 2 / DLP - script

**Part 4: HOOKS 실전 패턴**

## Code Blocks

### dlp.sh

```bash
#!/bin/bash
# /opt/claude/hooks/dlp.sh

INPUT=$(cat)
TOOL=$(echo "$INPUT" | jq -r '.tool_name')

# 검사 대상 콘텐츠 추출
case "$TOOL" in
  Bash)
    CONTENT=$(echo "$INPUT" | jq -r '.tool_input.command') ;;
  Write)
    CONTENT=$(echo "$INPUT" | jq -r '.tool_input.content') ;;
  Edit)
    CONTENT=$(echo "$INPUT" | jq -r '.tool_input.new_string') ;;
  MultiEdit)
    CONTENT=$(echo "$INPUT" | jq -r '.tool_input.edits[].new_string') ;;
  *)
    exit 0 ;;
esac

# 패턴 검사 함수
check_pattern() {
  local pattern="$1"
  local reason="$2"
  if echo "$CONTENT" | grep -qE "$pattern"; then
    echo "{\"action\":\"block\",\"reason\":\"$reason\"}" >&2
    exit 1
  fi
}

# 민감 패턴 검사
check_pattern 'AKIA[0-9A-Z]{16}'             'AWS Access Key 감지'
check_pattern 'aws_secret_access_key.*=.*[A-Za-z0-9/+]{40}' 'AWS Secret'
check_pattern 'BEGIN .* PRIVATE KEY'          'SSH/RSA Private Key 감지'
check_pattern 'sk-[a-zA-Z0-9]{32,}'           'API Key 패턴 감지'
check_pattern 'postgres://[^@]+@'             'DB 연결 문자열 감지'
check_pattern 'mongodb\+srv://[^@]+@'         'MongoDB 연결 감지'
check_pattern 'ghp_[a-zA-Z0-9]{36,}'          'GitHub Token 감지'

exit 0
```

## Speaker Notes

Pattern 2의 완성 스크립트입니다.
도구별로 검사 대상 콘텐츠 추출 방식이 다릅니다.
Bash는 command 필드, Write는 content 필드, Edit은 new_string 필드를 추출합니다.
MultiEdit은 edits 배열의 new_string을 모두 추출합니다.
검사 함수를 정의합니다.
check_pattern 함수는 정규식 패턴과 차단 이유를 받습니다.
grep -qE로 콘텐츠에 패턴이 있는지 확인하고 발견되면 block 액션 JSON을 stderr로 출력하고 exit 1로 종료합니다.
검사하는 주요 패턴 7가지를 봅니다.
AKIA로 시작하는 AWS Access Key, aws_secret_access_key 형식의 AWS Secret, BEGIN PRIVATE KEY 형식의 SSH Key, sk-로 시작하는 API Key, postgres와 mongodb 연결 문자열, ghp_로 시작하는 GitHub Token입니다.
모든 검사를 통과하면 exit 0으로 종료해 도구 호출을 허용합니다.
