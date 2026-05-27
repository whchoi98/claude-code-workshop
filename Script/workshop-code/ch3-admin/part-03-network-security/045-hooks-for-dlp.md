# Slide 45: Hooks for DLP

**Part 3: NETWORK & SECURITY**

## Code Blocks

### DLP Hook

```bash
# .claude/settings.json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash|Edit|Write",
        "hooks": [{
          "type": "command",
          "command": "/usr/local/bin/dlp-check.sh"
        }]
      }
    ]
  }
}

# /usr/local/bin/dlp-check.sh
#!/bin/bash
INPUT=$(cat)  # stdin으로 도구 호출 정보 수신

# 민감 패턴 감지
if echo "$INPUT" | grep -qE 'AKIA[0-9A-Z]{16}'; then
  echo '{"action":"block","reason":"AWS key detected"}' >&2
  exit 1
fi

if echo "$INPUT" | grep -qE 'ssh-rsa AAAAB3'; then
  echo '{"action":"block","reason":"SSH private key"}' >&2
  exit 1
fi

# 통과
exit 0

# 효과
- AWS Key 노출 즉시 차단
- SSH 개인키 노출 차단
- 모든 도구 호출 사전 검증
```

## Speaker Notes

Hooks를 통한 DLP, 즉 Data Loss Prevention 구현을 살펴봅니다.
민감 정보가 외부로 나가기 전에 사전 차단하는 패턴입니다.
settings.json에서 PreToolUse 후크를 설정합니다.
Bash, Edit, Write 도구 호출 직전에 dlp-check.sh를 실행합니다.
dlp-check.sh 스크립트를 봅니다.
stdin으로 도구 호출 정보를 수신합니다.
민감 패턴을 정규식으로 감지합니다.
AKIA로 시작하는 AWS Access Key 패턴이나 ssh-rsa로 시작하는 SSH 개인키 패턴이 발견되면 block 액션과 reason을 JSON으로 출력하고 exit 1로 차단합니다.
패턴이 발견되지 않으면 exit 0으로 통과시킵니다.
효과는 명확합니다.
AWS Key 노출이 즉시 차단됩니다.
SSH 개인키 노출도 차단됩니다.
모든 도구 호출이 사전에 검증되어 사고를 예방할 수 있습니다.
