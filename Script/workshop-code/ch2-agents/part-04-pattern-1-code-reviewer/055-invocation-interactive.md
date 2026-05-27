# Slide 55: Invocation interactive

**Part 4: PATTERN 1 / CODE REVIEWER**

## Code Blocks

### interactive

```bash
# 본인 PR을 작성한 후
$ git push origin feat/new-payment-flow
$ gh pr create --title "신규 결제 흐름" --body "..."

# Claude Code 세션에서 셀프 리뷰
$ claude

> 방금 만든 PR을 머지 전에 셀프 리뷰해 주세요.

[메인] code-reviewer를 호출해 분석합니다.
       → Task(code-reviewer, "git diff main..HEAD")

[리뷰] 분석 중... 변경 파일 7개, +234 -56 line.
       
## Summary
신규 결제 흐름 추가. 핵심 변경 사항은 PaymentService와 idempotency key.

## Issues
- [high] payment.js:88 — refund 흐름에서 idempotency key가 누락
- [medium] payment.js:124 — DB 트랜잭션 경계가 모호
- [low] tests/payment.test.js — refund 케이스 누락

> 첫 번째 이슈를 자세히 설명해 줘.
```

## Speaker Notes

첫 번째 호출 방법은 대화형입니다.
일상적인 PR 리뷰 흐름을 살펴봅니다.
본인 PR을 작성하고 푸시한 후 셀프 리뷰를 진행합니다.
gh CLI로 PR을 생성한 후 Claude Code 세션을 시작합니다.
사용자가 방금 만든 PR을 머지 전에 셀프 리뷰해 달라고 요청합니다.
메인은 code-reviewer를 자동 호출합니다.
Task 도구로 git diff main..HEAD를 분석하라고 지시합니다.
리뷰 에이전트가 분석을 진행합니다.
변경 파일 7개와 234줄 추가, 56줄 삭제를 확인합니다.
Summary와 Issues 두 섹션으로 결과를 반환합니다.
Issues는 우선순위 순으로 정렬됩니다.
high 이슈는 refund 흐름의 idempotency key 누락입니다.
사용자가 첫 번째 이슈를 자세히 설명해 달라고 추가 질문합니다.
대화형의 장점은 이런 drill-down이 자연스럽다는 것입니다.
