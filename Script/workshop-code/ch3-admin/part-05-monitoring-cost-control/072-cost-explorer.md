# Slide 72: Cost Explorer

**Part 5: MONITORING & COST CONTROL**

## Code Blocks

### Cost Explorer

```bash
# 1. Cost Explorer에서 Bedrock 비용 필터링
# AWS Console → Cost Explorer
# Filter: Service = Amazon Bedrock

# 2. 태그 기반 비용 분리
# IAM Role에 Cost Allocation Tag 설정:
#   Team: backend
#   Project: payment-service
#   Environment: production

# CLI로 태그 기반 비용 조회
aws ce get-cost-and-usage \
  --time-period Start=2026-05-01,End=2026-05-31 \
  --granularity DAILY \
  --metrics UnblendedCost \
  --group-by Type=TAG,Key=Team \
  --filter file://filter.json

# filter.json
{
  "Dimensions": {
    "Key": "SERVICE",
    "Values": ["Amazon Bedrock"]
  }
}

# 3. 결과 (예시)
DAILY Costs by Team (May)
  Backend Team:  $245.30
  Frontend Team: $118.50
  Data Team:     $87.20
  Total:         $451.00
```

## Speaker Notes

AWS Cost Explorer를 활용한 월간 비용 분석입니다.
1단계 Cost Explorer에서 Service를 Amazon Bedrock으로 필터링합니다.
2단계 태그 기반 비용 분리를 설정합니다.
IAM Role에 Cost Allocation Tag를 부여합니다.
Team, Project, Environment 같은 차원으로 태깅합니다.
AWS CLI로 태그 기반 비용을 조회할 수 있습니다.
aws ce get-cost-and-usage 명령에 group-by 옵션으로 Team 태그를 지정합니다.
filter.json으로 Bedrock 서비스만 한정합니다.
3단계 결과를 봅니다.
Backend Team이 245달러, Frontend Team이 118달러, Data Team이 87달러로 분리되어 표시됩니다.
총 451달러입니다.
이 데이터로 부서별 chargeback이 가능합니다.
각 팀이 자기 비용을 직접 책임지면 절감 동기가 강해집니다.
