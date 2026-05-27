# Slide 34: Permission inheritance

**Part 2: SUBAGENT 정의 방법**

## Code Blocks

### Permission Model

```bash
# 1. settings.json (프로젝트 전역 권한)
{
  "permissions": {
    "allow": ["Read(**)", "Bash(npm test:*)"],
    "ask":   ["Edit(**)", "Write(**)"],
    "deny":  ["Bash(rm -rf:*)"]
  }
}

# 2. Subagent의 tools 필드 (해당 에이전트만의 제한)
tools: Read, Edit, Bash(npm test:*)

# 3. 실제 적용 (교집합)
- Read       → allow (자동 허용)
- Edit       → ask  (사용자 확인 필요)
- Bash(npm)  → allow
- Bash(rm)   → deny (Subagent가 시도해도 차단)
```

## Speaker Notes

Subagent의 tools 필드가 settings.json의 권한 정책과 어떻게 통합되는지 설명합니다.
settings.json은 프로젝트 전역 권한을 정의합니다.
allow, ask, deny 세 가지 카테고리로 도구 호출을 통제합니다.
예시에서는 Read 전체를 자동 허용하고 npm test 명령도 자동 허용합니다.
Edit과 Write는 사용자 확인을 받고 rm -rf는 명시적으로 거부합니다.
Subagent의 tools 필드는 해당 에이전트만의 추가 제한입니다.
예시 에이전트는 Read, Edit, Bash 중 npm test만 사용한다고 선언합니다.
실제 적용은 교집합입니다.
Subagent의 tools 선언과 settings.json의 권한이 함께 적용됩니다.
Read는 양쪽에서 모두 허용되어 자동 실행되고, Edit은 tools에는 있지만 settings에서 ask이므로 사용자 확인을 받습니다.
Bash rm은 Subagent가 시도해도 deny가 적용되어 차단됩니다.
