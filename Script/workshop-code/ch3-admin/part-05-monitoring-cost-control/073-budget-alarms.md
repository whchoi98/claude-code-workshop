# Slide 73: Budget alarms

**Part 5: MONITORING & COST CONTROL**

## Code Blocks

### AWS Budgets

```bash
# AWS Budgets로 자동 알람 설정
aws budgets create-budget \
  --account-id 123456789012 \
  --budget '{
    "BudgetName": "ClaudeCode-Monthly",
    "BudgetLimit": { "Amount": "500", "Unit": "USD" },
    "TimeUnit": "MONTHLY",
    "BudgetType": "COST",
    "CostFilters": {
      "Service": ["Amazon Bedrock"]
    }
  }' \
  --notifications-with-subscribers '[
    {
      "Notification": {
        "NotificationType": "ACTUAL",
        "ComparisonOperator": "GREATER_THAN",
        "Threshold": 80,
        "ThresholdType": "PERCENTAGE"
      },
      "Subscribers": [
        { "SubscriptionType": "EMAIL",
          "Address": "admin@company.com" },
        { "SubscriptionType": "SNS",
          "Address": "arn:aws:sns:...:claude-alerts" }
      ]
    }
  ]'

# 다단계 임계치
# 50% / 80% / 100% / 120% 별로 다른 액션
```

## Speaker Notes

예산 알람 자동 설정 방법입니다.
AWS Budgets로 한도 초과를 자동 감지하고 알림을 보냅니다.
aws budgets create-budget 명령으로 예산을 생성합니다.
BudgetName을 ClaudeCode-Monthly로 명명합니다.
BudgetLimit을 500달러로 설정합니다.
TimeUnit MONTHLY로 월 단위 추적입니다.
CostFilters에 Amazon Bedrock 서비스만 포함시킵니다.
notifications-with-subscribers로 알림을 구성합니다.
ThresholdType을 PERCENTAGE로 80퍼센트 임계치를 설정합니다.
Subscribers로 이메일과 SNS topic을 함께 등록합니다.
이메일은 Admin에게 직접 발송되고 SNS topic은 자동화에 연결할 수 있습니다.
다단계 임계치를 권장합니다.
50퍼센트는 정보성 알림, 80퍼센트는 경고, 100퍼센트는 위험, 120퍼센트는 자동 차단 같은 식으로 단계별 다른 액션을 트리거합니다.
