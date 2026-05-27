# Slide 65: Devcontainer Setup

**Part 3: INSTALLATION**

## Code Blocks

### .devcontainer/devcontainer.json

```json
// .devcontainer/devcontainer.json
{
  "name": "Claude Code Dev",
  "image": "anthropic/claude-code:latest",
  "features": {
    "ghcr.io/devcontainers/features/git:1": {},
    "ghcr.io/devcontainers/features/github-cli:1": {}
  },
  "containerEnv": {
    "ANTHROPIC_API_KEY": "${localEnv:ANTHROPIC_API_KEY}"
  },
  "mounts": [
    "source=${localEnv:HOME}/.claude,target=/root/.claude,type=bind"
  ],
  "postCreateCommand": "claude doctor",
  "customizations": {
    "vscode": {
      "extensions": ["anthropic.claude-code"]
    }
  }
}
```

## Speaker Notes

Devcontainer는 VS Code에서 표준화된 개발 환경을 정의하는 방식입니다.
프로젝트 루트의 .devcontainer/devcontainer.json 파일에 환경 사양을 기술하면, VS Code에서 Reopen in Container 명령으로 자동으로 격리된 컨테이너 환경에 진입합니다.
화면 예시처럼 image에 Anthropic 공식 이미지를 지정하고, features 섹션으로 Git과 gh CLI를 자동 설치하며, containerEnv로 호스트의 환경변수를 전달합니다.
mounts 섹션은 호스트의 ~/.claude 디렉토리를 컨테이너 내부에 마운트해 인증 상태와 세션이 컨테이너 재생성 시에도 유지되도록 합니다.
postCreateCommand로 claude doctor를 자동 실행해 환경 검증까지 자동화합니다.
마지막으로 customizations에서 VS Code 확장도 자동 설치합니다.
팀 전체가 동일한 환경을 즉시 얻을 수 있어 온보딩 시간이 크게 단축됩니다.
