# Slide 58: Hooks for governance

**Part 4: GOVERNANCE & POLICY**

## Code Blocks

### Mandatory Hooks

```bash
# managed-settings.json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [{
          "type": "command",
          "command": "/opt/claude/hooks/audit-log.sh"
        }]
      },
      {
        "matcher": "Edit|Write",
        "hooks": [{
          "type": "command",
          "command": "/opt/claude/hooks/dlp-check.sh"
        }]
      }
    ],
    "SessionStart": [
      {
        "hooks": [{
          "type": "command",
          "command": "/opt/claude/hooks/policy-banner.sh"
        }]
      }
    ]
  }
}

# 효과
- 모든 Bash 호출이 사내 SIEM에 로깅
- 모든 Edit/Write가 DLP 검사 통과 필요
- 세션 시작 시 사용 정책 안내 메시지
```

## Speaker Notes

Hooks를 통한 거버넌스 강제를 살펴봅니다.
정책을 코드로 강제하는 강력한 메커니즘입니다.
managed-settings.json에 hooks 섹션을 추가합니다.
PreToolUse 후크는 도구 호출 직전에 실행됩니다.
Bash 호출 시 audit-log.sh를 실행해 사내 SIEM에 기록합니다.
Edit이나 Write 시 dlp-check.sh로 민감 정보를 검사합니다.
SessionStart 후크는 세션 시작 시 한 번 실행됩니다.
policy-banner.sh로 사용 정책을 사용자에게 안내합니다.
효과는 명확합니다.
모든 Bash 호출이 사내 SIEM에 자동 로깅됩니다.
모든 Edit과 Write가 DLP 검사를 통과해야만 진행됩니다.
세션 시작 시 사용 정책 안내 메시지가 자동 표시됩니다.
Hook 종류는 PreToolUse, PostToolUse, SessionStart, Stop 네 가지가 있습니다.
각각 적절한 시점에 사내 정책을 강제할 수 있습니다.
