# Slide 53: npm Install on Ubuntu/Debian

**Part 3: INSTALLATION**

## Code Blocks

### Ubuntu / Debian

```bash
# 1. apt 기본 저장소의 Node는 오래된 경우 많음 - NodeSource 권장
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# 2. 설치 확인
node --version  # v20.x.x
npm --version   # v10.x.x

# 3. Claude Code 설치 (sudo 불필요한 prefix 설정)
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

# 4. Claude Code 글로벌 설치
npm install -g @anthropic-ai/claude-code
claude --version
```

## Speaker Notes

Ubuntu와 Debian 환경에서의 설치를 자세히 살펴봅니다.
apt 기본 저장소의 Node는 너무 오래된 버전인 경우가 많아서 NodeSource 공식 저장소를 사용하는 것이 좋습니다.
1단계 curl로 NodeSource setup 스크립트를 다운받아 apt 저장소를 추가하고, apt-get install로 nodejs를 설치합니다.
2단계 node 와 npm 버전을 확인합니다.
3단계 sudo 없이 글로벌 설치가 가능하도록 npm prefix를 사용자 홈 아래로 설정하고 PATH 환경변수를 갱신합니다.
4단계 마침내 Claude Code를 글로벌 설치합니다.
이 방식은 sudo 권한이 없는 환경이나 권한 충돌을 피하고 싶을 때 표준적인 접근법입니다.
