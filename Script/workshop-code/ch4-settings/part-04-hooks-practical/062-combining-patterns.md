# Slide 62: Combining patterns

**Part 4: HOOKS 실전 패턴**

## Code Blocks

### combined

```bash
# managed-settings.json - 조직 표준 (모든 패턴 결합)
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash|Edit|Write|MultiEdit",
        "hooks": [
          { "type": "command", "command": "/opt/claude/hooks/dlp.sh" },
          { "type": "command", "command": "/opt/claude/hooks/audit.sh pre" }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [
          { "type": "command", "command": "/opt/claude/hooks/auto-format-pro.sh" }
        ]
      },
      {
        "matcher": ".*",
        "hooks": [
          { "type": "command", "command": "/opt/claude/hooks/audit.sh post" }
        ]
      }
    ],
    "SessionStart": [
      { "hooks": [{ "type": "command", "command": "/opt/claude/hooks/session-start.sh" }] }
    ],
    "Stop": [
      { "hooks": [{ "type": "command", "command": "/opt/claude/hooks/slack-notify.sh" }] }
    ]
  }
}

# 실행 순서 (Write 호출 시)
1. PreToolUse: dlp.sh → audit.sh pre  (둘 다 통과해야 진행)
2. Write 도구 실행
3. PostToolUse: auto-format-pro.sh → audit.sh post
```

## Speaker Notes

5가지 패턴을 모두 결합한 조직 표준 예시입니다.
managed-settings.json에 모든 Hook이 등록됩니다.
PreToolUse에 DLP 검사와 감사 로그 pre가 순차 등록됩니다.
DLP가 차단하면 audit pre는 실행되지 않습니다.
PostToolUse는 두 그룹으로 나뉩니다.
첫 그룹은 Write Edit MultiEdit만 매처로 auto-format-pro를 실행합니다.
두 번째 그룹은 모든 도구에 audit post를 실행합니다.
SessionStart에는 정책 안내와 환경 검증 스크립트가 있습니다.
Stop에는 Slack 알림이 등록됩니다.
Write 호출 시 실제 실행 순서를 봅니다.
1단계 PreToolUse로 dlp.sh와 audit.sh pre가 순차 실행됩니다.
둘 다 통과해야 진행됩니다.
2단계 Write 도구가 실제 실행됩니다.
3단계 PostToolUse로 auto-format-pro와 audit post가 실행됩니다.
조직 차원의 종합 거버넌스가 자동 작동합니다.
