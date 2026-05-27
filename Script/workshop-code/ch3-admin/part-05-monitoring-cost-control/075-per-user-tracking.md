# Slide 75: Per-user tracking

**Part 5: MONITORING & COST CONTROL**

## Code Blocks

### Per-user

```bash
# 1. IAM Identity Center 사용자별 추적 (Bedrock)
# CloudTrail이 자동으로 사용자 신원 기록
# userIdentity.principalId에서 사용자 식별

# 2. CloudWatch Insights 쿼리
fields @timestamp, userIdentity.principalId, modelId,
       inputTokens, outputTokens
| filter eventSource = "bedrock.amazonaws.com"
| stats sum(inputTokens) as totalIn,
        sum(outputTokens) as totalOut by principalId
| sort totalOut desc
| limit 50

# 3. 결과 (예시)
principalId                 totalIn      totalOut
alice@company.com           2,450,000    180,000
bob@company.com             890,000      120,000
charlie@company.com         620,000      45,000

# 4. 월간 자동 리포트
- Lambda + EventBridge 월 1일 트리거
- 위 쿼리 실행
- 사용자별 PDF 리포트 생성
- email/Slack DM 발송

# 5. 개인별 한도 (선택)
- IAM Role 정책에 사용자별 사용량 attribute
- 한도 초과 시 자동 ask 모드 전환
```

## Speaker Notes

사용자별 비용 추적 방법입니다.
IAM Identity Center 사용 시 CloudTrail이 자동으로 사용자 신원을 기록합니다.
userIdentity의 principalId 필드에서 사용자를 식별합니다.
CloudWatch Insights로 사용자별 통계를 쿼리합니다.
fields로 필요한 컬럼을 선택하고 filter로 Bedrock 이벤트만 추립니다.
stats with sum으로 사용자별 토큰 합계를 계산하고 sort로 정렬합니다.
결과 예시를 봅니다.
alice가 가장 많이 사용하고 그 다음 bob, charlie 순입니다.
월간 자동 리포트도 가능합니다.
Lambda와 EventBridge로 매월 1일 트리거되어 위 쿼리를 실행합니다.
사용자별 PDF 리포트를 생성해 이메일이나 Slack DM으로 발송합니다.
선택적으로 개인별 한도를 적용할 수도 있습니다.
IAM Role 정책에 사용자별 사용량 attribute를 두고 한도 초과 시 자동으로 ask 모드로 전환합니다.
