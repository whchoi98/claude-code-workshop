# Slide 13: telemetry & theme

**Part 1: settings.json 구조**

## Code Blocks

### misc

```json
{
  "telemetry": {
    "enabled": true,
    "endpoint": "https://otel.company.com:4318",
    "headers": { "Authorization": "Bearer ${OTEL_TOKEN}" },
    "exporters": ["traces", "metrics", "logs"],
    "sampling": { "traces": 1.0, "metrics": "always" },
    "attributes": {
      "service.name": "claude-code",
      "deployment.environment": "production"
    }
  },

  "theme": "dark",   // "dark" | "light" | "system"

  "editor": {
    "tabWidth": 2,
    "insertFinalNewline": true,
    "trimTrailingWhitespace": true,
    "preferredQuotes": "single"
  },

  "outputStyle": "concise",   // "concise" | "verbose" | "casual"

  "updateChecker": { "enabled": true, "channel": "stable" }
}
```

## Speaker Notes

telemetry, theme, editor 같은 추가 옵션들을 살펴봅니다.
telemetry는 관측 가능성 옵션입니다.
enabled를 true로 설정하고 endpoint에 OpenTelemetry Collector URL을 지정합니다.
exporters로 traces, metrics, logs 중 어느 것을 보낼지 명시하고 sampling으로 비율을 조정합니다.
attributes에는 service name이나 deployment environment 같은 메타데이터를 추가합니다.
theme은 UI 테마입니다.
dark, light, system 세 가지 옵션이 있으며 system은 OS 설정을 따릅니다.
editor는 코드 편집기 선호도입니다.
tabWidth, insertFinalNewline, trimTrailingWhitespace, preferredQuotes 같은 코드 스타일 선호를 명시합니다.
Claude Code가 코드를 생성할 때 이 선호도를 따릅니다.
outputStyle은 응답 톤입니다.
concise는 간결, verbose는 상세, casual은 친근한 톤입니다.
updateChecker는 자동 업데이트 체크 활성화 여부입니다.
