# Slide 87: Google Workspace integration

**Part 6: SSO & IDENTITY INTEGRATION**

## Code Blocks

### Google Workspace

```bash
# 옵션 A: GCP Vertex AI 직접 사용 (가장 간단)
# Workspace 사용자가 자동으로 GCP IAM 사용자
# 추가 SSO 설정 불필요

# 옵션 B: AWS Bedrock + Workspace SAML
# 1. Google Admin → Apps → Web and mobile apps
# 2. Add custom SAML app
# Service provider details
ACS URL: https://signin.aws.amazon.com/saml
Entity ID: urn:amazon:webservices
Name ID: Primary email

# 3. Attribute mapping
Primary email → https://aws.amazon.com/SAML/Attributes/RoleSessionName
Custom attribute "aws_roles" → Role attribute

# 4. Workspace 사용자 속성에 aws_roles 추가
# Admin → Users → 사용자 선택 → Custom attribute

# 5. 사용 흐름
1. Google 계정으로 로그인 (Workspace 통합 SSO)
2. 앱 카탈로그에서 AWS 클릭
3. AWS Console 자동 로그인
4. Claude Code 사용
```

## Speaker Notes

Google Workspace 연동 방법입니다.
두 가지 옵션이 있습니다.
옵션 A는 GCP Vertex AI 직접 사용입니다.
Workspace 사용자는 자동으로 GCP IAM 사용자가 되므로 추가 SSO 설정이 불필요합니다.
가장 간단한 옵션입니다.
옵션 B는 AWS Bedrock과 Workspace SAML 통합입니다.
1단계 Google Admin에서 Apps의 Web and mobile apps로 이동합니다.
2단계 Add custom SAML app으로 AWS용 앱을 만듭니다.
ACS URL, Entity ID, Name ID를 AWS 표준 값으로 입력합니다.
3단계 Attribute mapping을 설정합니다.
Primary email을 RoleSessionName으로 매핑하고 사용자 정의 속성 aws_roles를 Role attribute로 매핑합니다.
4단계 Workspace 사용자 속성에 aws_roles를 추가합니다.
Admin Console에서 각 사용자별로 어떤 AWS Role을 가질지 명시합니다.
5단계 사용자는 Google 계정으로 로그인한 후 앱 카탈로그에서 AWS를 클릭하면 자동 로그인됩니다.
