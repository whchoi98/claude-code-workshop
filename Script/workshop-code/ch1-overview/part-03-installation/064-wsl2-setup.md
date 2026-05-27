# Slide 64: WSL2 Setup

**Part 3: INSTALLATION**

## Code Blocks

### WSL2

```bash
# 1. WSL2 설치 (PowerShell 관리자 권한)
wsl --install -d Ubuntu-22.04
# 재부팅 후 사용자 생성

# 2. WSL 내부에서 Ubuntu 업데이트
sudo apt update && sudo apt upgrade -y

# 3. Node.js 20 설치 (NodeSource)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# 4. npm prefix 설정 후 Claude Code 설치
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
npm install -g @anthropic-ai/claude-code

# 5. Windows-WSL 파일 시스템 주의
# /mnt/c/Users/... 보다 ~/projects 권장 (성능)
```

## Speaker Notes

Windows 사용자에게 강력히 권장되는 WSL2 환경 설정입니다.
1단계 PowerShell을 관리자 권한으로 열고 wsl --install -d Ubuntu-22.04 명령으로 WSL2와 Ubuntu를 한 번에 설치합니다.
재부팅 후 사용자를 생성합니다.
2단계부터는 Ubuntu 가이드와 동일하게 apt 업데이트, NodeSource로 Node 20 설치, npm prefix 설정, Claude Code 설치 순으로 진행합니다.
한 가지 중요한 주의사항이 있는데, WSL2에서 /mnt/c 같은 Windows 파일 시스템에 접근할 수는 있지만 성능이 크게 떨어집니다.
작업 파일은 반드시 WSL2 네이티브 파일 시스템 내, 보통 사용자 홈 아래 projects 같은 디렉토리에 두는 것이 좋습니다.
그렇지 않으면 파일 접근이 매우 느려져 사용성에 영향을 줍니다.
