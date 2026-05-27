# Slide 43: 도구 정의 상세

**Part 3: TOOL USE**

## Code Blocks

### tool definition

```bash
# 1. 다양한 입력 타입
TOOLS = [
    {
        "name": "search_database",
        "description": "사용자 데이터베이스 검색",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "검색어",
                },
                "limit": {
                    "type": "integer",
                    "minimum": 1, "maximum": 100,
                    "default": 10,
                },
                "filters": {
                    "type": "object",
                    "properties": {
                        "department": {"type": "string"},
                        "min_age": {"type": "integer", "minimum": 0},
                    },
                },
                "sort_by": {
                    "type": "string",
                    "enum": ["name", "age", "created_at"],
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "send_email",
        "description": "이메일 발송",
        "input_schema": {
            "type": "object",
            "properties": {
                "to": {
                    "type": "array",
                    "items": {"type": "string", "format": "email"},
                },
                "subject": {"type": "string"},
                "body": {"type": "string"},
                "cc": {
                    "type": "array",
                    "items": {"type": "string", "format": "email"},
                },
            },
            "required": ["to", "subject", "body"],
        },
    },
]

# 2. 좋은 description 작성 팁
# - 도구가 무엇을 하는지 명확히
# - 언제 사용해야 하는지 힌트
# - 결과 형식 간략 설명
# - 제약 사항 명시 (rate limit, 권한 등)
```

## Speaker Notes

도구 정의는 JSON Schema 표준을 따릅니다.
1번 다양한 입력 타입을 정의할 수 있습니다.
search_database 예시는 복잡한 입력을 보여줍니다.
query는 단순 string입니다.
limit는 integer로 minimum과 maximum, default 값을 명시할 수 있습니다.
filters는 nested object로 더 구체적인 조건을 받습니다.
sort_by는 enum으로 허용 값을 제한합니다.
required에 query만 명시하면 다른 필드는 선택입니다.
send_email 예시는 배열과 format 검증을 보여줍니다.
to와 cc는 string의 array이고 format을 email로 명시해 이메일 형식 검증을 합니다.
2번 좋은 description 작성 팁이 매우 중요합니다.
도구가 무엇을 하는지 명확히 적습니다.
언제 사용해야 하는지 힌트를 줍니다.
결과 형식을 간략히 설명합니다.
제약 사항을 명시합니다.
Claude는 description을 보고 도구 사용 여부를 결정하므로 description의 품질이 도구 사용 정확도를 좌우합니다.
