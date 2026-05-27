# Slide 67: Real dialog

**Part 5: PATTERN 2 / TESTER**

## Code Blocks

### real dialog

```
> PaymentService의 테스트 커버리지를 90%로 끌어올려 주세요.

[메인] test-writer 에이전트를 호출합니다.
       → Task(test-writer, "PaymentService coverage to 90%")

[test ] 현재 커버리지 측정 중...
        Bash: npm test -- --coverage
        결과: PaymentService 67%

       갭 분석 중...
        Read: coverage/lcov-report/payment.html
        미커버: refund(), retry(), idempotency_check()

       refund() 분석 중...
        Read: src/services/payment.js (line 88-145)
        분기 6개, 엣지 케이스 4개 식별

       테스트 작성 중...
        Write: tests/payment.refund.test.js (8 cases)

       실행 검증 중...
        Bash: npm test -- payment.refund
        결과: 8/8 passed ✓

       최종 커버리지 측정...
        결과: PaymentService 92% (+25%)

[메인] 92%까지 향상. 8개 케이스가 신규 추가됨.
```

## Speaker Notes

Tester 에이전트의 실전 대화 예시입니다.
사용자가 PaymentService의 테스트 커버리지를 90%로 끌어올려 달라고 요청합니다.
메인은 test-writer 에이전트를 호출합니다.
Task 도구로 작업을 위임합니다.
에이전트가 단계별로 작업을 진행합니다.
첫째, 현재 커버리지를 측정합니다.
npm test --coverage 명령으로 67%임을 확인합니다.
둘째, 갭 분석을 합니다.
coverage 리포트를 읽어 refund, retry, idempotency_check 함수가 미커버임을 식별합니다.
셋째, refund 함수를 분석합니다.
분기 6개와 엣지 케이스 4개를 식별합니다.
넷째, 테스트 파일을 작성합니다.
8개 케이스가 포함된 payment.refund.test.js 파일을 생성합니다.
다섯째, 실행 검증입니다.
8개 모두 통과합니다.
여섯째, 최종 커버리지 측정으로 92%를 확인합니다.
메인은 25퍼센트 포인트 향상을 사용자에게 보고합니다.
