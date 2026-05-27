# Slide 63: Docker Custom Image

**Part 3: INSTALLATION**

## Code Blocks

### Dockerfile

```bash
# Dockerfile
FROM anthropic/claude-code:latest

# 사내 자주 쓰는 CLI 추가
RUN apt-get update && apt-get install -y \
    jq ripgrep awscli git-lfs \
    && rm -rf /var/lib/apt/lists/*

# 사내 CLAUDE.md 템플릿 사전 배치
COPY company-CLAUDE.md /etc/claude/CLAUDE.md.template

# 사내 MCP 서버 설정
COPY mcp-config.json /etc/claude/mcp.json

ENV CLAUDE_CONFIG_DIR=/etc/claude
ENV NODE_TLS_REJECT_UNAUTHORIZED=1

WORKDIR /workspace

ENTRYPOINT ["claude"]
```

## Speaker Notes

사내에서 표준화된 환경을 배포할 때는 사용자 정의 Docker 이미지를 만드는 것이 좋습니다.
화면 예시는 사내 표준 이미지의 Dockerfile입니다.
FROM 구문으로 공식 이미지를 베이스로 삼고, RUN 명령으로 사내에서 자주 쓰는 jq, ripgrep, awscli 같은 CLI 도구를 추가합니다.
COPY 구문으로 사내 표준 CLAUDE.md 템플릿과 MCP 서버 설정을 미리 배치하고, ENV로 환경변수를 사전 설정합니다.
CLAUDE_CONFIG_DIR로 설정 파일 경로를 강제하고 NODE_TLS_REJECT_UNAUTHORIZED를 1로 강제해 인증서 검증을 보장합니다.
이렇게 만든 이미지를 사내 컨테이너 레지스트리에 푸시하면 팀원들이 한 줄로 동일한 환경에서 Claude Code를 사용할 수 있습니다.
