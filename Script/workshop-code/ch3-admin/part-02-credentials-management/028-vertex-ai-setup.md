# Slide 28: Vertex AI setup

**Part 2: CREDENTIALS MANAGEMENT**

## Code Blocks

### Vertex AI

```bash
# 1. Vertex AI에서 Anthropic 모델 활성화
# Google Cloud Console → Vertex AI → Model Garden
# Anthropic 패밀리 모델 활성화 요청

# 2. 서비스 계정 또는 사용자 권한
# 필요 권한:
#   - aiplatform.endpoints.predict
#   - aiplatform.models.predict

gcloud projects add-iam-policy-binding PROJECT_ID \
  --member='user:dev@company.com' \
  --role='roles/aiplatform.user'

# 3. 환경 설정
export CLAUDE_CODE_USE_VERTEX=1
export ANTHROPIC_VERTEX_PROJECT_ID=my-gcp-project
export CLOUD_ML_REGION=us-east5

# 4. ADC 로그인 (Application Default Credentials)
$ gcloud auth application-default login
# 브라우저 로그인 후 사용 가능

# 5. 검증
$ claude doctor
  Auth:
    Provider: Google Vertex AI                ✓
    Project: my-gcp-project                   ✓
    Region: us-east5                          ✓
```

## Speaker Notes

Google Vertex AI 설정 방법입니다.
GCP 환경을 사용하는 조직에 적합한 옵션입니다.
1단계 Vertex AI에서 Anthropic 모델을 활성화합니다.
Google Cloud Console의 Vertex AI Model Garden에서 Anthropic 패밀리 모델 활성화를 요청합니다.
2단계 서비스 계정이나 사용자에 필요한 권한을 부여합니다.
aiplatform.endpoints.predict와 models.predict 권한이 필요합니다.
gcloud projects add-iam-policy-binding 명령으로 부여합니다.
3단계 환경 설정을 합니다.
CLAUDE_CODE_USE_VERTEX를 1로 설정하고 프로젝트 ID와 리전을 지정합니다.
권장 리전은 us-east5입니다.
4단계 ADC, 즉 Application Default Credentials로 로그인합니다.
gcloud auth application-default login 명령으로 브라우저 로그인을 진행합니다.
5단계 검증으로 claude doctor를 실행해 Provider가 Google Vertex AI로 표시되는지 확인합니다.
