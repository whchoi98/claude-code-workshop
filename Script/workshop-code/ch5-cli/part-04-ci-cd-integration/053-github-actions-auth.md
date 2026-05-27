# Slide 53: GitHub Actions / 인증

**Part 4: CI/CD 통합**

## Code Blocks

### GH auth

```bash
# 1. GitHub Secrets 설정
# Repository → Settings → Secrets and variables → Actions
# Name: ANTHROPIC_API_KEY
# Value: sk-ant-api03-...

# 2. Organization Secret (여러 repo 공유)
# Organization → Settings → Secrets → Actions
# - 모든 또는 특정 repo에 자동 적용

# 3. Environment Secret (환경별 분리)
# Repository → Settings → Environments
# - production: API_KEY_PROD
# - staging:    API_KEY_STAGE

# 4. Bedrock 사용 시
# AWS_ROLE_ARN              # OIDC로 임시 자격증명
# AWS_REGION
# CLAUDE_CODE_USE_BEDROCK=1

# 5. Vertex AI 사용 시
# GCP_WORKLOAD_IDENTITY_POOL
# CLAUDE_CODE_USE_VERTEX=1
# CLOUD_ML_REGION=us-central1

# 6. workflow에서 사용
# .github/workflows/example.yml
jobs:
  review:
    runs-on: ubuntu-latest
    environment: production    # environment secret 사용
    steps:
      - uses: actions/checkout@v4
      - name: Setup
        run: |
          npm install -g @anthropic-ai/claude-code
      - name: Call Claude
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p "리뷰" --output-format json
```

## Speaker Notes

GitHub Actions의 인증 설정 4가지 패턴입니다.
1번 GitHub Secrets는 가장 기본입니다.
Repository Settings의 Secrets and variables에서 ANTHROPIC_API_KEY를 추가합니다.
2번 Organization Secret은 여러 repo에서 공유할 때 사용합니다.
Organization Settings의 Secrets에 등록하면 모든 또는 특정 repo에 자동 적용됩니다.
3번 Environment Secret은 환경별 분리에 적합합니다.
production과 staging에 다른 API key를 사용할 수 있습니다.
4번 Bedrock 사용 시는 AWS OIDC 패턴이 권장됩니다.
AWS_ROLE_ARN으로 임시 자격증명을 받아 보안이 강화됩니다.
5번 Vertex AI 사용 시도 동일한 OIDC 패턴이 적용됩니다.
workflow에서는 env 블록에 secrets context로 환경변수를 주입합니다.
environment 키워드로 environment secret을 활성화할 수 있습니다.
