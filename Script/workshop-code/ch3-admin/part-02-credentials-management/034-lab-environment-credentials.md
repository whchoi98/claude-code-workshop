# Slide 34: Lab environment credentials

**Part 2: CREDENTIALS MANAGEMENT**

## Code Blocks

### Workshop creds

```bash
# 시나리오: 50명 워크샵 참가자에게 임시 자격증명 분배

# 패턴 A: AWS IAM Identity Center 임시 권한
# 1. workshop-attendees 그룹에 Bedrock 정책 부여
# 2. 시작 시 SSO URL 공유
# 3. 워크샵 종료 후 그룹 제거 (권한 즉시 회수)

# 패턴 B: 일회용 API Key 분배 (PoC 용도)
# 1. 50개 키 미리 생성 (anthropic console)
# 2. 워크샵 시작 시 1인 1키 분배 (slack DM)
# 3. 워크샵 종료 후 모든 키 즉시 폐기

# 패턴 C: 공용 데모 계정 (가장 단순)
# 1. 데모용 단일 키로 모두 사용
# 2. 사용 한도 미리 설정 ($50 한도)
# 3. 권장: 워크샵 끝에 키 즉시 폐기

# 추천: 보안 요건이 강하면 A, 간단함 우선이면 C

# Lab 종료 후 체크리스트
- 모든 임시 권한 회수 확인
- 사용량 리포트 점검
- 데모 키 폐기
```

## Speaker Notes

워크샵 같은 Lab 환경에서 자격증명을 분배하는 패턴입니다.
50명 워크샵 참가자에게 임시 자격증명을 분배하는 시나리오로 살펴봅니다.
패턴 A는 AWS IAM Identity Center 임시 권한입니다.
workshop-attendees 그룹에 Bedrock 정책을 부여하고 시작 시 SSO URL을 공유합니다.
워크샵 종료 후 그룹을 제거하면 권한이 즉시 회수됩니다.
패턴 B는 일회용 API Key 분배입니다.
50개 키를 미리 생성해 워크샵 시작 시 1인 1키를 Slack DM으로 분배합니다.
워크샵 종료 후 모든 키를 즉시 폐기합니다.
패턴 C는 공용 데모 계정입니다.
데모용 단일 키로 모두 사용하며 사용 한도를 미리 50달러 같은 수준으로 설정합니다.
가장 단순하지만 사용량 추적이 어렵습니다.
보안 요건이 강하면 패턴 A를, 간단함이 우선이면 패턴 C를 추천합니다.
Lab 종료 후 임시 권한 회수, 사용량 리포트 점검, 데모 키 폐기 체크리스트를 반드시 실행하시기 바랍니다.
