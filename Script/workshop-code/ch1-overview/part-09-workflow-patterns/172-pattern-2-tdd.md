# Slide 172: Pattern 2 TDD

**Part 9: WORKFLOW PATTERNS**

## Code Blocks

### TDD example

```
> userService.changePassword 에 대한 TDD를 시작합니다.

Claude:
  1. Write tests/userService.changePassword.test.ts (실패 테스트 5개)
  2. Bash npm test → 5 failures
  3. Edit src/services/userService.ts (최소 구현)
  4. Bash npm test → all green
  5. Edit src/services/userService.ts (Refactor)
  6. Bash npm test → all green
```

## Speaker Notes

Pattern 2 TDD 워크플로입니다.
Test-First, 즉 실패하는 테스트를 먼저 작성하고 그 테스트를 통과시키는 최소 구현, 그리고 리팩토링의 사이클을 반복합니다.
TDD는 Claude의 능력과 매우 잘 맞는데, 실패하는 테스트가 명확한 목표가 되어 Claude가 헤매지 않고 빠르게 작업할 수 있습니다.
예시처럼 changePassword 같은 함수를 TDD로 개발할 때 Claude는 먼저 실패 테스트 5개를 작성하고, 테스트가 모두 실패함을 확인한 후, 최소 구현으로 모두 통과시키고, 마지막으로 리팩토링하면서 테스트가 계속 green인지 검증합니다.
