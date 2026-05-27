# Slide 52: 동적 도구 정의

**Part 3: TOOL USE**

## Code Blocks

### dynamic tools

```python
# 시나리오: 사용자/컨텍스트별 다른 도구 제공

# 1. 사용자 권한 기반 도구
def get_tools_for_user(user) -> list:
    tools = [READ_TOOL]   # 기본

    if user.role == "admin":
        tools.append(WRITE_TOOL)
        tools.append(DELETE_TOOL)

    if "finance" in user.permissions:
        tools.append(FINANCE_TOOL)

    return tools

# 사용
user = get_user_from_session(request)
tools = get_tools_for_user(user)

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": prompt}],
)

# 2. OpenAPI에서 자동 생성
import yaml

def openapi_to_tools(openapi_path: str) -> list:
    with open(openapi_path) as f:
        spec = yaml.safe_load(f)

    tools = []
    for path, methods in spec["paths"].items():
        for method, op in methods.items():
            if method.upper() not in ["GET", "POST"]: continue

            tools.append({
                "name": op["operationId"],
                "description": op.get("summary", op.get("description", "")),
                "input_schema": op.get("parameters", {...}),
            })
    return tools

# 3. 데이터베이스 schema 기반
def db_schema_to_tools(conn) -> list:
    tools = []
    for table in conn.tables():
        tools.append({
            "name": f"query_{table}",
            "description": f"Query {table} table",
            "input_schema": {
                "type": "object",
                "properties": {
                    "where": {"type": "string"},
                    "limit": {"type": "integer"},
                },
            },
        })
    return tools

# 4. plugin 시스템
class Plugin:
    name: str
    description: str
    input_schema: dict
    def execute(self, **kwargs): ...

class WeatherPlugin(Plugin):
    name = "weather"
    description = "..."
    ...

PLUGINS = [WeatherPlugin(), DatabasePlugin(), ...]
tools = [p.to_tool_dict() for p in PLUGINS]
FUNCS = {p.name: p.execute for p in PLUGINS}
```

## Speaker Notes

동적 도구 정의는 런타임에 도구를 생성하는 패턴입니다.
1번 사용자 권한 기반 도구는 매우 일반적입니다.
get_tools_for_user 함수에서 user의 role과 permissions를 보고 적절한 도구만 반환합니다.
기본은 READ_TOOL이고 admin은 WRITE와 DELETE 추가, finance 권한은 FINANCE_TOOL 추가입니다.
2번 OpenAPI에서 자동 생성도 가능합니다.
openapi_to_tools 함수에서 YAML 스펙을 파싱하고 paths를 순회하면서 도구를 만듭니다.
operationId를 name으로, summary나 description을 그대로 사용합니다.
parameters를 input_schema로 변환합니다.
REST API를 가진 서비스를 즉시 Claude에 통합할 수 있습니다.
3번 데이터베이스 schema 기반은 테이블별 query 도구를 자동 생성합니다.
각 테이블에 query_테이블명 도구를 만들고 where와 limit를 받게 합니다.
4번 plugin 시스템은 가장 확장 가능한 구조입니다.
Plugin base class를 만들고 각 플러그인이 name, description, input_schema, execute를 구현합니다.
PLUGINS 리스트에서 to_tool_dict와 execute를 추출해 자동 등록됩니다.
새 플러그인 추가만으로 도구가 늘어납니다.
