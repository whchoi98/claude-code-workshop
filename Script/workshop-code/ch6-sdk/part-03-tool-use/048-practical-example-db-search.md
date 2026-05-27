# Slide 48: 실전 예시 / DB 검색 봇

**Part 3: TOOL USE**

## Code Blocks

### DB bot

```python
from anthropic import Anthropic
import sqlite3
import json

client = Anthropic()

# DB 연결
conn = sqlite3.connect("company.db")

# 도구 정의
TOOLS = [
    {
        "name": "query_users",
        "description": "사용자 정보 SQL 쿼리. SELECT만 허용.",
        "input_schema": {
            "type": "object",
            "properties": {
                "where": {
                    "type": "string",
                    "description": "WHERE 절 (예: department='Eng' AND age>30)",
                },
                "limit": {"type": "integer", "default": 10, "maximum": 100},
            },
            "required": ["where"],
        },
    },
    {
        "name": "get_user_details",
        "description": "특정 사용자 ID의 상세 정보",
        "input_schema": {
            "type": "object",
            "properties": {
                "user_id": {"type": "integer"},
            },
            "required": ["user_id"],
        },
    },
]

def query_users(where: str, limit: int = 10):
    # SQL injection 방지 (실제로는 SQLAlchemy 같은 것 사용 권장)
    sql = f"SELECT id, name, dept, age FROM users WHERE {where} LIMIT ?"
    rows = conn.execute(sql, (limit,)).fetchall()
    return [dict(zip(["id", "name", "dept", "age"], r)) for r in rows]

def get_user_details(user_id: int):
    row = conn.execute(
        "SELECT * FROM users WHERE id=?", (user_id,)
    ).fetchone()
    return dict(row) if row else {"error": "Not found"}

FUNCS = {"query_users": query_users, "get_user_details": get_user_details}

def chat(user_input: str):
    messages = [{"role": "user", "content": user_input}]
    while True:
        r = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=2048,
            tools=TOOLS,
            messages=messages,
        )
        messages.append({"role": "assistant", "content": r.content})
        if r.stop_reason != "tool_use":
            return "".join(b.text for b in r.content if b.type=="text")
        results = []
        for b in r.content:
            if b.type == "tool_use":
                try:
                    out = FUNCS[b.name](**b.input)
                    results.append({"type":"tool_result", "tool_use_id":b.id,
                                    "content": json.dumps(out)})
                except Exception as e:
                    results.append({"type":"tool_result", "tool_use_id":b.id,
                                    "content": str(e), "is_error": True})
        messages.append({"role": "user", "content": results})
```

## Speaker Notes

실전 예시 데이터베이스 검색 봇입니다.
SQLite DB와 Claude를 연결해 자연어로 데이터를 조회합니다.
도구는 2개를 정의합니다.
query_users는 SQL WHERE 절을 받아 사용자 목록을 반환합니다.
limit는 1에서 100 사이로 제한합니다.
get_user_details는 user_id로 특정 사용자의 모든 정보를 반환합니다.
실제 함수 구현은 sqlite3 connection으로 쿼리를 실행합니다.
SQL injection 방지를 위해 실무에서는 SQLAlchemy 같은 ORM을 권장합니다.
FUNCS dict로 함수를 매핑합니다.
chat 함수가 핵심입니다.
user_input으로 시작해 while 루프에서 messages.create를 반복 호출합니다.
stop_reason이 tool_use가 아니면 text 블록을 추출해 반환합니다.
tool_use면 각 블록을 처리합니다.
예외 발생 시 is_error true로 표시해 Claude가 인식하도록 합니다.
결과를 user role의 tool_result로 다음 호출에 전달합니다.
사용자는 영업 부서에 30세 이상인 사람 같은 자연어 질의로 DB를 조회할 수 있게 됩니다.
