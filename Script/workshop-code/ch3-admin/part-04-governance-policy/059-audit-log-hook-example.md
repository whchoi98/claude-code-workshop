# Slide 59: Audit log hook example

**Part 4: GOVERNANCE & POLICY**

## Code Blocks

### audit-log.sh

```bash
#!/bin/bash
# /opt/claude/hooks/audit-log.sh

INPUT=$(cat)  # stdin으로 도구 호출 정보

# 사용자 정보 수집
USER=$(whoami)
HOST=$(hostname)
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id')
TOOL=$(echo "$INPUT" | jq -r '.tool_name')
TOOL_INPUT=$(echo "$INPUT" | jq -r '.tool_input')

# JSON 형식으로 SIEM 페이로드 작성
PAYLOAD=$(cat <<EOF
{
  "timestamp": "$TS",
  "user": "$USER",
  "host": "$HOST",
  "session_id": "$SESSION_ID",
  "tool": "$TOOL",
  "tool_input_hash": "$(echo $TOOL_INPUT | sha256sum | cut -d' ' -f1)",
  "app": "claude-code"
}
EOF
)

# 사내 SIEM API로 전송 (Splunk, ELK, Datadog 등)
curl -s -X POST https://siem.company.com/api/log \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $SIEM_TOKEN" \
  -d "$PAYLOAD" > /dev/null

# 통과 (도구 호출 진행 허용)
exit 0
```

## Speaker Notes

Audit Log Hook의 실제 스크립트 예시입니다.
stdin으로 도구 호출 정보를 받습니다.
사용자, 호스트, 타임스탬프, 세션 ID, 도구 이름, 입력 내용을 수집합니다.
JSON 형식으로 SIEM 페이로드를 작성합니다.
중요한 점은 tool_input의 본문은 그대로 보내지 않고 SHA256 해시만 저장한다는 것입니다.
민감 정보 노출 위험을 줄이면서 감사 추적은 가능하게 합니다.
curl로 사내 SIEM API에 전송합니다.
Splunk, ELK, Datadog 같은 도구의 HTTP Event Collector에 전송합니다.
SIEM_TOKEN은 환경변수로 주입됩니다.
마지막에 exit 0으로 통과시켜 도구 호출이 정상 진행되게 합니다.
이 hook은 non-blocking이므로 모든 활동이 로깅되면서도 사용자 경험에 영향을 주지 않습니다.
