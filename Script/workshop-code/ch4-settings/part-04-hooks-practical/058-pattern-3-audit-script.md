# Slide 58: Pattern 3 / Audit - script

**Part 4: HOOKS 실전 패턴**

## Code Blocks

### audit.sh

```bash
#!/bin/bash
# /opt/claude/hooks/audit.sh
# Usage: audit.sh [pre|post]

PHASE="${1:-pre}"
INPUT=$(cat)

USER=$(whoami)
HOST=$(hostname)
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)

SESSION_ID=$(echo "$INPUT" | jq -r '.session_id')
TOOL=$(echo "$INPUT" | jq -r '.tool_name')
TOOL_INPUT=$(echo "$INPUT" | jq -c '.tool_input')

# 본문은 hash만 저장 (PII 보호)
CONTENT_HASH=$(echo -n "$TOOL_INPUT" | sha256sum | awk '{print $1}')

PAYLOAD=$(cat <<EOF
{
  "timestamp": "$TS",
  "phase": "$PHASE",
  "user": "$USER",
  "host": "$HOST",
  "session_id": "$SESSION_ID",
  "tool": "$TOOL",
  "tool_input_hash": "$CONTENT_HASH",
  "app": "claude-code"
}
EOF
)

# 사내 SIEM API로 비동기 전송 (백그라운드)
{
  curl -s -X POST "${SIEM_URL:-https://siem.company.com/api/log}" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${SIEM_TOKEN}" \
    -d "$PAYLOAD" >/dev/null 2>&1
} &

exit 0
```

## Speaker Notes

Pattern 3 audit.sh 완성 스크립트입니다.
첫 인자로 pre 또는 post를 받습니다.
stdin으로 INPUT을 받고 사용자, 호스트, 타임스탬프를 수집합니다.
세션 ID, 도구 이름, 도구 입력을 jq로 추출합니다.
tool_input을 -c 옵션으로 한 줄 JSON으로 만듭니다.
중요한 점은 본문은 해시만 저장한다는 것입니다.
sha256sum으로 hash를 계산해 PII나 민감 정보 노출 위험을 줄입니다.
실제 본문은 SIEM에 가지 않고 감사 추적은 가능합니다.
PAYLOAD를 heredoc으로 구조화 JSON을 만듭니다.
timestamp, phase, user, host, session_id, tool, tool_input_hash, app 필드를 포함합니다.
curl을 백그라운드로 실행해 비동기 전송합니다.
중괄호와 amp 문법으로 백그라운드 실행되어 SIEM API 응답을 기다리지 않습니다.
사용자 경험에 영향을 주지 않으면서 모든 활동이 기록됩니다.
환경변수 SIEM_URL과 SIEM_TOKEN으로 설정을 분리합니다.
