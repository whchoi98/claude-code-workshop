# Slide 105: 시나리오 3 리팩토링

**Part 5: QUICK START**

## Code Blocks

### refactor

```
> 모든 API 핸들러에서 try/catch + console.error 패턴을
  중앙 errorHandler 미들웨어로 통합해 주세요.
  
  목표: 47개 파일, 일관된 에러 로깅, Sentry 통합

Claude:
  Grep "console\.error" --include "*.ts" → 47 matches
  Read src/middleware/errorHandler.ts → 이미 존재, Sentry 통합 완료

  Plan
    47개 파일에서 try/catch + console.error 패턴 제거
    errorHandler 미들웨어를 라우터 레벨에 적용
    개별 핸들러는 throw만 (catch는 미들웨어 담당)

    예상 변경: ~200 lines 삭제, ~50 lines 추가
    테스트: 기존 통과 + 새 시나리오 추가

  Approve? (y/n/edit/preview)
```

## Speaker Notes

세 번째 시나리오는 대규모 리팩토링입니다.
모든 API 핸들러의 try-catch와 console.error 패턴을 중앙 errorHandler 미들웨어로 통합하는 작업입니다.
Claude는 먼저 Grep으로 47개 파일을 식별하고, 이미 존재하는 errorHandler 미들웨어 코드를 확인합니다.
Plan에서 변경 전략을 제시하는데, 47개 파일에서 패턴을 제거하고 미들웨어를 라우터 레벨에 적용하며 핸들러는 throw만 하도록 단순화합니다.
예상 변경량과 테스트 영향까지 미리 알려 주므로 사용자는 변경 규모를 정확히 파악할 수 있습니다.
preview 옵션으로 실제 diff를 미리 볼 수도 있습니다.
