# Slide 93: AWS Bedrock 환경변수 심화

**Part 6: 환경변수와 설정**

## Code Blocks

### Bedrock env

```bash
# 기본 Bedrock 설정
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1

# 1. 특정 모델 ID 지정
export ANTHROPIC_MODEL=us.anthropic.claude-sonnet-4-5-20250514-v1:0
# 또는 inference profile
export ANTHROPIC_MODEL=us.anthropic.claude-haiku-4-5-20251017-v1:0

# 2. Cross-region inference
# us. prefix : 미국 지역 자동 분산
# eu. prefix : 유럽 지역 자동 분산
# apac. prefix : 아시아-태평양 자동 분산
export ANTHROPIC_MODEL=apac.anthropic.claude-sonnet-4-5-20250514-v1:0

# 3. EC2 Instance Profile 사용 (IAM Role)
# 자격증명 명시 없이 자동 사용
# EC2/EKS/ECS에서 권장 (key 저장 안 함)

# 4. AWS SSO 통합
$ aws sso login --profile claude-prod
$ export AWS_PROFILE=claude-prod
$ claude doctor   # AWS 자격증명 확인

# 5. STS AssumeRole (다른 계정 접근)
$ aws sts assume-role \
    --role-arn arn:aws:iam::ACCOUNT:role/ClaudeBedrockRole \
    --role-session-name claude-session > /tmp/creds
$ export AWS_ACCESS_KEY_ID=$(jq -r '.Credentials.AccessKeyId' /tmp/creds)
$ export AWS_SECRET_ACCESS_KEY=$(jq -r '.Credentials.SecretAccessKey' /tmp/creds)
$ export AWS_SESSION_TOKEN=$(jq -r '.Credentials.SessionToken' /tmp/creds)

# 6. 엔드포인트 커스터마이즈 (private link)
export BEDROCK_ENDPOINT_URL=https://bedrock-vpc.company.internal

# 7. 요청 timeout
export ANTHROPIC_BEDROCK_TIMEOUT_MS=60000
```

## Speaker Notes

AWS Bedrock 환경변수 심화입니다.
1번 특정 모델 ID 지정으로 ANTHROPIC_MODEL에 Bedrock 모델 ID를 직접 명시합니다.
2번 Cross-region inference는 prefix로 분산 지역을 선택합니다.
us는 미국, eu는 유럽, apac은 아시아-태평양 지역입니다.
각 지역의 가용 capacity를 자동 활용합니다.
3번 EC2 Instance Profile은 IAM Role 사용 방식입니다.
EC2, EKS, ECS에서 권장되며 key를 저장하지 않으므로 가장 안전합니다.
4번 AWS SSO 통합은 사내 SSO와 함께 사용됩니다.
aws sso login으로 인증 후 AWS_PROFILE을 명시합니다.
5번 STS AssumeRole은 다른 계정의 Bedrock에 접근할 때 사용합니다.
임시 자격증명 3개를 환경변수로 주입합니다.
6번 엔드포인트 커스터마이즈로 VPC endpoint를 사용 가능합니다.
인터넷 경로 없이 Private Link로 호출합니다.
7번 요청 timeout을 60초로 늘릴 수 있습니다.
큰 작업이나 느린 네트워크 환경에서 유용합니다.
