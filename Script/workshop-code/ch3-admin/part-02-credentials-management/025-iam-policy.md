# Slide 25: IAM policy

**Part 2: CREDENTIALS MANAGEMENT**

## Code Blocks

### IAM Policy

```bash
# bedrock-claude-code-policy.json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "InvokeAnthropicModels",
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": [
        "arn:aws:bedrock:*::foundation-model/anthropic.claude-sonnet-4-5*",
        "arn:aws:bedrock:*::foundation-model/anthropic.claude-haiku-4-5*"
      ]
    },
    {
      "Sid": "ListModels",
      "Effect": "Allow",
      "Action": "bedrock:ListFoundationModels",
      "Resource": "*"
    }
  ]
}

# 적용 방법
- 사용자 IAM Group에 attach (가장 일반적)
- 또는 IAM Role + AssumeRole (단기 자격증명)
- Opus는 별도 정책으로 분리 (비용 통제)
```

## Speaker Notes

IAM 정책 설계를 살펴봅니다.
Bedrock 접근에 필요한 최소 권한 정책입니다.
InvokeAnthropicModels statement에서 bedrock:InvokeModel과 InvokeModelWithResponseStream 액션을 허용합니다.
Resource ARN으로 Sonnet과 Haiku만 허용하도록 좁힙니다.
별표 와일드카드 대신 anthropic.claude-sonnet과 haiku로 특정 모델만 명시합니다.
ListModels statement에서 모델 목록 조회를 허용해 doctor 명령이 동작하게 합니다.
적용 방법은 세 가지가 있습니다.
사용자 IAM Group에 attach하는 것이 가장 일반적입니다.
IAM Role과 AssumeRole 조합으로 단기 자격증명을 사용할 수도 있습니다.
Opus는 별도 정책으로 분리해 비용 통제를 강화합니다.
승인 받은 시니어 개발자에게만 Opus 정책을 추가로 부여하는 패턴이 흔합니다.
