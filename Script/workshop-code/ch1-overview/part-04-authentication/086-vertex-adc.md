# Slide 86: Vertex 자격증명 (ADC)

**Part 4: AUTHENTICATION**

## Code Blocks

### ADC

```bash
# 1. 개발자 워크스테이션 - 가장 일반적
gcloud auth application-default login
# 브라우저 열림 > GCP 계정 로그인 > 동의

# 자격증명 파일 위치 (자동 저장)
#   ~/.config/gcloud/application_default_credentials.json

# 2. Service Account (CI/CD 등)
gcloud iam service-accounts create claude-code-sa \
  --display-name "Claude Code SA"

gcloud projects add-iam-policy-binding my-gcp-project \
  --member="serviceAccount:claude-code-sa@my-gcp-project.iam.gserviceaccount.com" \
  --role="roles/aiplatform.user"

# Service Account 키 생성 + 환경변수
gcloud iam service-accounts keys create sa-key.json \
  --iam-account=claude-code-sa@my-gcp-project.iam.gserviceaccount.com
export GOOGLE_APPLICATION_CREDENTIALS=$(pwd)/sa-key.json
```

## Speaker Notes

Vertex AI 자격증명의 핵심은 Application Default Credentials, 즉 ADC 패턴입니다.
1단계 개발자 워크스테이션에서는 gcloud auth application-default login 명령으로 가장 쉽게 설정할 수 있습니다.
브라우저가 열리고 GCP 계정 로그인 후 동의하면 자격증명이 ~/.config/gcloud 디렉토리에 자동 저장됩니다.
2단계 CI/CD 같은 비대화형 환경에서는 Service Account를 사용합니다.
먼저 SA를 생성하고 aiplatform.user 권한을 부여한 후, 키 파일을 다운받아 GOOGLE_APPLICATION_CREDENTIALS 환경변수에 경로를 지정합니다.
GKE 클러스터 내에서 실행한다면 Workload Identity를 사용해 키 파일 없이 자동 인증되는 방식이 가장 안전합니다.
