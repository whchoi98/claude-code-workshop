# Slide 108: 인증 문제 진단

**Part 7: 디버깅과 트러블슈팅**

## Code Blocks

### auth issues

```bash
# Symptom: "Authentication failed" or 401 Unauthorized

# 진단 1: API key 확인
$ echo "${ANTHROPIC_API_KEY:0:15}..."    # 일부만 표시
# 잘못된 예: 빈 값, 형식 오류, 따옴표 포함

# 진단 2: API key 직접 테스트
$ curl -sS https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{"model":"claude-haiku-4-5","max_tokens":10,"messages":[{"role":"user","content":"hi"}]}' \
    | jq .

# 401 응답: API key가 유효하지 않음
# 200 응답: API key는 유효, 다른 문제

# Bedrock 401/403 시
$ aws sts get-caller-identity
# 응답이 있으면 자격증명 OK
# ExpiredToken이면 SSO 재로그인

$ aws bedrock list-foundation-models --region us-east-1 \
    | jq '.modelSummaries[] | select(.modelId | contains("claude"))'
# Claude 모델이 활성화되었는지 확인

# Vertex AI 401 시
$ gcloud auth application-default login
$ gcloud auth list

# 진단 3: doctor로 종합 확인
$ claude doctor --verbose | grep -i auth

# 해결 패턴
1. API key 새로 발급 (Anthropic Console)
2. 환경변수 재export
3. Bedrock: aws sso login
4. Vertex: gcloud auth login
5. settings.json의 model이 region과 일치하는지
```

## Speaker Notes

인증 문제 진단입니다.
401 Unauthorized 에러가 가장 흔합니다.
진단 1은 API key 확인입니다.
echo 명령으로 일부만 표시해 안전하게 확인합니다.
빈 값, 형식 오류, 따옴표 포함 같은 일반 실수를 찾습니다.
진단 2는 curl로 API를 직접 호출합니다.
API key가 유효하면 200 응답, 그렇지 않으면 401이 옵니다.
200이지만 claude 명령은 실패한다면 Claude Code 자체 문제입니다.
Bedrock에서 401이나 403이 발생하면 aws sts get-caller-identity로 자격증명을 확인합니다.
ExpiredToken이면 SSO 재로그인이 필요합니다.
aws bedrock list-foundation-models로 Claude 모델 활성화 여부도 확인합니다.
Vertex AI는 gcloud auth로 인증 상태를 확인합니다.
진단 3는 claude doctor의 verbose 출력에서 auth 섹션을 확인합니다.
해결 패턴 5가지를 정리합니다.
API key 재발급, 환경변수 재export, AWS SSO 로그인, GCP 인증, 모델과 region 일치 확인이 표준 흐름입니다.
