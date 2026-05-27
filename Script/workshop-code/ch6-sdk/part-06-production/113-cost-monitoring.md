# Slide 113: 비용 모니터링

**Part 6: PRODUCTION 운영**

## Code Blocks

### cost monitoring

```python
# 1. 호출별 비용 기록 (DB)
import sqlalchemy as sa
from datetime import datetime

usage_table = sa.Table(
    "claude_usage", metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("timestamp", sa.DateTime, default=datetime.utcnow),
    sa.Column("user_id", sa.String, index=True),
    sa.Column("model", sa.String),
    sa.Column("input_tokens", sa.Integer),
    sa.Column("output_tokens", sa.Integer),
    sa.Column("cache_read_tokens", sa.Integer, default=0),
    sa.Column("cost_usd", sa.Numeric(10, 6)),
)

# 2. 자동 기록
def record_usage(user_id, response):
    cost = calculate_cost(response)
    session.execute(usage_table.insert().values(
        user_id=user_id, model=response.model,
        input_tokens=response.usage.input_tokens,
        output_tokens=response.usage.output_tokens,
        cache_read_tokens=response.usage.cache_read_input_tokens,
        cost_usd=cost,
    ))
    session.commit()

# 3. CloudWatch Alarm (일일 한도)
import boto3
cw = boto3.client("cloudwatch")
cw.put_metric_alarm(
    AlarmName="claude-daily-cost-high",
    MetricName="DailyCost",
    Namespace="ClaudeApp",
    Statistic="Sum",
    Period=3600,
    EvaluationPeriods=1,
    Threshold=100.0,
    ComparisonOperator="GreaterThanThreshold",
    AlarmActions=["arn:aws:sns:us-east-1:123:claude-alerts"],
)

# 4. 사용자별 사전 차단
def check_budget(user_id, monthly_limit):
    used = session.execute("""
        SELECT SUM(cost_usd) FROM claude_usage
        WHERE user_id = :uid
          AND timestamp >= date_trunc('month', CURRENT_DATE)
    """, {"uid": user_id}).scalar() or 0
    if used >= monthly_limit:
        raise Exception(f"Monthly budget exceeded: ${used:.2f}/${monthly_limit}")
    return True

# 사용
def call_claude_with_budget(user_id, prompt):
    check_budget(user_id, monthly_limit=10.0)
    response = client.messages.create(...)
    record_usage(user_id, response)
    return response

# 5. 일일 리포트 자동 생성
def daily_cost_report():
    return session.execute("""
        SELECT user_id, model, COUNT(*) as calls,
               SUM(cost_usd) as cost
        FROM claude_usage
        WHERE timestamp >= CURRENT_DATE
        GROUP BY user_id, model
        ORDER BY cost DESC
    """).fetchall()
```

## Speaker Notes

비용 모니터링과 통제 패턴입니다.
호출별 비용 기록을 DB에 합니다.
claude_usage 테이블에 timestamp, user_id, model, 토큰, cost_usd를 저장합니다.
user_id에 index를 두어 사용자별 조회를 빠르게 합니다.
호출 후 자동 기록 함수입니다.
record_usage에서 cost를 계산하고 모든 토큰 정보와 함께 insert합니다.
cache_read_tokens도 별도 컬럼으로 추적해 캐시 효과를 분석할 수 있습니다.
예산 알람은 CloudWatch Alarm으로 설정합니다.
DailyCost 메트릭이 100달러 초과 시 SNS topic으로 알람이 발송됩니다.
Slack이나 PagerDuty 같은 곳으로 자동 전달할 수 있습니다.
사용자별 사전 차단은 월간 한도로 구현합니다.
check_budget 함수에서 이번 달 사용량을 조회하고 한도 초과 시 예외를 던집니다.
call_claude_with_budget에서 호출 전에 budget 확인하고 호출 후 사용량을 기록합니다.
비용 폭증을 사전에 방지하는 강력한 패턴입니다.
일일 리포트도 자동 생성해 매일 메일이나 Slack으로 발송하면 운영 가시성이 크게 향상됩니다.
