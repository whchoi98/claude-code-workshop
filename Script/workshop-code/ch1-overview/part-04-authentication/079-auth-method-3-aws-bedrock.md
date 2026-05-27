# Slide 79: Auth Method 3: AWS Bedrock

**Part 4: AUTHENTICATION**

## Code Blocks

### AWS Bedrock

```bash
# 1. Bedrock 모드 활성화
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-west-2

# 2. AWS 자격증명 (택1)
#  (a) AWS_PROFILE 사용
export AWS_PROFILE=anthropic-prod

#  (b) AWS_ACCESS_KEY_ID + AWS_SECRET_ACCESS_KEY
export AWS_ACCESS_KEY_ID=AKIA...
export AWS_SECRET_ACCESS_KEY=...

#  (c) EC2/EKS IAM Role - 자동 감지

# 3. 모델 ID (Bedrock 형식)
export ANTHROPIC_MODEL=anthropic.claude-sonnet-4-5-20250929-v1:0

# 4. 실행
claude
# > Successfully authenticated via AWS Bedrock (us-west-2)
```

## Speaker Notes

세 번째 인증 방식은 AWS Bedrock입니다.
AWS 청구로 통합되어 엔터프라이즈에서 가장 선호되는 경로입니다.
1단계 CLAUDE_CODE_USE_BEDROCK 환경변수를 1로 설정해 Bedrock 모드를 활성화하고 AWS_REGION을 지정합니다.
2단계 AWS 자격증명은 세 가지 방식 중 하나를 선택합니다.
(a) AWS_PROFILE 환경변수로 프로필 지정, (b) 액세스 키와 시크릿 키 환경변수 직접 설정, (c) EC2나 EKS의 IAM Role 자동 감지. 운영 환경에서는 (c) 방식이 가장 안전합니다.
3단계 ANTHROPIC_MODEL 환경변수에 Bedrock 형식의 모델 ID를 지정합니다.
anthropic.claude-sonnet- 같은 prefix가 붙은 형식입니다.
4단계 claude 실행 시 Bedrock 인증이 완료되었다는 메시지가 표시됩니다.
