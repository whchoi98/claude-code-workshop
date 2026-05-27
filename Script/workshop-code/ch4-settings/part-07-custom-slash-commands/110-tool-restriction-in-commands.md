# Slide 110: Tool restriction in commands

**Part 7: CUSTOM SLASH COMMANDS**

## Code Blocks

### tool restrict

```bash
# .claude/commands/read-only-analysis.md
---
description: 읽기 전용 분석 (코드 수정 절대 안 함)
allowed-tools:
  - Read
  - Grep
  - Glob
  - WebFetch
disallowed-tools:
  - Edit
  - Write
  - MultiEdit
  - Bash
---

이 명령은 분석만 수행하고 절대 수정하지 않습니다.

$ARGUMENTS 에 대해 다음 관점에서 분석해 주세요:
- 코드 구조와 의도
- 잠재적 문제점
- 개선 제안 (실행은 안 함)

# .claude/commands/auto-deploy.md  
---
description: 자동 배포 (위험 작업, 신중히 사용)
allowed-tools:
  - Read
  - Bash(git:*)
  - Bash(npm run deploy:*)
disallowed-tools:
  - Bash(rm:*)
  - Bash(sudo:*)
---

$ARGUMENTS 환경에 배포합니다.

절차:
1. git status로 깨끗한지 확인
2. npm run test 통과 확인
3. npm run deploy:$ARGUMENTS 실행

# 효과
- 명령 단위 권한 통제로 안전성 향상
- 위험한 명령은 매우 좁은 권한만
```

## Speaker Notes

명령별 도구 제한 방법입니다.
명령 단위로 권한을 통제해 안전성을 향상시킵니다.
read-only-analysis 명령 예시를 봅니다.
allowed-tools에 Read, Grep, Glob, WebFetch만 명시합니다.
disallowed-tools에 Edit, Write, MultiEdit, Bash를 명시 차단합니다.
이 명령 실행 중에는 코드를 절대 수정할 수 없습니다.
auto-deploy 명령은 정반대입니다.
위험한 작업이므로 매우 좁은 권한만 부여합니다.
allowed-tools에 Read, git 명령, npm run deploy 명령만 명시합니다.
disallowed-tools에 rm과 sudo를 명시 차단합니다.
배포에 필요한 최소 권한만 부여됩니다.
효과는 명확합니다.
명령 단위 권한 통제로 안전성이 향상됩니다.
위험한 명령은 매우 좁은 권한만 가지므로 사고 위험이 최소화됩니다.
