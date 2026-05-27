# Slide 53: managed-settings.json sample

**Part 4: GOVERNANCE & POLICY**

## Code Blocks

### managed-settings

```bash
# /etc/claude/managed-settings.json
{
  "permissions": {
    "allow": [
      "Read(**)",
      "Grep", "Glob",
      "Bash(npm test:*)", "Bash(npm run lint)",
      "Bash(git diff:*)", "Bash(git status)", "Bash(git log:*)"
    ],
    "ask": [
      "Edit(**)", "Write(**)",
      "Bash(git push:*)", "Bash(git commit:*)"
    ],
    "deny": [
      "Bash(rm -rf:*)",
      "Bash(curl:*)", "Bash(wget:*)",
      "Bash(* > /etc/*)",
      "Read(**/.env*)", "Read(**/secrets/**)"
    ]
  },
  "model": {
    "allowedModels": ["sonnet", "haiku"],
    "deniedModels": ["opus"]
  },
  "updateChecker": { "enabled": false },
  "telemetry": {
    "enabled": true,
    "endpoint": "https://otel.company.com/v1/traces"
  }
}
```

## Speaker Notes

managed-settings.json의 실제 예시입니다.
조직 표준 정책을 어떻게 정의하는지 보여줍니다.
permissions 섹션이 핵심입니다.
allow 리스트에 자동 허용되는 도구를 명시합니다.
Read 전체, Grep, Glob 같은 안전한 읽기 도구와 npm test, lint, git diff, status, log 같은 안전한 명령을 허용합니다.
ask 리스트에는 사용자 확인이 필요한 도구를 둡니다.
Edit과 Write, git push와 commit이 여기에 들어갑니다.
deny 리스트에는 절대 금지되는 패턴을 둡니다.
rm -rf 같은 위험 명령, curl wget 같은 외부 다운로드, /etc 디렉토리 쓰기, 환경 파일과 secrets 디렉토리 읽기를 차단합니다.
model 섹션에서 sonnet과 haiku만 허용하고 opus를 거부해 비용을 통제합니다.
updateChecker를 비활성화해 자동 업데이트를 차단합니다.
telemetry를 활성화하고 사내 OpenTelemetry 엔드포인트를 강제 지정합니다.
