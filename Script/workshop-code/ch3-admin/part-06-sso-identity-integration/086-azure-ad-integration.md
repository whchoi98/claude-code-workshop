# Slide 86: Azure AD integration

**Part 6: SSO & IDENTITY INTEGRATION**

## Code Blocks

### Azure AD

```bash
# 1. Azure Portal → Enterprise Applications
# → AWS Single-Account Access 또는 AWS IAM Identity Center

# 2. Single Sign-On 설정 (SAML)
Identifier (Entity ID): urn:amazon:webservices
Reply URL: https://signin.aws.amazon.com/saml
Sign-on URL: https://your-domain.awsapps.com/start

# Attributes & Claims
- Role: user.assignedroles
- RoleSessionName: user.mail
- SessionDuration: 28800  (8시간)

# 3. AWS 측 IAM SAML provider 생성
aws iam create-saml-provider \
  --saml-metadata-document file://azure-metadata.xml \
  --name AzureAD-Provider

# 4. AzureAD Role 생성 (Trust policy)
{
  "Effect": "Allow",
  "Principal": {
    "Federated": "arn:aws:iam::123:saml-provider/AzureAD-Provider"
  },
  "Action": "sts:AssumeRoleWithSAML",
  "Condition": {
    "StringEquals": { "SAML:aud": "https://signin.aws.amazon.com/saml" }
  }
}

# 5. AAD Group 매핑 → AWS Role attach
```

## Speaker Notes

Azure AD 연동 방법입니다.
Azure AD는 새 이름이 Entra ID로 바뀌었지만 동작은 동일합니다.
Microsoft 365 환경 통합에 적합합니다.
1단계 Azure Portal에서 Enterprise Applications로 이동합니다.
AWS Single-Account Access 또는 IAM Identity Center 앱을 추가합니다.
2단계 Single Sign-On을 SAML로 설정합니다.
Identifier, Reply URL, Sign-on URL을 AWS 표준 값으로 입력합니다.
Attributes & Claims에서 Role과 RoleSessionName, SessionDuration을 매핑합니다.
3단계 AWS 측에서 IAM SAML provider를 생성합니다.
aws iam create-saml-provider 명령에 Azure에서 다운받은 metadata XML을 전달합니다.
4단계 AzureAD Role을 생성하면서 Trust policy에 SAML provider를 명시합니다.
AssumeRoleWithSAML 액션을 허용하고 audience condition으로 보안을 강화합니다.
5단계 AAD Group을 AWS Role에 매핑합니다.
매핑된 그룹의 사용자가 자동으로 해당 Role을 받을 수 있습니다.
