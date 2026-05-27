# Slide 102: Audit report automation

**Part 7: AUDIT & COMPLIANCE**

## Code Blocks

### Auto report

```python
# Lambda + EventBridge로 매월 1일 자동 생성

# audit-report-generator.py
import boto3, json
from datetime import datetime, timedelta

def generate_monthly_report():
    cloudtrail = boto3.client('cloudtrail')
    end = datetime.now()
    start = end - timedelta(days=30)

    # Bedrock 이벤트 조회
    events = cloudtrail.lookup_events(
        LookupAttributes=[
            {'AttributeKey': 'EventSource', 'AttributeValue': 'bedrock.amazonaws.com'}
        ],
        StartTime=start,
        EndTime=end
    )

    # 통계 집계
    report = {
        'total_invocations': len(events['Events']),
        'unique_users': len(set(e['Username'] for e in events['Events'])),
        'by_model': {},
        'security_incidents': 0,
        'policy_violations': 0
    }

    # PDF 생성 후 S3에 저장
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket='compliance-reports',
        Key=f'monthly/{end.strftime("%Y-%m")}/audit-report.pdf',
        Body=generate_pdf(report)
    )

    # 컴플라이언스팀에 이메일
```

## Speaker Notes

감사 리포트 자동화 구현입니다.
Lambda와 EventBridge로 매월 1일 자동 생성합니다.
Python 스크립트 예시를 봅니다.
boto3 cloudtrail 클라이언트로 지난 30일 Bedrock 이벤트를 조회합니다.
lookup_events 메서드에 EventSource를 bedrock.amazonaws.com으로 필터링합니다.
통계를 집계합니다.
총 호출 횟수, unique 사용자 수, 모델별 분포, 보안 사고 횟수, 정책 위반 횟수를 계산합니다.
PDF로 생성한 후 S3 compliance-reports 버킷에 저장합니다.
월별 디렉토리에 정리되어 추적이 용이합니다.
마지막으로 컴플라이언스팀에 이메일로 배포합니다.
이 자동화로 매월 수동 작업 부담이 사라지고 컴플라이언스 감사 대응이 즉시 가능해집니다.
