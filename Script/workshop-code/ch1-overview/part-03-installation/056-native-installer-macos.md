# Slide 56: Native Installer macOS

**Part 3: INSTALLATION**

## Code Blocks

### macOS Native

```bash
# 1. Homebrew 확인 (없다면 설치)
brew --version
# Homebrew가 없는 경우:
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Anthropic tap 추가 후 설치
brew install --cask claude-code

# 3. 또는 직접 다운로드 설치
curl -fsSL https://claude.ai/install.sh | bash

# 4. 검증
claude --version
which claude        # /opt/homebrew/bin/claude (Apple Silicon)
                    # /usr/local/bin/claude     (Intel)

# 5. 업그레이드
brew upgrade --cask claude-code
# 또는: claude update
```

## Speaker Notes

macOS Native Installer는 Homebrew를 통한 설치가 가장 일반적입니다.
1단계 brew --version으로 Homebrew 설치 여부를 확인하고 없다면 공식 install.sh 스크립트로 먼저 설치합니다.
2단계 brew install --cask claude-code 명령으로 Claude Code를 설치합니다.
cask는 GUI 앱이나 바이너리 형태의 패키지를 의미합니다.
3단계 대안으로 Anthropic 공식 install.sh 스크립트를 직접 실행해도 됩니다.
4단계 claude --version으로 검증하고 which claude로 설치 경로를 확인합니다.
Apple Silicon Mac은 /opt/homebrew/bin, Intel Mac은 /usr/local/bin에 설치됩니다.
업그레이드는 brew upgrade 명령으로 가능하며, claude update 명령으로도 가능합니다.
