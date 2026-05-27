# Slide 91: SCIM provisioning

**Part 6: SSO & IDENTITY INTEGRATION**

## Code Blocks

### SCIM

```bash
# IAM Identity Center에서 SCIM 활성화
# Settings → Identity source → Configure SCIM
# - SCIM endpoint: https://scim.us-east-1.amazonaws.com/...
# - Access token: 시크릿 보관

# Okta SCIM 연결
# Applications → AWS SSO → Provisioning
# - Enable API integration
# - Base URL: SCIM endpoint
# - API Token: 위에서 받은 token
# - Test connection

# 자동 동기화되는 정보
- 사용자 생성/수정/삭제
- 그룹 멤버십 변경
- 사용자 속성 (email, name, dept)

# 효과
- 신입 직원 → IdP에 추가 → AWS에 자동 생성
- 퇴사자 → IdP에서 제거 → AWS에서 자동 비활성화
- 부서 이동 → IdP 그룹 변경 → AWS 권한 자동 변경

# 사람이 수동 동기화할 필요 없음
```

## Speaker Notes

SCIM 프로비저닝을 살펴봅니다.
SCIM은 System for Cross-domain Identity Management의 약자입니다.
사용자와 그룹 정보를 IdP와 AWS 사이에서 자동 동기화하는 표준 프로토콜입니다.
설정 방법은 두 단계입니다.
먼저 IAM Identity Center에서 SCIM을 활성화합니다.
Settings의 Identity source에서 Configure SCIM을 선택하면 SCIM endpoint URL과 access token이 발급됩니다.
다음 Okta에서 SCIM 연결을 설정합니다.
Applications의 AWS SSO에서 Provisioning을 켜고 Enable API integration을 선택합니다.
Base URL과 API Token에 위에서 받은 값을 입력하고 Test connection으로 확인합니다.
자동 동기화되는 정보는 사용자 CRUD, 그룹 멤버십 변경, 사용자 속성입니다.
효과는 명확합니다.
신입 직원이 IdP에 추가되면 AWS에 자동 생성됩니다.
퇴사자가 IdP에서 제거되면 AWS에서 자동 비활성화됩니다.
부서 이동 시 IdP 그룹 변경에 따라 AWS 권한이 자동 변경됩니다.
사람이 수동으로 동기화할 필요가 없습니다.
