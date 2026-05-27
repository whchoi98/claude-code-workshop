# Slide 57: Pattern 3 / Audit - design

**Part 4: HOOKS 실전 패턴**

## Code Blocks

### register

```bash
# settings.json
{
  "hooks": {
    "PreToolUse":  [{ "matcher": ".*", "hooks": [{ "type": "command", "command": "/opt/claude/audit.sh pre"  }] }],
    "PostToolUse": [{ "matcher": ".*", "hooks": [{ "type": "command", "command": "/opt/claude/audit.sh post" }] }]
  }
}
```

## Speaker Notes

Pattern 3 Audit Logging의 설계를 살펴봅니다.
동작 흐름은 5단계입니다.
도구 호출 전후에 PreToolUse와 PostToolUse 양쪽 Hook을 모두 등록합니다.
입력과 결과를 수집하고 구조화 JSON 페이로드를 만들어 SIEM API로 비동기 전송합니다.
왜 Pre와 Post 모두인지 중요합니다.
PreToolUse만으로는 도구 호출 결과를 알 수 없습니다.
PostToolUse도 등록해 실행 결과의 성공이나 실패까지 함께 기록해야 완전한 감사 추적이 가능합니다.
settings.json에 두 시점을 모두 등록합니다.
matcher를 점 별로 두어 모든 도구 호출에 적용합니다.
같은 스크립트를 pre와 post 인자로 구분해 호출합니다.
비동기 전송과 본문 해시 처리가 핵심입니다.
