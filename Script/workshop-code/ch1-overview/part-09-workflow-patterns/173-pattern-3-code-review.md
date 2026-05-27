# Slide 173: Pattern 3 Code Review

**Part 9: WORKFLOW PATTERNS**

## Code Blocks

### CODE REVIEW

```bash
# 1. 본인 PR 셀프 리뷰
$ claude
> diff main..HEAD 한 후 발견 가능한 잠재적 이슈를 알려 줘
$ claude

Claude:
  ✓ Bash git diff main..HEAD --stat
  ✓ Bash git diff main..HEAD -- 'src/'
  ✓ Review 출력:
    - src/api/users.ts:142 N+1 query 위험 (loop in Promise.all)
    - src/utils/format.ts:67 toFixed로 precision 손실 가능
    - test 커버리지: 신규 코드 78% (목표 85% 미달)

# 2. 다른 사람 PR 리뷰
$ gh pr checkout 123
$ claude -p "이 PR이 우리 CLAUDE.md 컨벤션을 따르는지 검토해 줘"

# 3. CI 통합 (헤드리스)
$ claude -p "$(git diff main..HEAD)" --output-format json \
   > review.json
```

## Speaker Notes

Pattern 3 코드 리뷰입니다.
PR을 만들기 전 본인 PR 셀프 리뷰, 다른 사람의 PR 검토, CI 자동 통합 세 가지 시나리오를 다룹니다.
셀프 리뷰에서는 git diff를 읽혀 N+1 query 위험, 정밀도 손실, 테스트 커버리지 미달 같은 잠재 이슈를 찾아냅니다.
다른 사람 PR을 리뷰할 때는 gh pr checkout으로 받은 후 CLAUDE.md 컨벤션 준수 여부를 검토합니다.
CI 통합은 헤드리스 모드와 JSON 출력 옵션을 결합해 GitHub Actions에서 자동 리뷰를 수행할 수 있습니다.
