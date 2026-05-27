# Slide 17: Org standard example

**Part 1: settings.json 구조**

## Code Blocks

### managed

```bash
# /etc/claude/managed-settings.json (root only, 강제)
{
  "permissions": {
    "deny": [
      "Bash(rm -rf:*)", "Bash(curl:*)", "Bash(wget:*)",
      "Bash(* > /etc/*)",
      "Read(**/.env*)", "Read(**/credentials/**)",
      "Read(**/private_key*)", "Read(**/.ssh/**)"
    ]
  },
  "model": "claude-sonnet-4-5",
  "modelAlias": {
    "smart": "claude-sonnet-4-5"   # smart도 Sonnet (Opus 차단)
  },
  "deniedModels": ["claude-opus-4-5"],
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash|Edit|Write",
        "hooks": [{ "type": "command", "command": "/opt/claude/dlp.sh" }]
      }
    ],
    "SessionStart": [
      { "hooks": [{ "type": "command", "command": "/opt/claude/policy.sh" }] }
    ]
  },
  "telemetry": {
    "enabled": true,
    "endpoint": "https://otel.company.com:4318"
  },
  "updateChecker": { "enabled": false }
}
```

## Speaker Notes

완성 예시 세 번째는 조직 표준입니다.
/etc/claude/managed-settings.json에 root 권한으로만 작성합니다.
사용자가 수정할 수 없는 강제 설정입니다.
permissions의 deny에 조직 차원의 위험 패턴을 모두 명시합니다.
rm, curl, wget, 환경 파일 읽기, credentials 디렉토리, private key, SSH 디렉토리를 차단합니다.
model을 Sonnet으로 기본 지정하고 modelAlias로 smart도 Sonnet에 매핑합니다.
사용자가 smart를 호출해도 Opus가 아닌 Sonnet이 사용됩니다.
deniedModels로 Opus를 명시 차단해 이중 보호합니다.
hooks의 PreToolUse에 DLP 스크립트를 강제 등록합니다.
SessionStart에 정책 안내 스크립트도 강제합니다.
telemetry를 강제 활성화해 모든 사용이 SIEM에 기록됩니다.
updateChecker를 비활성화해 자동 업데이트를 차단합니다.
조직 거버넌스의 완성판입니다.
