# Slide 102: 시나리오 2 기능 추가 (문제 정의)

**Part 5: QUICK START**

## Code Blocks

### feature spec

```
> /api/users 엔드포인트에 cursor 기반 페이지네이션을 추가해 주세요.

요구사항:
  - cursor 파라미터: 마지막 본 항목의 id (base64 인코딩)
  - limit 파라미터: 기본 20, 최대 100
  - 응답 헤더 Link: <...?cursor=xxx>; rel="next"
  - 정렬: created_at DESC, tiebreaker id DESC
  - 호환성: 기존 호출자가 깨지지 않아야 함 (cursor 없으면 첫 페이지)

테스트도 함께 작성해 주세요.
스타일은 기존 컨벤션을 따라 주세요 (CLAUDE.md 참고).
```

## Speaker Notes

두 번째 시나리오는 신기능 추가입니다.
cursor 기반 페이지네이션을 GET /api/users 엔드포인트에 추가하는 작업입니다.
요구사항을 자세히 명시하는 것이 핵심인데, cursor와 limit 파라미터 동작, 응답 헤더 형식, 정렬 기준과 tiebreaker, 호환성 요구사항을 모두 포함합니다.
추가로 테스트도 함께 작성해 달라고 요청하고, CLAUDE.md의 컨벤션을 따르도록 명시합니다.
이렇게 구체적으로 명시하면 Claude가 의도와 다른 구현을 할 가능성이 크게 줄어듭니다.
