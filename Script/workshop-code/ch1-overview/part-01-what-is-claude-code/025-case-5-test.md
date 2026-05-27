# Slide 25: Case 5 테스트 작성

**Part 1: WHAT IS CLAUDE CODE**

## Code Blocks

### TYPICAL FLOW

```
User: PaymentService의 테스트 커버리지를 90%로 끌어올려 주세요.

Claude:
  1. Bash    npm test -- --coverage → 현재 67% 확인
  2. Read    coverage/coverage-summary.json
  3. Grep    누락된 라인의 함수 식별 (refund, retry 등)
  4. Read    src/services/payment.js 미커버 분기 분석
  5. Write   tests/payment.refund.test.js
            tests/payment.retry.test.js
  6. Bash    npm test -- --coverage → 92% 달성
  7. Output  변경 요약 + 추가 권장 케이스
```

## Speaker Notes

다섯 번째 사례는 테스트 작성입니다.
사용자가 PaymentService의 커버리지를 90%로 끌어올려 달라고 요청하는 시나리오입니다.
Claude Code는 먼저 현재 커버리지를 측정하여 67%임을 확인하고, coverage 요약 JSON을 읽어 누락된 부분을 식별합니다.
그 후 refund와 retry 같은 미커버 함수를 분석하고, 각 함수의 분기와 예외 처리를 Read로 검토합니다.
새로운 테스트 파일들을 작성하여 92%까지 커버리지를 끌어올립니다.
마지막으로 변경 요약과 함께 추가 권장 케이스까지 제안합니다.
단순한 라인 커버리지 채우기가 아니라 분기 커버리지와 예외 케이스까지 다루기 때문에 실제로 의미 있는 테스트가 생성된다는 점이 중요합니다.
