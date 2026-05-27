# Slide 57: Native Installer Linux

**Part 3: INSTALLATION**

## Code Blocks

### Linux Native

```bash
# 1. 공식 install.sh 스크립트 (curl)
curl -fsSL https://claude.ai/install.sh | bash

# 스크립트 동작:
#   - 사용자 OS/아키텍처 감지 (linux-x64, linux-arm64)
#   - ~/.claude/bin 에 claude 바이너리 다운로드
#   - PATH 자동 추가 (.bashrc / .zshrc)

# 2. 검증
source ~/.bashrc
claude --version

# 3. APT/RPM 기반 패키지 (엔터프라이즈 미러)
# Anthropic이 제공하는 deb/rpm 패키지를 사내 미러에 배포
# 자세한 절차는 Chapter 3 Admin Setup에서 다룸

# 4. 업데이트
claude update
```

## Speaker Notes

Linux Native Installer를 살펴봅니다.
가장 간단한 방법은 공식 install.sh 스크립트입니다.
curl로 다운받아 bash에 파이프하면 자동으로 OS와 아키텍처를 감지해 linux-x64 또는 linux-arm64 바이너리를 다운로드합니다.
설치 경로는 사용자 홈 아래 .claude/bin이며 bashrc 또는 zshrc에 PATH 추가도 자동 처리됩니다.
source 명령으로 환경을 갱신한 후 claude --version으로 검증할 수 있습니다.
엔터프라이즈 환경에서는 deb 또는 rpm 패키지를 사내 미러를 통해 배포할 수 있는데, 자세한 절차는 Chapter 3 Admin Setup에서 다룹니다.
업데이트는 claude update 명령 한 번으로 처리됩니다.
