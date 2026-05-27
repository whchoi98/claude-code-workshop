# Slide 185: Combining Patterns

**Part 9: WORKFLOW PATTERNS**

## Code Blocks

### COMBINED PATTERNS

```bash
# 예시: 신규 기능 + CI 자동 리뷰 + 비용 통제

# 1. EPC + Plan 모드로 신규 기능 개발
$ claude
> Shift+Tab (Plan 모드 활성화)
> /users API에 페이지네이션 추가

# 2. 큰 변경은 여러 Subagents 사용 (Pattern 4)
> 이 변경을 routes/services/tests 3개 Subagent로 병렬 처리

# 3. 비용 점검 후 다음 작업 결정 (Pattern 비용관리)
> /cost
# 사용량 확인 후 다음 작업 진행 여부 결정

# 4. PR 생성 → CI 자동 리뷰 (Pattern 8)
> git checkout -b feat/users-pagination && commit && gh pr create
# GitHub Actions가 자동으로 Claude로 리뷰 댓글 게시

# 5. 컨텍스트 정리 후 다음 작업
> /clear
> 다음 기능: ...
```

## Speaker Notes

실무에서는 여러 패턴을 결합해 사용합니다.
예시 시나리오를 보면, 1단계 EPC와 Plan 모드로 신규 기능 개발을 시작하고, 2단계 큰 변경은 여러 Subagents로 병렬 처리하며, 3단계 /cost로 비용을 점검한 후 다음 작업 진행 여부를 결정합니다.
4단계 PR 생성과 동시에 GitHub Actions에서 Claude로 자동 리뷰 댓글이 게시되고, 5단계 /clear로 컨텍스트를 정리한 후 다음 작업으로 넘어갑니다.
식으로 EPC, Plan, Multi-agent, Cost, CI 등 여러 패턴을 자연스럽게 결합하면 안전하고 효율적인 워크플로가 완성됩니다.
