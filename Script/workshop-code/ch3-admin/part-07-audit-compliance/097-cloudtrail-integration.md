# Slide 97: CloudTrail integration

**Part 7: AUDIT & COMPLIANCE**

## Code Blocks

### CloudTrail

```bash
# 1. CloudTrail이 자동 기록하는 Bedrock 이벤트
- InvokeModel (모델 호출)
- InvokeModelWithResponseStream (스트리밍)
- ListFoundationModels (모델 조회)

# 2. CloudTrail 설정 (조직 전체 권장)
aws cloudtrail create-trail \
  --name claude-code-audit-trail \
  --s3-bucket-name audit-logs-bucket \
  --is-multi-region-trail \
  --is-organization-trail \
  --enable-log-file-validation

# 3. 로그 무결성 보장
- 파일 단위 SHA-256 해시
- 일일 digest 파일에 모든 해시 기록
- digest는 CloudTrail 키로 서명
- 변조 시 즉시 탐지 가능

# 4. 기록되는 정보 예시
{
  "eventTime": "2026-05-25T10:23:45Z",
  "eventName": "InvokeModel",
  "userIdentity": { "principalId": "alice@company.com" },
  "sourceIPAddress": "10.0.1.42",
  "requestParameters": {
    "modelId": "anthropic.claude-sonnet-4-5",
    "inputTokenCount": 1240,
    "outputTokenCount": 380
  }
}
```

## Speaker Notes

CloudTrail 통합으로 Bedrock 호출이 자동 감사됩니다.
CloudTrail이 자동 기록하는 Bedrock 이벤트는 세 가지입니다.
InvokeModel은 일반 모델 호출, InvokeModelWithResponseStream은 스트리밍 호출, ListFoundationModels는 모델 조회입니다.
조직 전체 Trail 설정을 권장합니다.
aws cloudtrail create-trail 명령에 is-multi-region-trail과 is-organization-trail 옵션으로 전 조직을 커버합니다.
enable-log-file-validation으로 로그 무결성을 보장합니다.
로그 무결성 보장 방식은 정교합니다.
파일 단위로 SHA-256 해시가 계산되고 일일 digest 파일에 모든 해시가 기록됩니다.
digest는 CloudTrail 키로 서명되며 변조 시 즉시 탐지 가능합니다.
기록되는 정보 예시를 봅니다.
eventTime, eventName, userIdentity의 principalId로 누가 했는지 정확히 추적됩니다.
sourceIPAddress로 어디에서, modelId와 토큰 수로 무엇을 얼마나 사용했는지 모두 기록됩니다.
