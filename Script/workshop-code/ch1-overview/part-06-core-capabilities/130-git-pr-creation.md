# Slide 130: Git PR creation

**Part 6: CORE CAPABILITIES**

## Code Blocks

### PR creation

```bash
# 1. gh CLI 인증 (사전 1회)
gh auth status
# 또는: gh auth login

# 2. Claude가 PR을 생성하는 흐름
Bash("git push -u origin feat/user-pagination")

Bash("gh pr create --title '...' --body \"$(cat <<'EOF'
## Summary
사용자 API에 페이지네이션 추가.

## Changes
- Cursor 기반 페이지네이션 구현
- Link 헤더로 next/prev 이동 지원
- 단위 테스트 12개 추가

## Test Plan
- npm test -- pagination (passes ✓)
- 수동 검증: /users?page=2&limit=20

🤖 Generated with Claude Code
EOF
)\"")
```

## Speaker Notes

GitHub PR 생성 흐름입니다.
사전에 한 번 gh auth login 명령으로 gh CLI 인증을 마쳐 두어야 합니다.
그 후 Claude가 PR을 생성하는 흐름은 두 단계입니다.
1단계 git push로 브랜치를 원격에 푸시합니다.
2단계 gh pr create 명령으로 PR을 생성합니다.
title은 자동 작성되며 body는 Summary, Changes, Test Plan 세 섹션을 자동 구성합니다.
마지막에 Generated with Claude Code 같은 표시를 추가해 AI가 작성한 PR임을 명확히 합니다.
