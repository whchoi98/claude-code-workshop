# Slide 101: 시나리오 1 디버깅 (도구 호출)

**Part 5: QUICK START**

## Code Blocks

### tool execution

```typescript
# 사용자가 Plan을 승인한 후

[Edit] src/pages/user/profile.tsx
  - <p>{user.preferences.theme}</p>
  + <p>{user.preferences?.theme ?? 'light'}</p>

[Edit] src/lib/userService.ts
  + const normalize = (u: User) => ({
  +   ...u,
  +   preferences: u.preferences ?? {},
  + })
  ...
  - return user
  + return normalize(user)

[Write] prisma/migrations/2026_05_24_backfill_preferences.sql
  + UPDATE users SET preferences = '{}'::jsonb WHERE preferences IS NULL;

[Bash] pnpm test -- user/profile
  ✓ 23 tests passed

[Bash] git diff --stat
  3 files changed, 12 insertions(+), 4 deletions(-)
```

## Speaker Notes

Plan 승인 후 실제 도구 호출 시퀀스입니다.
Edit 도구로 profile.tsx에 옵셔널 체이닝을 적용하고 기본값을 추가합니다.
다음 Edit으로 userService에 normalize 함수를 추가해 모든 호출 지점에서 일관된 기본값을 보장합니다.
Write 도구로 새 마이그레이션 SQL 파일을 생성하는데, 기존 NULL 값을 빈 객체로 backfill합니다.
Bash로 관련 테스트를 자동 실행하고 23개 테스트가 통과하는 것을 확인합니다.
마지막으로 git diff --stat으로 전체 변경 요약을 제시합니다.
이 모든 흐름이 사용자의 추가 입력 없이 자동 진행되며, 사용자는 결과만 검토하면 됩니다.
