# Slide 100: 환경별 설정 패턴

**Part 6: 환경변수와 설정**

## Code Blocks

### env patterns

```bash
# 1. shell 스크립트로 환경별 로드
# ~/.bin/claude-env.sh
case "$1" in
  dev)
    export ANTHROPIC_API_KEY="$DEV_API_KEY"
    export CLAUDE_CODE_LOG_LEVEL=debug
    export ANTHROPIC_MODEL=claude-haiku-4-5
    ;;
  staging)
    export CLAUDE_CODE_USE_BEDROCK=1
    export AWS_PROFILE=claude-staging
    export CLAUDE_CODE_LOG_LEVEL=info
    ;;
  prod)
    export CLAUDE_CODE_USE_BEDROCK=1
    export AWS_PROFILE=claude-prod
    export CLAUDE_CODE_LOG_LEVEL=warn
    export ANTHROPIC_MODEL=claude-sonnet-4-5
    ;;
esac

# 사용
$ source ~/.bin/claude-env.sh prod
$ claude doctor

# 2. direnv로 디렉토리별 자동 적용
# 프로젝트 폴더의 .envrc
case "$PWD" in
  */project-a/*)
    use_aws_profile claude-prod
    export ANTHROPIC_MODEL=claude-opus-4-5
    ;;
  */project-b/*)
    export ANTHROPIC_API_KEY="$DEV_API_KEY"
    ;;
esac

# 3. 사내 표준 wrapper
# /opt/company/bin/claude
#!/bin/bash
# 사내 표준 환경변수 강제 적용
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1
export NODE_EXTRA_CA_CERTS=/etc/ssl/company-ca.pem
export HTTPS_PROXY=http://proxy.company.com:8080
export NO_PROXY=localhost,.company.com
export CLAUDE_CODE_DISABLE_TELEMETRY=1

# 사용자가 임의 변경 못 하게
exec /opt/claude/node_modules/.bin/claude "$@"

# 4. Docker 컨테이너에서
# Dockerfile
FROM node:20-alpine
ENV CLAUDE_CODE_USE_BEDROCK=1
ENV AWS_REGION=us-east-1
ENV NO_PROXY=localhost
RUN npm install -g @anthropic-ai/claude-code
ENTRYPOINT ["claude"]
```

## Speaker Notes

환경별 설정 패턴 4가지입니다.
1번 shell 스크립트로 환경별 로드입니다.
case 문으로 dev, staging, prod를 분기 처리합니다.
각 환경마다 다른 API key, 모델, 로그 레벨을 export합니다.
source 명령으로 실행해 현재 셸에 적용합니다.
2번 direnv로 디렉토리별 자동 적용입니다.
.envrc 파일에 case 문으로 PWD 기반 분기를 구현합니다.
프로젝트 폴더에 들어가면 자동으로 해당 환경이 적용됩니다.
3번 사내 표준 wrapper입니다.
/opt/company/bin/claude 스크립트를 만들어 PATH에 두면 사용자가 claude를 실행할 때 항상 사내 표준 환경변수가 강제됩니다.
exec로 실제 claude 바이너리를 실행합니다.
사용자가 임의 변경할 수 없게 통제할 수 있습니다.
4번 Docker 컨테이너 패턴입니다.
Dockerfile에 ENV로 환경변수를 명시합니다.
컨테이너 시작 시 자동 적용되며 격리된 환경에서 일관성이 보장됩니다.
ENTRYPOINT를 claude로 설정하면 컨테이너 자체가 claude 명령처럼 동작합니다.
