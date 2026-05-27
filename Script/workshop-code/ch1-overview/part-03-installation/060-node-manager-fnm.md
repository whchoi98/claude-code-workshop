# Slide 60: Node Manager fnm

**Part 3: INSTALLATION**

## Code Blocks

### fnm

```bash
# 1. fnm 설치 (Rust 기반, nvm보다 훨씬 빠름)
curl -fsSL https://fnm.vercel.app/install | bash
# 또는 Homebrew: brew install fnm

# 2. 쉘 통합 활성화
echo 'eval "$(fnm env --use-on-cd)"' >> ~/.bashrc
source ~/.bashrc

# 3. Node 설치
fnm install 20
fnm install --lts

# 4. 기본 버전
fnm default 20

# 5. .nvmrc / .node-version 자동 인식 (cd 시)
echo "20" > .node-version
cd .  # 자동 전환 동작 확인

# 6. Claude Code 설치
npm install -g @anthropic-ai/claude-code
```

## Speaker Notes

fnm은 Fast Node Manager의 약자로 Rust로 구현된 빠르고 가벼운 Node 매니저입니다.
nvm 대비 10배에서 100배 빠른 성능을 보여 줍니다.
1단계 공식 install 스크립트나 Homebrew로 설치합니다.
2단계 쉘 통합을 활성화하는데, use-on-cd 옵션을 주면 cd 명령으로 디렉토리 진입 시 자동으로 .nvmrc 또는 .node-version 파일을 인식해 Node 버전을 전환합니다.
3단계 fnm install로 Node를 설치합니다.
--lts 플래그로 최신 LTS를 자동 선택할 수도 있습니다.
4단계 기본 버전 설정 후 5단계에서 .node-version 파일로 프로젝트별 고정합니다.
