# Slide 7: 3-tier hierarchy

**Part 1: settings.json 구조**

## Code Blocks

### Hierarchy

```bash
# 우선순위 (높음 → 낮음)

# Tier 1: managed-settings.json (조직 강제, 최우선)
macOS:   /Library/Application Support/Claude/managed-settings.json
Linux:   /etc/claude/managed-settings.json
Windows: C:\ProgramData\Claude\managed-settings.json
권한: root/Administrator 필요
용도: 회사 정책 강제

# Tier 2: 프로젝트 settings (.claude/settings.json)
위치: 프로젝트 루트의 .claude/settings.json
권한: 프로젝트 팀이 Git으로 관리
용도: 프로젝트 특수 설정 (팀 공유)

# Tier 3: 사용자 settings (~/.claude/settings.json)
위치: 사용자 홈 디렉토리
권한: 본인만 수정 가능
용도: 개인 선호 (테마, 단축키, 개인 MCP)

# 추가: settings.local.json (Git 미커밋 권장)
프로젝트 .claude/settings.local.json
용도: 개인의 프로젝트별 오버라이드
```

## Speaker Notes

3단 계층 구조의 파일 위치와 우선순위를 살펴봅니다.
Tier 1은 managed-settings.json으로 조직 강제 설정이며 최우선입니다.
macOS는 Library Application Support, Linux는 /etc/claude, Windows는 C: ProgramData에 위치합니다.
root나 Administrator 권한이 필요하며 회사 정책을 강제하는 용도입니다.
Tier 2는 프로젝트 settings로 프로젝트 루트의 .claude/settings.json에 있습니다.
프로젝트 팀이 Git으로 관리하며 프로젝트 특수 설정을 팀과 공유하는 용도입니다.
Tier 3는 사용자 settings로 사용자 홈 디렉토리에 있습니다.
본인만 수정 가능하며 테마나 단축키 같은 개인 선호 설정에 사용됩니다.
추가로 settings.local.json도 있습니다.
프로젝트 .claude/settings.local.json 형태이며 Git에 커밋하지 않는 것을 권장합니다.
개인의 프로젝트별 오버라이드 용도입니다.
