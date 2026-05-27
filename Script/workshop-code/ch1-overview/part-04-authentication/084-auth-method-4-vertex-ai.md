# Slide 84: Auth Method 4: Vertex AI

**Part 4: AUTHENTICATION**

## Code Blocks

### Google Vertex AI

```bash
# 1. Vertex AI 모드 활성화
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
export ANTHROPIC_VERTEX_PROJECT_ID=my-gcp-project

# 2. GCP 자격증명 (택1)
#  (a) Application Default Credentials (ADC)
gcloud auth application-default login

#  (b) Service Account 키 파일
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/sa-key.json

#  (c) GKE Workload Identity - 자동 감지

# 3. 모델 ID (Vertex AI 형식)
export ANTHROPIC_MODEL=claude-sonnet-4-5@20250929

# 4. 실행
claude
# > Authenticated via Vertex AI (project: my-gcp-project)
```

## Speaker Notes

네 번째 인증 방식은 Google Vertex AI를 통한 GCP 청구 경로입니다.
1단계 CLAUDE_CODE_USE_VERTEX 환경변수를 1로, CLOUD_ML_REGION을 us-east5 같은 Vertex AI 지원 리전으로 지정하고 ANTHROPIC_VERTEX_PROJECT_ID에 GCP 프로젝트 ID를 넣습니다.
2단계 자격증명은 세 가지 방식이 있습니다.
(a) gcloud auth application-default login으로 ADC를 설정하는 방식, (b) Service Account 키 파일을 GOOGLE_APPLICATION_CREDENTIALS에 지정하는 방식, (c) GKE Workload Identity로 자동 감지되는 방식. 운영 환경에서는 (c)가 가장 안전합니다.
3단계 ANTHROPIC_MODEL에 Vertex AI 형식의 모델 ID를 지정합니다.
@20250929 같은 버전 태그가 붙은 형식입니다.
