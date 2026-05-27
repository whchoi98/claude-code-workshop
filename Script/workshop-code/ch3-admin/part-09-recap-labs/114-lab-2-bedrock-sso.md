# Slide 114: Lab 2 / Bedrock SSO

**Part 9: RECAP & 3 LABS**

## Code Blocks

### Lab 2 steps

```bash
# 1. IAM Identity Center 활성화 (AWS Console)
# Services → IAM Identity Center → Enable

# 2. Permission Set 생성
# Name: ClaudeCodeWorkshop
# AWS managed policy 또는 인라인 정책:
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["bedrock:InvokeModel", "bedrock:ListFoundationModels"],
    "Resource": [
      "arn:aws:bedrock:*::foundation-model/anthropic.claude-sonnet-4-5*",
      "arn:aws:bedrock:*::foundation-model/anthropic.claude-haiku-4-5*"
    ]
  }]
}

# 3. 사용자 생성 및 Permission Set 할당
# Workshop 그룹 → ClaudeCodeWorkshop 부여

# 4. 사용자 PC에서 SSO 로그인
$ aws sso configure  # 또는 ~/.aws/config 직접 편집
$ aws sso login --profile claude-workshop

# 5. Claude Code 실행
$ export CLAUDE_CODE_USE_BEDROCK=1
$ export AWS_PROFILE=claude-workshop
$ export AWS_REGION=us-east-1
$ claude doctor   # Provider: AWS Bedrock 확인
$ claude          # 첫 세션 시작
```

## Speaker Notes

Lab 2는 Bedrock과 SSO 통합 실습입니다.
약 30분 소요됩니다.
5단계로 진행됩니다.
1단계 AWS Console에서 IAM Identity Center를 활성화합니다.
2단계 Permission Set을 생성합니다.
ClaudeCodeWorkshop이라는 이름으로 Bedrock InvokeModel과 ListFoundationModels 권한을 부여합니다.
Sonnet과 Haiku 모델만 명시적으로 허용합니다.
3단계 사용자를 생성하고 Workshop 그룹을 만들어 Permission Set을 할당합니다.
4단계 사용자 PC에서 SSO 로그인을 합니다.
aws sso configure로 프로필을 만들고 aws sso login으로 브라우저 로그인을 진행합니다.
5단계 Claude Code를 실행합니다.
CLAUDE_CODE_USE_BEDROCK을 1로, AWS_PROFILE을 claude-workshop으로, AWS_REGION을 us-east-1로 설정합니다.
claude doctor로 Provider가 AWS Bedrock인지 확인하고 claude 명령으로 첫 세션을 시작합니다.
SSO 기반 단기 자격증명으로 Claude Code를 사용하는 표준 패턴을 직접 경험합니다.
