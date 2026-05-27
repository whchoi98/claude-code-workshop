# Slide 110: 메트릭과 대시보드

**Part 6: PRODUCTION 운영**

## Code Blocks

### metrics

```python
# 1. CloudWatch (Python)
import boto3
from datetime import datetime

cw = boto3.client("cloudwatch")

def emit(name, value, unit="Count", dimensions=None):
    cw.put_metric_data(
        Namespace="ClaudeApp",
        MetricData=[{
            "MetricName": name, "Value": value, "Unit": unit,
            "Timestamp": datetime.utcnow(),
            "Dimensions": dimensions or [],
        }]
    )

def call_with_metrics(prompt, user_tier):
    start = time.time()
    try:
        response = client.messages.create(...)
        emit("ApiCalls", 1, "Count",
            [{"Name": "Status", "Value": "Success"},
             {"Name": "UserTier", "Value": user_tier}])
        emit("Duration", (time.time()-start)*1000, "Milliseconds",
            [{"Name": "Model", "Value": response.model}])
        emit("InputTokens", response.usage.input_tokens, "Count")
        emit("OutputTokens", response.usage.output_tokens, "Count")
        emit("Cost", calculate_cost(response), "None")
        return response
    except Exception as e:
        emit("ApiCalls", 1, "Count",
            [{"Name": "Status", "Value": "Failure"},
             {"Name": "ErrorType", "Value": type(e).__name__}])
        raise

# 2. Datadog statsd
from datadog import statsd

def call_with_datadog(prompt):
    start = time.time()
    try:
        response = client.messages.create(...)
        statsd.histogram("claude.duration_ms",
                         (time.time()-start)*1000,
                         tags=[f"model:{response.model}"])
        statsd.increment("claude.calls", tags=["status:success"])
        statsd.gauge("claude.input_tokens", response.usage.input_tokens)
        return response
    except Exception as e:
        statsd.increment("claude.calls",
            tags=["status:failure", f"error:{type(e).__name__}"])
        raise

# 3. 핵심 메트릭 종류
# - api_calls (success/failure)
# - duration_ms (p50, p95, p99)
# - input_tokens, output_tokens
# - cost (USD)
# - rate_limit_hits
# - retries

# 4. 대시보드 위젯
# - 시간별 호출 수
# - p95 응답 시간
# - 에러율 (%)
# - 일일 비용
# - 모델별 사용 분포
```

## Speaker Notes

메트릭과 대시보드 구현입니다.
1번 CloudWatch Metrics를 Python에서 사용합니다.
boto3 client로 emit 헬퍼를 만듭니다.
Namespace ClaudeApp 아래 MetricData를 put_metric_data로 전송합니다.
Dimensions로 Status, UserTier 같은 차원을 추가하면 필터링이 가능합니다.
call_with_metrics 함수에서 성공 시 ApiCalls, Duration, 토큰, Cost 메트릭을 전송합니다.
실패 시 ErrorType 차원으로 어떤 에러인지 추적합니다.
2번 Datadog는 statsd 라이브러리를 사용합니다.
histogram, increment, gauge 세 가지 타입을 사용합니다.
histogram은 응답 시간 같은 분포 분석에, increment는 카운터에, gauge는 현재 값에 사용합니다.
tags로 차원을 추가합니다.
3번 핵심 메트릭 종류는 6가지입니다.
api_calls의 success와 failure, duration_ms의 p50, p95, p99 백분위, input과 output 토큰, cost, rate_limit_hits, retries입니다.
4번 대시보드 위젯을 CloudWatch나 Grafana에 구성합니다.
시간별 호출 수, p95 응답 시간, 에러율, 일일 비용, 모델별 사용 분포 같은 그래프를 만듭니다.
비정상 패턴을 시각적으로 즉시 감지할 수 있습니다.
