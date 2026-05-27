# Slide 156: User Memory

**Part 8: CLAUDE.md & MEMORY**

## Code Blocks

### ~/.claude/CLAUDE.md

```bash
# Personal Preferences

## Communication Style
- 한국어로 응답
- 코드 변경 전 항상 Plan 제시
- 코드 변경 후 핵심 변경점 3줄 요약

## Code Style (개인 기본값)
- 들여쓰기: 스페이스 2칸
- 따옴표: 작은따옴표 (JS/TS)
- import 순서: 외부 → 내부 → 상대경로
- 트레일링 콤마: 항상

## Frequently Used Commands
- 빠른 테스트: jest --watch --testPathPattern
- Git 정리: git rebase -i HEAD~5
- 로그 검색: ag -i (the silver searcher)

## Tools
- 패키지: pnpm 선호 (npm/yarn 대신)
```

## Speaker Notes

User Memory는 사용자 홈 아래 ~/.claude/CLAUDE.md에 위치하며, 모든 프로젝트에 자동으로 적용되는 개인 선호 설정입니다.
한국어 응답, Plan 우선 제시 같은 커뮤니케이션 스타일, 들여쓰기와 따옴표 같은 개인 코드 스타일 기본값, 자주 쓰는 명령, 선호하는 도구를 적어둡니다.
여기에 명시한 내용은 Project Memory의 내용과 충돌하면 Project Memory가 우선합니다.
