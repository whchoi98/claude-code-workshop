# Slide 27: Bedrock SSO integration

**Part 2: CREDENTIALS MANAGEMENT**

## Code Blocks

### IAM IC + SSO

```bash
# 1. AWS Organizations + IAM Identity Center 활성화
# (구 AWS SSO)

# 2. Permission Set 생성: ClaudeCodeUser
- 정책: bedrock-claude-code-policy 첨부
- 세션 시간: 8시간 (업무 시간)

# 3. 사용자 또는 그룹에 할당
- 개발팀 그룹 → ClaudeCodeUser 권한
- 시니어 그룹 → ClaudeCodeAdvanced (Opus 포함)

# 4. 개발자 PC에서 SSO 로그인
$ aws sso login --profile claude-code
# 브라우저 OAuth 로그인 → 임시 자격증명 발급

# 5. Claude Code 사용
$ claude
# 자동으로 SSO 자격증명 사용
# 만료 시 자동 갱신 또는 재로그인 안내

# 6. 보안 이점
- 영구 API Key 불필요
- 8시간 후 자동 만료
- 사용자 신원 추적 가능 (CloudTrail)
- 퇴사 시 권한 즉시 회수
```

## Speaker Notes

Bedrock과 SSO 통합 방법을 살펴봅니다.
AWS IAM Identity Center 연동 패턴입니다.
1단계 AWS Organizations와 IAM Identity Center를 활성화합니다.
Identity Center는 구 AWS SSO입니다.
2단계 Permission Set을 생성합니다.
ClaudeCodeUser라는 이름으로 만들고 앞서 만든 Bedrock 정책을 첨부합니다.
세션 시간을 업무 시간인 8시간으로 설정합니다.
3단계 사용자 또는 그룹에 할당합니다.
개발팀 그룹은 기본 ClaudeCodeUser, 시니어 그룹은 Opus까지 포함된 Advanced 권한을 부여합니다.
4단계 개발자 PC에서 SSO 로그인합니다.
aws sso login 명령으로 브라우저 OAuth 로그인 후 임시 자격증명이 발급됩니다.
5단계 Claude Code를 사용하면 자동으로 SSO 자격증명이 라우팅됩니다.
만료 시 자동 갱신되거나 재로그인 안내가 나옵니다.
6단계 보안 이점은 명확합니다.
영구 API Key가 불필요하고 8시간 후 자동 만료되며 사용자 신원이 CloudTrail로 추적되고 퇴사 시 권한이 즉시 회수됩니다.
