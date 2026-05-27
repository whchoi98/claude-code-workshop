# Slide 77: API Key 환경변수

**Part 4: AUTHENTICATION**

## Code Blocks

### env vars

```bash
# Bash / Zsh
export ANTHROPIC_API_KEY="sk-ant-..."

# Fish shell
set -gx ANTHROPIC_API_KEY "sk-ant-..."

# PowerShell
$env:ANTHROPIC_API_KEY = "sk-ant-..."

# Windows cmd (영구 저장)
setx ANTHROPIC_API_KEY "sk-ant-..."

# direnv (.envrc - 프로젝트별)
export ANTHROPIC_API_KEY="sk-ant-..."
# .envrc는 .gitignore에 반드시 추가!

# .env 파일 (dotenv 라이브러리와 사용 시)
ANTHROPIC_API_KEY=sk-ant-...

# Docker / Kubernetes
docker run -e ANTHROPIC_API_KEY ...
kubectl create secret generic claude-key \
  --from-literal=ANTHROPIC_API_KEY="sk-ant-..."
```

## Speaker Notes

환경별로 API Key를 설정하는 방법을 정리했습니다.
Bash와 Zsh는 export 구문, Fish는 set -gx, PowerShell은 env: 접근, Windows cmd는 setx로 영구 저장합니다.
direnv를 사용하면 프로젝트 루트의 .envrc 파일에 키를 두고 디렉토리 진입 시 자동으로 환경변수가 적용됩니다.
.envrc는 반드시 .gitignore에 추가해 커밋되지 않도록 주의해야 합니다.
.env 파일은 dotenv 라이브러리와 함께 사용할 때 유용합니다.
Docker는 -e 플래그로 환경변수를 주입하고, Kubernetes에서는 Secret 리소스로 안전하게 관리합니다.
어떤 방식이든 키 값이 평문 파일이나 코드 저장소에 노출되지 않도록 하는 것이 핵심입니다.
