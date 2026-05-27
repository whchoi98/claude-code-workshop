# Slide 26: Bedrock env config

**Part 2: CREDENTIALS MANAGEMENT**

## Code Blocks

### Env config

```bash
# 1. 환경변수 설정 (개발자 PC 표준화)
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=ap-northeast-2
export AWS_PROFILE=default

# 2. 또는 ~/.aws/config 명시 (AWS CLI 표준)
[profile claude-code]
region = ap-northeast-2
role_arn = arn:aws:iam::123:role/ClaudeCodeRole
source_profile = sso-user

# 3. 자격증명은 다음 순서로 자동 감지
1. 환경변수 (AWS_ACCESS_KEY_ID 등)
2. ~/.aws/credentials 프로필
3. EC2 Instance Profile (서버 환경)
4. ECS Task Role (컨테이너)
5. EKS IRSA (쿠버네티스)

# 4. 동작 검증
$ claude doctor
  Auth:
    Provider: AWS Bedrock                        ✓
    Region:   ap-northeast-2                     ✓
    Profile:  claude-code                        ✓
    Model access: Sonnet, Haiku (Opus denied)    i
```

## Speaker Notes

Bedrock 경로를 Claude Code에 알리는 방법입니다.
1단계 환경변수를 설정합니다.
CLAUDE_CODE_USE_BEDROCK을 1로 설정하면 Bedrock 경로가 활성화됩니다.
AWS_REGION으로 리전을 명시하고 AWS_PROFILE로 사용할 프로필을 지정합니다.
2단계 또는 ~/.aws/config 파일에 명시할 수도 있습니다.
AWS CLI의 표준 설정 형식을 따릅니다.
3단계 AWS 자격증명은 다음 순서로 자동 감지됩니다.
환경변수가 가장 우선이고, credentials 파일, EC2 Instance Profile, ECS Task Role, EKS IRSA 순입니다.
4단계 동작을 검증합니다.
claude doctor 명령으로 Provider가 AWS Bedrock으로 표시되는지, Region과 Profile이 맞는지, 어떤 모델에 액세스 가능한지를 확인합니다.
예시처럼 Sonnet과 Haiku는 가능하지만 Opus는 거부된 상태가 표시될 수 있습니다.
