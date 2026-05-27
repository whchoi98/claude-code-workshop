# Slide 53: Pattern 1 / Auto Lint - settings

**Part 4: HOOKS 실전 패턴**

## Code Blocks

### settings reg

```bash
# 1. 프로젝트 .claude/settings.json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "/opt/claude/hooks/auto-lint.sh",
            "timeout": 10000
          }
        ]
      }
    ]
  }
}

# 2. matcher 설명
# "Write|Edit"  - Write 또는 Edit 도구 호출 시 실행
# "Edit"        - Edit만
# "Write"       - Write만
# "MultiEdit"   - 여러 파일 동시 수정 (포함하려면 추가)

# 3. timeout 권장값
# - lint만:     3000ms (3초)
# - lint + 포맷: 5000ms
# - 큰 프로젝트: 10000ms (10초)

# 4. 조직 표준화 (managed-settings)
# /etc/claude/managed-settings.json에 동일 설정 두면
# 모든 사용자의 모든 프로젝트에 적용됨

# 5. 환경변수로 도구 경로 전달
# auto-lint.sh가 PATH에 의존하지 않게 환경변수 사용
```

## Speaker Notes

Pattern 1을 settings에 등록하는 방법입니다.
프로젝트 .claude/settings.json에 PostToolUse Hook을 추가합니다.
matcher를 Write 또는 Edit으로 설정합니다.
command에 auto-lint.sh 스크립트 절대 경로를 명시합니다.
timeout을 10초로 충분히 둡니다.
matcher 종류를 정리합니다.
Write와 Edit 분리해서 적용할 수도 있고 MultiEdit까지 포함시킬 수도 있습니다.
timeout 권장값은 lint만 3초, lint와 포맷 5초, 큰 프로젝트는 10초입니다.
조직 표준화는 managed-settings에 동일 설정을 두면 됩니다.
모든 사용자의 모든 프로젝트에 자동 적용됩니다.
환경변수로 도구 경로를 전달하면 auto-lint.sh가 PATH에 의존하지 않게 됩니다.
사내 표준 도구 경로를 강제할 수 있어 일관성이 보장됩니다.
