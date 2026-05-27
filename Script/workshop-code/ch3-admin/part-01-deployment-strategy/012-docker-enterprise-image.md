# Slide 12: Docker enterprise image

**Part 1: DEPLOYMENT STRATEGY**

## Code Blocks

### Enterprise Dockerfile

```bash
# Dockerfile - 사내 표준 이미지
FROM anthropic/claude-code:1.5.0   # 버전 고정

# 사내 CA 인증서 설치
COPY company-ca.crt /usr/local/share/ca-certificates/
RUN update-ca-certificates

# 사내 자주 사용하는 CLI 추가
RUN apt-get update && apt-get install -y \
    jq ripgrep awscli git-lfs gh \
    && rm -rf /var/lib/apt/lists/*

# 사내 표준 CLAUDE.md 템플릿
COPY company-CLAUDE.md /etc/claude/templates/CLAUDE.md

# 사내 MCP 서버 사전 설정
COPY mcp-config.json /etc/claude/mcp.json

# 환경변수 사전 설정
ENV CLAUDE_CONFIG_DIR=/etc/claude
ENV NODE_EXTRA_CA_CERTS=/usr/local/share/ca-certificates/company-ca.crt
ENV HTTPS_PROXY=https://proxy.company.com:8080

WORKDIR /workspace
ENTRYPOINT ["claude"]
```

## Speaker Notes

사내 표준 Docker 이미지 구축을 살펴봅니다.
Dockerfile은 anthropic/claude-code 공식 이미지를 베이스로 합니다.
버전을 1.5.0처럼 명시적으로 고정하는 것이 중요합니다.
사내 CA 인증서를 설치합니다.
company-ca.crt를 시스템 인증서 저장소에 추가하고 update-ca-certificates로 갱신합니다.
사내에서 자주 쓰는 CLI 도구들을 추가합니다.
jq, ripgrep, awscli, git-lfs, gh 같은 도구가 표준 포함됩니다.
사내 표준 CLAUDE.md 템플릿을 /etc/claude/templates에 배치합니다.
사내 MCP 서버 설정도 사전에 포함시킵니다.
환경변수로 CLAUDE_CONFIG_DIR을 명시하고 NODE_EXTRA_CA_CERTS로 인증서를 설정하며 HTTPS_PROXY로 사내 프록시를 강제합니다.
이 이미지를 사내 컨테이너 레지스트리에 푸시하면 팀원들이 한 줄로 동일한 환경에서 사용할 수 있습니다.
