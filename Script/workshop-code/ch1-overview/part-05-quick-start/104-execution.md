# Slide 104: 시나리오 2 기능 추가 (실행)

**Part 5: QUICK START**

## Code Blocks

### execution

```
> y (Plan 승인)

[Write] src/lib/pagination.ts (39 lines)
[Edit]  src/app/api/users/route.ts (cursor 처리 + Link header)
[Edit]  src/lib/users.ts (시그니처 변경: paginated 옵션)
[Write] tests/api/users.pagination.test.ts (5 test cases)
[Bash]  pnpm test -- pagination → 5/5 passed
[Bash]  pnpm test → 142/142 passed (회귀 없음)
[Bash]  pnpm lint → no issues

Git
  [Bash] git checkout -b feat/users-pagination
  [Bash] git add ...
  [Bash] git commit -m "feat(api): cursor-based pagination on /users"
  [Bash] gh pr create --title "..." --body "..."
  > Created PR #234: https://github.com/.../pull/234

총 소요: 4분 23초 / 토큰: 18,742 / 비용: $0.18
```

## Speaker Notes

사용자가 Plan을 승인하면 Claude는 모든 작업을 자동으로 실행합니다.
pagination 헬퍼 신규 작성, route 핸들러 수정, users 라이브러리 시그니처 변경, 테스트 파일 신규 작성, 그리고 모든 테스트와 lint 자동 실행입니다.
회귀가 없음을 확인한 후 git으로 새 브랜치 생성, 커밋, gh CLI로 PR 자동 생성까지 한 번에 처리합니다.
PR 본문에는 변경 요약과 테스트 결과가 포함되어 검토자가 바로 리뷰할 수 있습니다.
총 4분 23초, 18742 토큰, 약 $0.18의 비용으로 검토 가능한 PR이 만들어졌습니다.
