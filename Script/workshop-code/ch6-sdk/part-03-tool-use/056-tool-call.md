# Slide 56: 도구 호출 로깅

**Part 3: TOOL USE**

## Code Blocks

### logging

```python
# 1. 구조화 로깅
import logging
import json
from datetime import datetime

logger = logging.getLogger("tool_use")
logger.setLevel(logging.INFO)

def log_tool_call(user_id, tool, input, output, duration_ms, error=None):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        "tool": tool,
        "input": input,
        "output_truncated": str(output)[:500] if output else None,
        "duration_ms": duration_ms,
        "error": error,
        "is_success": error is None,
    }
    logger.info(json.dumps(log_entry))

# 2. 감사 로그
import sqlalchemy as sa

audit_log = sa.Table(
    "tool_audit_log",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("timestamp", sa.DateTime, default=datetime.utcnow),
    sa.Column("user_id", sa.String, index=True),
    sa.Column("session_id", sa.String, index=True),
    sa.Column("tool", sa.String, index=True),
    sa.Column("input", sa.JSON),
    sa.Column("output", sa.JSON),
    sa.Column("duration_ms", sa.Integer),
    sa.Column("error", sa.Text, nullable=True),
)

def log_to_db(user_id, session_id, tool, input, output, duration_ms, error=None):
    session.execute(audit_log.insert().values(
        user_id=user_id, session_id=session_id, tool=tool,
        input=input, output=output[:1000] if output else None,
        duration_ms=duration_ms, error=error,
    ))
    session.commit()

# 3. 통합 실행 wrapper
def execute_and_log(user_id, session_id, name, input, funcs):
    start = time.time()
    error = None
    output = None

    try:
        output = funcs[name](**input)
    except Exception as e:
        error = f"{type(e).__name__}: {e}"

    duration_ms = int((time.time() - start) * 1000)

    log_tool_call(user_id, name, input, output, duration_ms, error)
    log_to_db(user_id, session_id, name, input, output, duration_ms, error)

    if error:
        return {"error": error, "is_error": True}
    return output

# 4. 분석 쿼리 예시
# 자주 사용되는 도구
SELECT tool, COUNT(*) as count FROM tool_audit_log
GROUP BY tool ORDER BY count DESC LIMIT 10;

# 에러율
SELECT tool,
       COUNT(CASE WHEN error IS NOT NULL THEN 1 END) * 1.0 / COUNT(*) as err_rate
FROM tool_audit_log GROUP BY tool;
```

## Speaker Notes

도구 호출 로깅으로 감사와 디버깅을 가능하게 합니다.
1번 구조화 로깅은 JSON 형식으로 stdout이나 파일에 출력합니다.
log_tool_call 함수에 user_id, tool, input, output, duration_ms, error를 받아 구조화 dict를 만들고 JSON으로 logging합니다.
output은 truncated 처리해 로그 크기를 통제합니다.
2번 감사 로그는 데이터베이스에 영구 저장합니다.
SQLAlchemy로 tool_audit_log 테이블을 정의합니다.
user_id, session_id, tool, input, output, duration_ms, error 필드와 timestamp 자동 생성으로 모든 호출이 추적됩니다.
user_id, session_id, tool 컬럼에 index를 두어 검색을 빠르게 합니다.
3번 통합 실행 wrapper는 execute_and_log입니다.
시간 측정, 도구 실행, 에러 캡처, 로깅, DB 기록을 한 함수에서 모두 처리합니다.
모든 도구 호출이 이 함수를 통과하므로 일관된 추적이 가능합니다.
4번 분석 쿼리 예시를 봅니다.
자주 사용되는 도구 top 10이나 도구별 에러율 같은 분석이 SQL로 즉시 가능합니다.
운영 대시보드에 활용할 수 있는 메트릭의 기반입니다.
