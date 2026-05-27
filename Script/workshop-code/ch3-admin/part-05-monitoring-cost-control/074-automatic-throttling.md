# Slide 74: Automatic throttling

**Part 5: MONITORING & COST CONTROL**

## Code Blocks

### Auto throttle

```python
# 1. SNS topic 구독자에 Lambda 함수 등록
# Budget 100% 도달 → SNS → Lambda → IAM 정책 수정

# Lambda 함수 (Python)
import boto3, json

def lambda_handler(event, context):
    iam = boto3.client('iam')

    # 사용자 그룹에 Bedrock deny 정책 부착
    iam.attach_group_policy(
        GroupName='claude-code-users',
        PolicyArn='arn:aws:iam::123:policy/BedrockTempDeny'
    )

    # Slack/Teams 알림
    notify_slack({
        'channel': '#claude-alerts',
        'text': '🚨 월 예산 100% 초과! 사용 일시 중지됨'
    })

    return {'status': 'throttled'}

# BedrockTempDeny 정책
{
  "Effect": "Deny",
  "Action": ["bedrock:InvokeModel"],
  "Resource": "*"
}

# 다음 달 1일 자동 해제 (EventBridge schedule)
# 또는 Admin 수동 해제
```

## Speaker Notes

자동 사용량 제한 구현입니다.
한도 초과 시 자동으로 사용을 차단하는 메커니즘입니다.
SNS topic 구독자에 Lambda 함수를 등록합니다.
Budget이 100퍼센트 도달하면 SNS topic이 트리거되고 Lambda가 실행됩니다.
Lambda 함수는 Python으로 작성된 예시입니다.
boto3 클라이언트로 IAM API를 호출합니다.
claude-code-users 그룹에 BedrockTempDeny 정책을 부착합니다.
동시에 Slack이나 Teams 채널에 알림을 보냅니다.
사용자들이 갑작스러운 차단을 인지할 수 있게 합니다.
BedrockTempDeny 정책은 bedrock InvokeModel을 모든 리소스에 대해 Deny합니다.
다음 달 1일에 EventBridge schedule이 자동으로 정책을 분리합니다.
또는 Admin이 수동으로 해제할 수도 있습니다.
이 자동화로 예산 초과 위험을 완전히 통제할 수 있습니다.
