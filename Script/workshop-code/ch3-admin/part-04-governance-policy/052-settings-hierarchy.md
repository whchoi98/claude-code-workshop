# Slide 52: Settings hierarchy

**Part 4: GOVERNANCE & POLICY**

## Code Blocks

### Hierarchy

```bash
# 우선순위 (높음 → 낮음)

# 1. managed-settings.json (조직 강제, 최우선)
# 위치 OS별:
#   macOS:   /Library/Application Support/Claude/managed-settings.json
#   Linux:   /etc/claude/managed-settings.json
#   Windows: C:\ProgramData\Claude\managed-settings.json
# 권한: 일반 사용자가 수정 불가 (관리자 권한 필요)

# 2. project settings (.claude/settings.json)
# 위치: 프로젝트 루트의 .claude/settings.json
# 권한: 프로젝트 팀이 Git으로 관리
# 사용: 프로젝트별 특수 설정

# 3. user settings (~/.claude/settings.json)
# 위치: 사용자 홈
# 권한: 본인만 수정
# 사용: 개인 선호 (테마, 단축키 등)

# 병합 규칙
- deny: 어느 계층이든 deny면 차단 (deny 항상 승리)
- allow/ask: 더 상위 계층(managed > project > user) 우선
```

## Speaker Notes

Settings의 3단 계층 구조와 우선순위입니다.
가장 높은 우선순위는 managed-settings.json입니다.
OS별 시스템 디렉토리에 위치하며 일반 사용자가 수정할 수 없습니다.
macOS는 Library Application Support, Linux는 /etc/claude, Windows는 C: ProgramData에 있습니다.
관리자 권한으로만 수정 가능합니다.
두 번째 우선순위는 project settings입니다.
프로젝트 루트의 .claude/settings.json에 있으며 프로젝트 팀이 Git으로 관리합니다.
프로젝트별 특수 설정에 사용됩니다.
세 번째 우선순위는 user settings입니다.
사용자 홈의 ~/.claude/settings.json에 있으며 본인만 수정 가능합니다.
테마나 단축키 같은 개인 선호에 사용합니다.
병합 규칙은 명확합니다.
deny는 어느 계층이든 deny면 차단됩니다.
deny가 항상 승리합니다.
allow와 ask는 더 상위 계층이 우선합니다.
