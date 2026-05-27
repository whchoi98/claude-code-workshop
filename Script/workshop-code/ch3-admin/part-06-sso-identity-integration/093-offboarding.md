# Slide 93: Offboarding

**Part 6: SSO & IDENTITY INTEGRATION**

## Code Blocks

### flow

```bash
# 자동화 흐름 (예시)
HR System (Workday/SuccessFactors)
   ↓ webhook 또는 SCIM
IdP (Okta/Azure AD)
   ↓ deactivate user
   ↓ SCIM
AWS IAM Identity Center
   ↓ revoke active sessions
   ↓ disable user
CloudTrail에 모든 변경 기록
```

## Speaker Notes

Offboarding 자동화는 퇴사자 권한을 즉시 회수하는 절차입니다.
5단계 흐름으로 진행됩니다.
1단계 HR 시스템에서 퇴사 처리가 됩니다.
2단계 IdP에서 사용자가 자동 비활성화됩니다.
3단계 SCIM이 AWS에 변경을 전파합니다.
4단계 모든 활성 세션이 즉시 무효화됩니다.
5단계 감사 로그가 보관됩니다.
Critical 포인트는 명확합니다.
퇴사자 권한 회수는 보안 사고의 가장 흔한 원인입니다.
HR에서 IdP를 거쳐 AWS로 이어지는 자동 흐름이 사람의 실수를 막아줍니다.
자동화 흐름은 HR System에서 시작합니다.
Workday나 SuccessFactors 같은 HR 시스템이 진실의 원천입니다.
webhook이나 SCIM으로 IdP에 전파되고 그 다음 SCIM으로 AWS에 전파됩니다.
AWS에서 active session이 revoke되고 사용자가 disable됩니다.
CloudTrail에 모든 변경이 기록되어 감사 추적이 가능합니다.
전체 회수 시간이 5분 이내로 단축됩니다.
