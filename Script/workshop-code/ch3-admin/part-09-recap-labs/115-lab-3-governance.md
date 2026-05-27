# Slide 115: Lab 3 / Governance

**Part 9: RECAP & 3 LABS**

## Code Blocks

### Lab 3 steps

```bash
# 1. managed-settings.json 작성 (Lab VM)
sudo tee /etc/claude/managed-settings.json <<EOF
{
  "permissions": {
    "allow": ["Read(**)", "Grep", "Glob", "Bash(npm test:*)"],
    "ask": ["Edit(**)", "Write(**)"],
    "deny": ["Bash(rm -rf:*)", "Read(**/.env*)"]
  },
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash|Edit|Write",
      "hooks": [{"type":"command", "command":"/opt/claude/dlp.sh"}]
    }]
  },
  "telemetry": {
    "enabled": true,
    "endpoint": "https://otel.lab.local:4318"
  }
}
EOF

# 2. DLP Hook 스크립트 작성
sudo tee /opt/claude/dlp.sh <<'EOF'
#!/bin/bash
INPUT=$(cat)
if echo "$INPUT" | grep -qE 'AKIA[0-9A-Z]{16}'; then
  echo '{"action":"block","reason":"AWS key"}' >&2
  exit 1
fi
exit 0
EOF
sudo chmod +x /opt/claude/dlp.sh

# 3. 검증 시나리오
> 다음 코드를 src/aws.js에 작성해줘:
  AKIAIOSFODNN7EXAMPLE
# 결과: DLP Hook이 차단 (정상 동작)
```

## Speaker Notes

Lab 3는 managed-settings 거버넌스 구축 실습입니다.
약 30분 소요됩니다.
권한 정책, DLP Hook, OpenTelemetry 수집을 한 번에 구성합니다.
1단계 managed-settings.json을 sudo로 작성합니다.
/etc/claude 디렉토리에 저장하며 일반 사용자가 수정할 수 없습니다.
permissions에 allow, ask, deny 규칙을 명시합니다.
hooks의 PreToolUse에 DLP 스크립트를 등록합니다.
telemetry로 OpenTelemetry endpoint를 강제 설정합니다.
2단계 DLP Hook 스크립트를 작성합니다.
/opt/claude/dlp.sh에 AWS Access Key 패턴 감지 로직을 넣습니다.
AKIA로 시작하는 16자 영숫자 패턴이 발견되면 차단합니다.
chmod +x로 실행 권한을 부여합니다.
3단계 검증 시나리오를 실행합니다.
Claude Code에서 AKIA로 시작하는 가짜 Key를 코드에 작성해 달라고 요청합니다.
결과적으로 DLP Hook이 차단해 작성이 거부되어야 정상입니다.
실제 운영 환경에서 그대로 사용할 수 있는 거버넌스 패턴을 직접 구축한 경험을 얻게 됩니다.
