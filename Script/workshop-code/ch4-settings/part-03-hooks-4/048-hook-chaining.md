# Slide 48: Hook chaining

**Part 3: HOOKS 4가지 시점**

## Code Blocks

### chaining

```bash
# 여러 Hook을 순차 실행
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash|Edit|Write",
        "hooks": [
          { "type": "command", "command": "/opt/claude/dlp-check.sh" },
          { "type": "command", "command": "/opt/claude/audit-log.sh" },
          { "type": "command", "command": "/opt/claude/cost-check.sh" }
        ]
      }
    ]
  }
}

# 실행 순서
1. dlp-check.sh 실행
   - exit 1이면 → 차단 (다음 hook 실행 안 함)
   - exit 0이면 → 다음
2. audit-log.sh 실행
   - 항상 exit 0 (로깅만)
3. cost-check.sh 실행
   - 사용량 한도 초과 시 exit 1 차단
4. 모두 통과 시 도구 호출 진행

# matcher 별 분리도 가능
{
  "hooks": {
    "PreToolUse": [
      { "matcher": "Bash", "hooks": [...] },     # Bash 전용
      { "matcher": "Edit|Write", "hooks": [...] } # 쓰기 전용
    ]
  }
}
```

## Speaker Notes

Hook 체이닝은 같은 시점에 여러 Hook을 순차 실행하는 패턴입니다.
hooks 배열에 여러 command 객체를 나열합니다.
실행 순서는 정의된 순서를 따릅니다.
DLP 검사가 먼저, 그 다음 감사 로그, 마지막으로 비용 체크입니다.
Fail-fast 동작이 중요합니다.
어떤 hook이 exit 1로 차단을 결정하면 그 시점에서 멈춥니다.
다음 hook은 실행되지 않고 도구 호출도 차단됩니다.
DLP 검사에서 차단되면 감사 로그도 기록되지 않습니다.
매처별 분리도 가능합니다.
여러 객체를 hooks 배열에 두고 matcher만 다르게 설정합니다.
Bash 전용 hook과 Edit Write 전용 hook을 분리해 관리할 수 있습니다.
조합 가능성이 핵심입니다.
작은 단위 hook들을 만들어 두고 필요에 따라 조합하면 유지보수가 쉬워집니다.
