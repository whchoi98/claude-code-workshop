# Slide 94: Audit identity events

**Part 6: SSO & IDENTITY INTEGRATION**

## Code Blocks

### Identity audit

```bash
# CloudTrail에서 자동 기록되는 신원 이벤트
- AssumeRoleWithSAML (SSO 로그인)
- AssumeRole (Role 전환)
- GetSessionToken (임시 자격증명 발급)
- ConsoleLogin (Console 직접 로그인)

# 이상 패턴 탐지 쿼리 (CloudWatch Insights)
fields @timestamp, eventName, userIdentity.principalId,
       sourceIPAddress, userAgent
| filter eventSource = "signin.amazonaws.com"
   or eventSource = "sts.amazonaws.com"
| filter eventName = "AssumeRoleWithSAML"
| stats count() as logins by principalId,
   sourceIPAddress, bin(1h)
| sort logins desc

# 알람 조건
- 1시간 내 같은 사용자 5개 이상 IP에서 로그인 → 알람
- 비정상 시간대 (새벽 3시 등) 로그인 → 알람
- 해외 IP에서 로그인 → 알람 (지오 펜싱)
- 실패 5회 연속 → 계정 일시 잠금
```

## Speaker Notes

신원 이벤트 감사 방법입니다.
CloudTrail이 자동으로 기록하는 신원 이벤트는 4가지입니다.
AssumeRoleWithSAML은 SSO 로그인을 기록합니다.
AssumeRole은 Role 전환을 기록합니다.
GetSessionToken은 임시 자격증명 발급을 기록합니다.
ConsoleLogin은 Console 직접 로그인을 기록합니다.
이상 패턴 탐지를 CloudWatch Insights 쿼리로 수행합니다.
signin이나 sts 이벤트 소스를 필터링하고 AssumeRoleWithSAML 이벤트만 추립니다.
stats count로 사용자별 소스 IP별 시간대별 로그인 횟수를 계산합니다.
정렬해서 비정상적으로 많은 로그인을 식별합니다.
알람 조건을 명확히 정의합니다.
1시간 내 같은 사용자가 5개 이상 IP에서 로그인하면 알람을 보냅니다.
비정상 시간대 로그인, 해외 IP 로그인, 실패 5회 연속 같은 패턴에 대응합니다.
지오 펜싱으로 허용 국가 외 로그인을 자동 차단할 수도 있습니다.
