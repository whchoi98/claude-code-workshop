# Slide 171: Pattern 1 Example

**Part 9: WORKFLOW PATTERNS**

## Code Blocks

### EPC EXAMPLE

```
> 결제 모듈에 자동 재시도 로직을 추가해 주세요. (Plan 모드)

[Explore]
  ✓ Read src/payment/processor.ts
  ✓ Read src/payment/errors.ts
  ✓ Grep "PaymentError" → 5 callsites
  ✓ Read tests/payment/processor.test.ts

[Plan]
  1. exponential backoff 적용 (1s, 2s, 4s)
  2. 재시도 가능 에러 분류: NetworkError, TimeoutError
  3. 멱등성 검증: paymentIntentId로 중복 방지
  4. 최대 재시도 3회 (이후 dead letter queue)
  5. 새 테스트 케이스 4개 추가

  ✓ 위 계획으로 진행하시겠습니까?

> Yes

[Code]
  ✓ Edit src/payment/processor.ts
  ✓ Write src/payment/retry.ts
  ✓ Edit tests/payment/processor.test.ts
  ✓ Bash npm test → all green
```

## Speaker Notes

EPC 패턴의 구체적 예시를 살펴봅니다.
결제 모듈에 자동 재시도 로직을 추가하는 작업을 Plan 모드로 시작합니다.
Explore 단계에서 Claude가 processor, errors, 테스트 파일을 읽고 PaymentError 호출 지점들을 Grep으로 확인합니다.
Plan 단계에서 exponential backoff, 재시도 가능 에러 분류, 멱등성 검증, 최대 3회 재시도, 신규 테스트 케이스 4개 추가라는 5단계 계획을 명시적으로 제시하고 사용자 승인을 요청합니다.
사용자가 Yes를 응답하면 Code 단계로 진입해 합의된 범위 안에서 Edit, Write, Bash를 실행하고 모든 테스트가 green인지 확인합니다.
