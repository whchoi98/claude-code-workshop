# Slide 92: 인증 환경변수

**Part 6: 환경변수와 설정**

## Code Blocks

### auth env

```bash
# 1. Anthropic Direct (기본)
$ export ANTHROPIC_API_KEY="sk-ant-api03-..."
$ claude -p "Hello"

# 2. AWS Bedrock 경로
$ export CLAUDE_CODE_USE_BEDROCK=1
$ export AWS_REGION=us-east-1
$ export AWS_ACCESS_KEY_ID=...      # 또는 AWS Profile/Role
$ export AWS_SECRET_ACCESS_KEY=...
$ export AWS_SESSION_TOKEN=...      # 임시 자격증명 (선택)
# 또는 AWS Profile
$ export AWS_PROFILE=production
$ claude -p "Hello"
# 사용 모델: anthropic.claude-3-5-sonnet-20241022-v2:0

# 3. GCP Vertex AI 경로
$ export CLAUDE_CODE_USE_VERTEX=1
$ export GOOGLE_APPLICATION_CREDENTIALS=/path/to/sa.json
$ export CLOUD_ML_REGION=us-central1
$ export ANTHROPIC_VERTEX_PROJECT_ID=my-project
$ claude -p "Hello"

# 4. 다중 경로 설정 (프로젝트별)
# 프로젝트 A: Bedrock
$ cd project-a && export CLAUDE_CODE_USE_BEDROCK=1
# 프로젝트 B: Direct
$ cd project-b && unset CLAUDE_CODE_USE_BEDROCK
$ export ANTHROPIC_API_KEY="sk-..."

# 5. direnv로 자동 전환 (.envrc)
$ cat .envrc
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1
export AWS_PROFILE=this-project
$ direnv allow

# 6. 우선순위
# 환경변수 > settings.json > 기본값
```

## Speaker Notes

인증 환경변수를 3가지 경로별로 정리합니다.
1번 Anthropic Direct가 가장 기본입니다.
ANTHROPIC_API_KEY 하나만 export하면 됩니다.
2번 AWS Bedrock 경로는 더 많은 변수가 필요합니다.
CLAUDE_CODE_USE_BEDROCK을 1로 설정하고 AWS 자격증명을 주입합니다.
ACCESS_KEY와 SECRET_ACCESS_KEY를 직접 사용하거나 AWS_PROFILE로 named profile을 사용할 수 있습니다.
AWS_SESSION_TOKEN은 임시 자격증명 사용 시 추가합니다.
3번 GCP Vertex AI 경로는 GOOGLE_APPLICATION_CREDENTIALS로 service account JSON 경로를 명시합니다.
CLOUD_ML_REGION과 ANTHROPIC_VERTEX_PROJECT_ID도 필요합니다.
4번 다중 경로는 프로젝트별 다른 설정이 필요할 때 사용합니다.
export와 unset으로 변경할 수 있습니다.
5번 direnv를 사용하면 디렉토리별 자동 환경 전환이 가능합니다.
.envrc 파일에 환경변수를 정의하고 direnv allow 한 번만 실행하면 됩니다.
6번 우선순위는 환경변수, settings.json, 기본값 순입니다.
환경변수가 가장 우선이므로 임시 변경이 쉽습니다.
