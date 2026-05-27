# Slide 54: npm Install on RHEL/Fedora

**Part 3: INSTALLATION**

## Code Blocks

### RHEL / Fedora

```bash
# 1. NodeSource 저장소 추가 (RHEL/CentOS/Rocky/Fedora)
curl -fsSL https://rpm.nodesource.com/setup_20.x | sudo bash -
sudo dnf install -y nodejs

# 2. 또는 dnf 모듈을 통한 설치 (RHEL 9+)
sudo dnf module install nodejs:20/common

# 3. 설치 확인
node --version
npm --version

# 4. 사용자 prefix 설정 후 Claude Code 설치
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

npm install -g @anthropic-ai/claude-code
```

## Speaker Notes

RHEL, CentOS, Rocky Linux, Fedora 같은 RPM 계열 배포판에서의 설치입니다.
NodeSource RPM 저장소를 추가한 후 dnf install로 nodejs를 설치하는 것이 가장 일반적입니다.
RHEL 9 이상에서는 dnf module install nodejs 명령으로 모듈 스트림 방식으로 설치할 수도 있습니다.
이후 단계는 Debian 계열과 동일하게 사용자 prefix를 설정한 후 글로벌 설치를 진행합니다.
RHEL 계열에서는 SELinux 정책이 활성화되어 있는 경우가 많은데, Claude Code의 도구 실행에 영향을 줄 수 있으니 권한 문제 발생 시 SELinux 로그를 확인하시기 바랍니다.
