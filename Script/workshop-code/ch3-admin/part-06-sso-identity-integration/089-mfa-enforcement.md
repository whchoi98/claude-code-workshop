# Slide 89: MFA enforcement

**Part 6: SSO & IDENTITY INTEGRATION**

## Code Blocks

### MFA Policy

```bash
# 1. IdP 측 MFA 강제 (가장 강력)
# Okta: Policy → Authentication → MFA
# Azure AD: Conditional Access → Require MFA
# Google: Admin → 2-Step Verification → Enforce

# 2. AWS Role Trust Policy에 MFA 조건
{
  "Effect": "Allow",
  "Principal": {
    "Federated": "arn:aws:iam::123:saml-provider/Okta"
  },
  "Action": "sts:AssumeRoleWithSAML",
  "Condition": {
    "BoolIfExists": {
      "aws:MultiFactorAuthPresent": "true"
    }
  }
}

# 3. Bedrock 호출에 MFA 조건 (정책 수준)
{
  "Effect": "Deny",
  "Action": "bedrock:InvokeModel",
  "Resource": "*",
  "Condition": {
    "BoolIfExists": { "aws:MultiFactorAuthPresent": "false" }
  }
}

# 4. 이중 보호 효과
- IdP에서 1차 차단
- AWS에서 2차 확인
- MFA 없이는 절대 사용 불가
```

## Speaker Notes

MFA 강제 적용 방법입니다.
다중 인증을 필수화하는 다층 방어 패턴입니다.
1단계 IdP 측에서 MFA를 강제합니다.
가장 강력한 방어선입니다.
Okta는 Policy에서 Authentication MFA를 설정합니다.
Azure AD는 Conditional Access로 Require MFA를 강제합니다.
Google은 Admin에서 2-Step Verification을 Enforce합니다.
2단계 AWS Role Trust Policy에 MFA 조건을 추가합니다.
aws MultiFactorAuthPresent가 true여야 AssumeRoleWithSAML이 허용됩니다.
BoolIfExists로 안전하게 처리합니다.
3단계 Bedrock 호출에 MFA 조건을 추가합니다.
정책 수준에서 MFA가 false면 Deny합니다.
InvokeModel 호출 자체가 차단됩니다.
이중 보호 효과로 IdP에서 1차 차단되고 AWS에서 2차 확인이 됩니다.
MFA 없이는 절대 Claude Code를 사용할 수 없게 됩니다.
