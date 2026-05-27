# Slide 8: Full options overview

**Part 1: settings.json 구조**

## Code Blocks

### All options

```json
{
  "permissions": {
    "allow": [...], "ask": [...], "deny": [...]
  },

  "model": "claude-sonnet-4-5",
  "modelAlias": {
    "fast": "claude-haiku-4-5",
    "smart": "claude-opus-4-5"
  },

  "hooks": {
    "PreToolUse":  [...],
    "PostToolUse": [...],
    "SessionStart": [...],
    "Stop": [...]
  },

  "mcpServers": {
    "filesystem": { ... },
    "github": { ... },
    "internal-jira": { ... }
  },

  "telemetry": {
    "enabled": true,
    "endpoint": "https://otel.company.com"
  },

  "theme": "dark",
  "editor": { "tabWidth": 2, "insertFinalNewline": true },
  "outputStyle": "concise"
}
```

## Speaker Notes

settings.json의 전체 옵션을 6대 카테고리로 살펴봅니다.
첫 번째는 permissions입니다.
allow, ask, deny 세 가지 리스트로 도구 권한을 통제합니다.
두 번째는 model입니다.
기본 모델을 명시할 수 있고 modelAlias로 fast와 smart 같은 별명을 등록할 수 있습니다.
세 번째는 hooks입니다.
PreToolUse, PostToolUse, SessionStart, Stop 4가지 시점의 자동화 스크립트를 등록합니다.
네 번째는 mcpServers입니다.
filesystem, github 같은 공식 서버와 internal-jira 같은 사내 서버를 등록합니다.
다섯 번째는 telemetry입니다.
OpenTelemetry endpoint를 지정해 사내 SIEM과 통합합니다.
여섯 번째는 사용자 경험 관련 옵션입니다.
theme, editor, outputStyle 같은 옵션으로 개인화합니다.
