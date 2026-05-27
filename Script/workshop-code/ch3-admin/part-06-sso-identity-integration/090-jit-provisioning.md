# Slide 90: JIT provisioning

**Part 6: SSO & IDENTITY INTEGRATION**

## Code Blocks

### JIT trust

```bash
# Trust Policy + Condition으로 그룹 기반 자동 매핑
{
  "Effect": "Allow",
  "Principal": { "Federated": "arn:aws:iam::123:saml-provider/Okta" },
  "Action": "sts:AssumeRoleWithSAML",
  "Condition": {
    "StringEquals": {
      "SAML:aud": "https://signin.aws.amazon.com/saml"
    },
    "ForAnyValue:StringLike": {
      "saml:groups": ["engineering-*"]
    }
  }
}
```

## Speaker Notes

JIT 프로비저닝은 Just-In-Time의 약자입니다.
사용자를 사전 등록 없이 자동으로 등록하는 패턴입니다.
5단계 흐름으로 진행됩니다.
사용자가 처음 SSO 로그인하면 IdP가 SAML 응답을 전송합니다.
AWS가 사용자를 자동으로 생성하고 그룹 매핑에 따라 Role을 부여한 후 Bedrock을 즉시 사용할 수 있게 됩니다.
장점은 명확합니다.
사용자를 AWS에 미리 등록할 필요가 없습니다.
IdP 권한만 부여하면 됩니다.
신규 직원의 첫 로그인 시 자동으로 AWS 사용자가 생성됩니다.
Trust Policy에 Condition을 추가해 그룹 기반 자동 매핑을 합니다.
ForAnyValue StringLike로 saml groups 중 engineering으로 시작하는 그룹이 있는지 확인합니다.
이 패턴으로 신입 직원이 첫날부터 Claude Code를 사용할 수 있습니다.
