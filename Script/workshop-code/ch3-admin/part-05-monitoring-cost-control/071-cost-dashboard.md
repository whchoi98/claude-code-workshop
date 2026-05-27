# Slide 71: Cost dashboard

**Part 5: MONITORING & COST CONTROL**

## Code Blocks

### CW Dashboard

```bash
# CloudFormation으로 대시보드 자동 생성
Resources:
  ClaudeCodeDashboard:
    Type: AWS::CloudWatch::Dashboard
    Properties:
      DashboardName: ClaudeCode-Operations
      DashboardBody: !Sub |
        {
          "widgets": [
            {
              "type": "metric",
              "properties": {
                "metrics": [
                  ["AWS/Bedrock", "Invocations",
                    "ModelId", "anthropic.claude-sonnet-4-5"],
                  ["...", "InputTokenCount"],
                  ["...", "OutputTokenCount"]
                ],
                "stat": "Sum",
                "period": 300,
                "title": "Sonnet Usage (5m)"
              }
            },
            {
              "type": "metric",
              "properties": {
                "metrics": [["AWS/Bedrock", "InvocationLatency"]],
                "stat": "Average",
                "title": "Latency p50/p99"
              }
            }
          ]
        }
```

## Speaker Notes

AWS Bedrock 사용 시 CloudWatch 대시보드 구성입니다.
CloudFormation으로 대시보드를 자동 생성하는 예시입니다.
ClaudeCodeDashboard라는 이름으로 만들고 여러 widget을 정의합니다.
첫 번째 widget은 Sonnet 모델의 사용량 메트릭입니다.
Invocations, InputTokenCount, OutputTokenCount를 5분 단위로 합계 표시합니다.
stat을 Sum으로 설정하고 period를 300초로 합니다.
두 번째 widget은 응답 시간입니다.
InvocationLatency의 평균을 표시합니다.
p50과 p99 percentile도 함께 볼 수 있도록 추가할 수 있습니다.
Bedrock의 모든 메트릭은 자동으로 CloudWatch에 수집됩니다.
별도 설정 없이 대시보드만 만들면 됩니다.
조직 단위 사용 현황을 시각적으로 추적할 수 있어 의사 결정에 큰 도움이 됩니다.
