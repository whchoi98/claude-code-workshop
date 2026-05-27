# Slide 84: IAM Identity Center deep dive

**Part 6: SSO & IDENTITY INTEGRATION**

## Code Blocks

### IAM IC

```bash
# 1. 활성화 (한 번만)
# AWS Console → IAM Identity Center → Enable
# 자동으로 .awsapps.com URL 생성

# 2. ID source 설정
# 옵션 A: Identity Center 디렉토리 (내장)
# 옵션 B: 외부 IdP 연동 (SAML)
#   - Okta, Azure AD, Google 등 연결
#   - SCIM으로 사용자 자동 프로비저닝

# 3. Permission Set 생성 (역할 묶음)
# PowerUser-ClaudeCode:
#   - bedrock-claude-code-policy
#   - 세션 시간: 8h
#   - 인라인 정책 또는 관리형 정책 첨부

# 4. AWS 계정에 어사인먼트
# Group: developers → PowerUser-ClaudeCode → Account: prod
# Group: contractors → ReadOnly-ClaudeCode → Account: dev

# 5. 사용자 사용 흐름
$ aws sso login --profile claude
# 브라우저 자동 열림 → SSO 로그인 → 임시 자격증명
$ claude  # Bedrock 자동 연결
```

## Speaker Notes

AWS IAM Identity Center를 자세히 살펴봅니다.
AWS 신원 통합의 표준입니다.
1단계 한 번만 활성화하면 됩니다.
AWS Console에서 IAM Identity Center를 Enable하면 자동으로 awsapps.com URL이 생성됩니다.
2단계 ID source를 설정합니다.
옵션 A는 Identity Center 자체 디렉토리를 사용합니다.
옵션 B는 외부 IdP를 SAML로 연동합니다.
Okta, Azure AD, Google을 연결할 수 있고 SCIM 프로토콜로 사용자가 자동 프로비저닝됩니다.
3단계 Permission Set을 생성합니다.
예를 들어 PowerUser-ClaudeCode 권한 묶음에 Bedrock 정책을 첨부하고 세션 시간을 8시간으로 설정합니다.
4단계 그룹별로 AWS 계정에 어사인먼트합니다.
developers 그룹은 prod 계정의 PowerUser 권한을, contractors 그룹은 dev 계정의 ReadOnly 권한을 가집니다.
5단계 사용자는 aws sso login으로 한 번 로그인하면 Claude Code가 자동으로 Bedrock에 연결됩니다.
