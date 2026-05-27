# Slide 86: API doc generation

**Part 7: PATTERN 4 / DOCS WRITER**

## Code Blocks

### API doc

```bash
# 사용자 요청
"src/routes/users.js의 엔드포인트 문서를 만들어 줘"

# docs-writer의 출력 (Markdown)
## GET /users

사용자 목록을 페이지네이션과 함께 반환합니다.

### Query Parameters
| Name  | Type   | Required | Default | Description                |
|-------|--------|----------|---------|----------------------------|
| page  | int    | No       | 1       | 페이지 번호 (1-base)        |
| limit | int    | No       | 20      | 페이지당 항목 수 (max: 100) |

### Response 200
```json
{
  "users": [{ "id": "u_1", "name": "..." }],
  "links": { "next": "/users?page=2", "prev": null },
  "total": 142
}
```

### Errors
- 400: limit > 100
```

## Speaker Notes

API 문서 자동 생성 예시입니다.
사용자가 특정 라우트 파일의 엔드포인트 문서를 만들어 달라고 요청합니다.
docs-writer가 코드를 분석해 Markdown 형식의 API 문서를 출력합니다.
예시는 GET /users 엔드포인트입니다.
사용자 목록을 페이지네이션과 함께 반환한다고 명시합니다.
Query Parameters를 표로 정리합니다.
Name, Type, Required, Default, Description 컬럼을 갖춥니다.
Response 200의 JSON 스키마도 실제 응답 형태로 보여줍니다.
Errors 섹션에는 가능한 에러 코드와 조건을 명시합니다.
예시처럼 limit이 100을 초과하면 400 에러가 발생한다고 기술합니다.
이 형식은 OpenAPI 같은 표준으로 변환하기도 쉽습니다.
