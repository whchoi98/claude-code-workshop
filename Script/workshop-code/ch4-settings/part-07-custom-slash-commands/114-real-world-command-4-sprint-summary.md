# Slide 114: Real-world command 4: Sprint summary

**Part 7: CUSTOM SLASH COMMANDS**

## Code Blocks

### sprint summary

```bash
# .claude/commands/sprint-summary.md
---
description: 스프린트 활동 요약 (PR, Issue, 결과)
argument-hint: <since-date>
allowed-tools:
  - Bash(gh pr:*)
  - Bash(gh issue:*)
  - Bash(git log:*)
model: claude-sonnet-4-5
---

$ARGUMENTS 이후의 스프린트 활동을 요약해 주세요.

# 데이터 수집
1. gh pr list --state merged --search "merged:>=$ARGUMENTS"
2. gh issue list --state closed --search "closed:>=$ARGUMENTS"
3. git log --since="$ARGUMENTS" --pretty=format:"%h %an %s"

# 분석
1. 머지된 PR을 카테고리별 분류 (feat, fix, docs, refactor, etc)
2. 가장 active한 contributor top 5
3. 가장 큰 변경 (LoC 기준) top 3
4. 클로즈된 issue를 우선순위별 분류
5. 미해결 issue 중 critical/high 목록

# 출력 형식 (Markdown)
# Sprint Summary: $ARGUMENTS ~ now

## Highlights
- 머지된 PR: <count>개
- 클로즈된 Issue: <count>개
- 활동 contributors: <count>명

## PR 카테고리
- feat: <n> (주요: ...)
- fix: <n> (주요: ...)
...

## Top Contributors
1. @user1 (X PRs, Y commits)
...

## 다음 스프린트 준비
- 미해결 critical: <list>
- carry-over 후보: <list>

# 호출 예시
> /sprint-summary 2026-05-12
```

## Speaker Notes

실전 명령 네 번째는 스프린트 요약입니다.
2주마다 반복되는 스프린트 회고를 자동화합니다.
frontmatter에 argument-hint로 시작 날짜를 받음을 명시합니다.
allowed-tools에 gh pr, gh issue, git log를 허용합니다.
데이터 수집 단계에서 3가지 명령을 실행합니다.
gh pr list로 머지된 PR, gh issue list로 클로즈된 issue, git log로 commit 이력을 가져옵니다.
분석 단계에서 5가지 작업을 수행합니다.
첫째, 머지된 PR을 카테고리별 분류합니다.
둘째, 가장 active한 contributor top 5를 추립니다.
셋째, 가장 큰 변경 LoC 기준 top 3를 식별합니다.
넷째, 클로즈된 issue를 우선순위별 분류합니다.
다섯째, 미해결 critical과 high 목록을 만듭니다.
출력 형식은 Markdown입니다.
Highlights, PR 카테고리, Top Contributors, 다음 스프린트 준비 섹션으로 구성됩니다.
호출은 /sprint-summary 2026-05-12 같은 시작 날짜를 인자로 전달합니다.
