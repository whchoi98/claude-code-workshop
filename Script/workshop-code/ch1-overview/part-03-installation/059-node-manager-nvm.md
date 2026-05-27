# Slide 59: Node Manager nvm

**Part 3: INSTALLATION**

## Code Blocks

### nvm

```bash
# 1. nvm 설치
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc  # 또는 ~/.zshrc

# 2. Node 18, 20, 22 설치
nvm install 18
nvm install 20
nvm install 22

# 3. 기본 버전 지정
nvm alias default 20
nvm use default

# 4. 프로젝트별 .nvmrc
echo "20" > .nvmrc
nvm use   # .nvmrc 자동 인식

# 5. Claude Code 글로벌 설치 (sudo 불필요)
npm install -g @anthropic-ai/claude-code
```

## Speaker Notes

nvm은 가장 널리 사용되는 Node 버전 매니저입니다.
macOS와 Linux 환경에서 권장됩니다.
1단계 nvm 공식 install.sh 스크립트로 설치하고 source 명령으로 쉘 환경을 갱신합니다.
2단계 nvm install로 여러 Node 버전을 설치할 수 있습니다.
3단계 nvm alias default로 기본 버전을 지정합니다.
4단계 프로젝트 루트에 .nvmrc 파일을 만들면 해당 프로젝트로 cd 했을 때 자동으로 그 버전이 활성화됩니다.
5단계 nvm 환경에서는 sudo 없이 npm install -g가 가능하므로 권한 문제 없이 Claude Code를 글로벌 설치할 수 있습니다.
