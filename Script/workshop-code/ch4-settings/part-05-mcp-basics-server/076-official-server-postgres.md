# Slide 76: Official server: postgres

**Part 5: MCP 기본과 공식 서버**

## Code Blocks

### postgres

```bash
# 1. settings.json 등록
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgres://user:pass@host:5432/dbname"
      ]
    }
  }
}

# 또는 환경변수 사용 (권장)
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_URL": "${DATABASE_URL}"
      }
    }
  }
}

# 2. 제공되는 도구
- query(sql)               - SQL 실행 (보통 read-only)
- list_tables()            - 테이블 목록
- describe_table(name)     - 테이블 스키마

# 3. 사용 예시
> 어제 주문 건수를 시간대별로 보여줘
> users 테이블에 어떤 컬럼이 있어?
> 이 쿼리를 더 효율적으로 작성해 줘 [기존 쿼리]

# 4. 보안 권장
- read-only 사용자로 연결 (DDL/DML 차단)
- production DB 직접 연결 절대 X
- 개발/스테이징 또는 replica만
```

## Speaker Notes

네 번째 공식 서버는 postgres입니다.
PostgreSQL 데이터 접근을 제공합니다.
settings.json 등록 방법은 두 가지입니다.
첫째, 연결 문자열을 args에 직접 넣는 방법입니다.
둘째, 환경변수로 분리하는 방법입니다.
환경변수가 더 안전하므로 권장됩니다.
제공되는 도구는 세 가지입니다.
query로 SQL 실행, list_tables로 목록 조회, describe_table로 스키마 확인입니다.
사용 예시를 봅니다.
어제 주문 건수를 시간대별로 보여 달라거나 users 테이블 컬럼을 확인하거나 쿼리를 더 효율적으로 작성해 달라는 요청이 가능합니다.
Claude가 자동으로 list_tables와 describe_table을 호출해 스키마를 파악한 후 적절한 query를 작성해 실행합니다.
보안 권장 사항이 매우 중요합니다.
read-only 사용자로 연결해 DDL과 DML을 차단합니다.
production DB에 직접 연결하지 마시고 개발이나 스테이징 또는 replica만 사용하시기 바랍니다.
