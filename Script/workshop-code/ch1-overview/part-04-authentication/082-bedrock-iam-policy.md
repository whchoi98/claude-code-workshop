# Slide 82: Bedrock IAM Policy

**Part 4: AUTHENTICATION**

## Code Blocks

### IAM Policy (least privilege)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ClaudeCodeBedrockInvoke",
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": [
        "arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-sonnet-*",
        "arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-haiku-*",
        "arn:aws:bedrock:us-east-1:*:inference-profile/us.anthropic.claude-*"
      ]
    },
    {
      "Sid": "ListModelsOptional",
      "Effect": "Allow",
      "Action": ["bedrock:ListFoundationModels"],
      "Resource": "*"
    }
  ]
}
```

## Speaker Notes

Bedrock 경로로 Claude Code를 사용하려면 IAM 정책에 최소 두 가지 액션 권한이 필요합니다.
bedrock:InvokeModel은 일반 호출, bedrock:InvokeModelWithResponseStream은 SSE 스트리밍 호출에 필요합니다.
Resource는 사용할 모델 ARN을 정확히 지정하며, 와일드카드를 활용해 모델 패밀리 전체를 허용할 수 있습니다.
CRIS, 즉 inference-profile을 사용한다면 inference-profile ARN도 함께 추가합니다.
선택 사항으로 bedrock:ListFoundationModels를 추가하면 사용 가능한 모델 목록을 확인할 수 있어 디버깅에 유용합니다.
이 정책을 IAM Role이나 사용자에게 부착하면 됩니다.
최소 권한 원칙을 지키며, 더 넓은 권한은 필요할 때만 추가합니다.
