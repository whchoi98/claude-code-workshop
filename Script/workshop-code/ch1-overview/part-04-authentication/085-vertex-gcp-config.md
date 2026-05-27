# Slide 85: Vertex GCP 설정

**Part 4: AUTHENTICATION**

## Code Blocks

### GCP setup

```bash
# 1. Vertex AI API 활성화
gcloud services enable aiplatform.googleapis.com \
  --project=my-gcp-project

# 2. Anthropic 모델 활성화 (Vertex Model Garden)
# Console > Vertex AI > Model Garden > Claude
# > "Enable" 버튼 클릭

# 3. IAM 권한 부여 (Service Account 또는 사용자)
gcloud projects add-iam-policy-binding my-gcp-project \
  --member="user:dev@example.com" \
  --role="roles/aiplatform.user"

# 4. 사용 사례 신청 (대규모 사용 시)
# Console > Vertex AI > Anthropic Models > Submit use case

# 5. 검증
gcloud ai models list --region=us-east5
```

## Speaker Notes

Vertex AI를 사용하기 전 GCP 측 사전 설정 단계입니다.
1단계 Vertex AI API인 aiplatform.googleapis.com을 gcloud services enable 명령으로 활성화합니다.
2단계 Vertex AI Console의 Model Garden 메뉴에서 Anthropic Claude 모델을 찾아 Enable 버튼을 누릅니다.
3단계 IAM 권한 부여인데, 모델 호출 사용자나 Service Account에 roles/aiplatform.user 역할을 부여합니다.
4단계 대규모 사용을 계획한다면 Vertex AI의 Anthropic Models 페이지에서 사용 사례를 제출하면 더 높은 쿼터를 받을 수 있습니다.
5단계 gcloud ai models list로 사용 가능한 모델 목록을 확인해 정상 설정을 검증합니다.
한 번 설정하면 같은 GCP 프로젝트 내 모든 IAM 사용자가 사용 가능합니다.
