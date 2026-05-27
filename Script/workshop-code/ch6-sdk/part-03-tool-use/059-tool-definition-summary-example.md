# Slide 59: 도구 정의 종합 예시

**Part 3: TOOL USE**

## Code Blocks

### common tools

```bash
# 실무에서 자주 사용되는 도구 6가지
COMMON_TOOLS = [
    # 1. 웹 검색
    {
        "name": "web_search",
        "description": "최신 정보 검색. 시사, 가격, 날씨 같은 변하는 정보.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "num_results": {"type": "integer", "default": 5},
            },
            "required": ["query"],
        },
    },
    # 2. SQL 쿼리
    {
        "name": "run_sql",
        "description": "분석 데이터베이스에 읽기 전용 SQL. SELECT만.",
        "input_schema": {
            "type": "object",
            "properties": {
                "sql": {"type": "string"},
            },
            "required": ["sql"],
        },
    },
    # 3. HTTP 요청
    {
        "name": "http_get",
        "description": "JSON API GET. 사내 API endpoint 호출.",
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {"type": "string"},
                "headers": {"type": "object"},
            },
            "required": ["url"],
        },
    },
    # 4. 사내 위키 검색
    {
        "name": "search_wiki",
        "description": "사내 문서 시스템에서 정보 검색.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "space": {"type": "string", "enum": ["eng", "ops", "all"]},
            },
            "required": ["query"],
        },
    },
    # 5. 알림 발송
    {
        "name": "send_slack",
        "description": "Slack 채널에 메시지 발송.",
        "input_schema": {
            "type": "object",
            "properties": {
                "channel": {"type": "string"},
                "message": {"type": "string"},
            },
            "required": ["channel", "message"],
        },
    },
    # 6. 작업 생성
    {
        "name": "create_task",
        "description": "Jira/Linear에 작업 생성.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "description": {"type": "string"},
                "priority": {"type": "string", "enum": ["low", "medium", "high"]},
                "assignee": {"type": "string"},
            },
            "required": ["title"],
        },
    },
]
```

## Speaker Notes

실무에서 자주 사용되는 도구 6가지 세트입니다.
첫째, web_search로 최신 정보를 검색합니다.
시사, 가격, 날씨 같은 변하는 정보에 사용합니다.
둘째, run_sql로 분석 데이터베이스에 읽기 전용 SQL을 실행합니다.
SELECT만 허용해 안전성을 확보합니다.
셋째, http_get으로 JSON API의 GET 요청을 합니다.
사내 API endpoint 호출에 활용합니다.
넷째, search_wiki로 사내 문서 시스템에서 정보를 검색합니다.
space enum으로 검색 범위를 제한할 수 있습니다.
다섯째, send_slack으로 Slack 채널에 메시지를 발송합니다.
Claude가 작업 완료를 자동 알릴 수 있습니다.
여섯째, create_task로 Jira나 Linear에 작업을 생성합니다.
priority enum과 assignee로 정확한 작업 등록이 가능합니다.
이 6가지 도구를 조합하면 정보 수집부터 실행까지 자동화된 워크플로가 가능합니다.
예를 들어 Slack 메시지를 보고 관련 정보를 검색하고 작업을 생성하는 다단계 자동화입니다.
