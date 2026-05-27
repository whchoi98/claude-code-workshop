# Slide 85: Okta integration

**Part 6: SSO & IDENTITY INTEGRATION**

## Code Blocks

### Okta + AWS

```bash
# 1. Okta Admin Console에서 SAML App 생성
Applications → Add Application → AWS Account Federation
또는: Create App Integration → SAML 2.0

# 2. SAML 설정
SSO URL: https://signin.aws.amazon.com/saml
Audience URI: urn:amazon:webservices
Name ID Format: EmailAddress

# Attribute Statements
- https://aws.amazon.com/SAML/Attributes/Role
  = arn:aws:iam::123:role/ClaudeCodeRole,
    arn:aws:iam::123:saml-provider/Okta
- https://aws.amazon.com/SAML/Attributes/RoleSessionName
  = user.email

# 3. Group Mapping (Okta groups → AWS Roles)
- okta_developers → ClaudeCodeRole (allows Sonnet, Haiku)
- okta_seniors → ClaudeCodeAdvancedRole (allows all models)

# 4. 사용자 흐름
1. https://company.okta.com 로그인
2. AWS Account Federation 클릭
3. 자동으로 AWS Console 또는 CLI 자격증명 발급
4. Claude Code 실행 → Bedrock 자동 사용

# 5. saml2aws CLI 도구 활용 (옵션)
```

## Speaker Notes

Okta 연동 방법입니다.
IdP 시장 선도 솔루션과 AWS Bedrock 통합 패턴입니다.
1단계 Okta Admin Console에서 SAML App을 생성합니다.
Applications에서 AWS Account Federation을 선택하거나 새 SAML 2.0 앱을 만듭니다.
2단계 SAML 설정을 입력합니다.
SSO URL은 AWS 표준 signin.aws.amazon.com saml입니다.
Audience URI는 urn amazon webservices입니다.
3단계 Attribute Statements를 추가합니다.
Role 속성에 AWS Role ARN과 SAML provider ARN을 콤마로 연결해 명시합니다.
RoleSessionName으로 user.email을 매핑합니다.
4단계 Group Mapping을 설정합니다.
Okta의 okta_developers 그룹은 ClaudeCodeRole로 매핑되어 Sonnet과 Haiku만 사용 가능합니다.
okta_seniors 그룹은 Advanced Role로 매핑되어 모든 모델을 사용할 수 있습니다.
5단계 사용자 흐름입니다.
Okta에 로그인하고 AWS Account Federation을 클릭하면 자동으로 자격증명이 발급됩니다.
saml2aws 같은 CLI 도구로 명령행에서도 자동화 가능합니다.
