# Slide 48: Explicit dispatch real example

**Part 3: TASK 도구와 디스패치**

## Code Blocks

### explicit demo

```
> /agents
Available agents:
  - code-reviewer    : PR 코드 리뷰 (Sonnet)
  - security-scanner : 보안 분석 (Opus)
  - test-writer      : 테스트 작성 (Sonnet)
  - docs-writer      : 문서 작성 (Sonnet)
  - migration-bot    : 일괄 변경 (Haiku)

> docs-writer를 사용해서 src/api/users.js의 API 문서를 작성해 줘.

[메인]   docs-writer 에이전트를 호출합니다.
         → Task(docs-writer, "Generate API doc for src/api/users.js")

[docs ]  src/api/users.js 분석 중...
         5개 엔드포인트 식별: GET, POST, PUT, DELETE, PATCH /users
         OpenAPI 스타일 마크다운 작성 중...
         docs/api/users.md 생성 완료.

[메인]   문서 작성 완료: docs/api/users.md (5 endpoints documented).
         미리보기를 원하시면 보여드릴 수 있습니다.
```

## Speaker Notes

명시적 호출의 실전 대화 예시입니다.
사용자가 먼저 /agents 명령으로 등록된 에이전트 목록을 확인합니다.
5개의 에이전트가 나열됩니다.
각 에이전트의 이름, 역할, 모델이 함께 표시됩니다.
사용자가 docs-writer를 명시적으로 지정해 src/api/users.js의 API 문서를 작성해 달라고 요청합니다.
메인은 자동 디스패치를 우회하고 사용자가 지정한 docs-writer를 직접 호출합니다.
docs-writer는 파일 분석을 시작합니다.
5개의 엔드포인트를 식별하고 OpenAPI 스타일의 마크다운 문서를 작성합니다.
결과 파일은 docs/api/users.md로 저장됩니다.
메인은 작업 완료를 보고하고 미리보기를 원하면 보여줄 수 있다고 사용자에게 안내합니다.
명시적 호출은 예측 가능한 동작이 필요할 때 권장됩니다.
