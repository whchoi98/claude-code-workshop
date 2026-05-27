# Slide 91: 실전 / Database MCP

**Part 5: MCP SDK 통합**

## Code Blocks

### Database MCP

```python
# db_analyst.py - 자연어로 데이터 분석
import anthropic

client = anthropic.Anthropic()

def ask_data(question: str):
    response = client.beta.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=4000,
        mcp_servers=[{
            "type": "url",
            "url": "https://mcp.company.com/postgres",
            "name": "db",
            "authorization_token": os.getenv("DB_MCP_TOKEN"),
        }],
        # 읽기 전용 도구만
        tools=[
            {"name": "db__list_schemas"},
            {"name": "db__list_tables"},
            {"name": "db__describe_table"},
            {"name": "db__query"},   # SELECT만 가능한 read-only
        ],
        system="""당신은 데이터 분석 전문가입니다.

        흐름:
        1. list_schemas, list_tables로 사용 가능한 데이터 파악
        2. describe_table로 컬럼 정보 확인
        3. query로 SQL 실행 (SELECT만)
        4. 결과를 자연어로 설명

        규칙:
        - LIMIT을 항상 사용 (기본 100)
        - 큰 테이블은 COUNT나 샘플링으로 시작
        - 결과를 마크다운 표로 정리""",
        messages=[{"role": "user", "content": question}],
        betas=["mcp-client-2025-04-04"],
    )
    return response

# 사용 예시
result = ask_data("지난주 가장 많이 팔린 상품 top 5")
print("".join(b.text for b in result.content if b.type == "text"))

# Claude가 자동으로:
# 1. db__list_tables -> orders, products 같은 테이블 발견
# 2. db__describe_table products -> 컬럼 구조 파악
# 3. db__query "SELECT p.name, SUM(o.qty) AS sold
#               FROM orders o JOIN products p ON o.product_id=p.id
#               WHERE o.created_at >= now()-interval '7 days'
#               GROUP BY p.name ORDER BY sold DESC LIMIT 5"
# 4. 결과를 마크다운 표로 정리

# 다양한 질문 가능
ask_data("이달의 신규 가입자 수")
ask_data("지역별 매출 비교")
ask_data("재고가 10개 이하인 상품 목록")
ask_data("VIP 고객의 구매 패턴 분석")

# 안전 장치
# - read-only DB user
# - LIMIT 강제
# - 시간 제한
# - 로그 기록 (감사용)
# - 사용자별 권한 통제
```

## Speaker Notes

실전 Database MCP 통합으로 자연어 데이터 분석을 구현합니다.
ask_data 함수에서 자연어 질문을 받아 SQL 분석을 자동 수행합니다.
DB MCP 서버에 연결하고 읽기 전용 도구 4가지만 허용합니다.
list_schemas, list_tables, describe_table, query 네 가지입니다.
query는 SELECT만 가능한 read-only 도구로 설정되어 있어 안전합니다.
system prompt에 4단계 흐름을 명시합니다.
첫째 스키마와 테이블 파악, 둘째 컬럼 정보 확인, 셋째 SQL 실행, 넷째 결과를 자연어로 설명입니다.
규칙으로 LIMIT 사용, 큰 테이블은 샘플링, 마크다운 표 정리를 명시합니다.
사용 예시가 매우 강력합니다.
지난주 가장 많이 팔린 상품 top 5를 물으면 Claude가 자동으로 list_tables로 테이블을 발견하고 describe_table로 컬럼을 파악합니다.
JOIN과 GROUP BY가 포함된 정교한 SQL을 자동 생성해 query로 실행합니다.
결과를 마크다운 표로 정리해 응답합니다.
다양한 질문이 가능합니다.
신규 가입자, 지역별 매출, 재고, VIP 고객 패턴 같은 분석이 자연어 한 줄로 가능합니다.
안전 장치 5가지를 적용해 프로덕션에서도 안전합니다.
read-only DB user, LIMIT 강제, 시간 제한, 로그 기록, 사용자별 권한입니다.
