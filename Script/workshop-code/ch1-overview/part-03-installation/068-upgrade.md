# Slide 68: Upgrade

**Part 3: INSTALLATION**

## Code Blocks

### upgrade

```bash
# 1. 최신 버전 확인
claude --version
claude update --check
# Latest: 1.5.0 / Installed: 1.4.2 -> update available

# 2. 자동 업그레이드
claude update
# 패키지 매니저에 따라 자동 적용 (npm/brew/native)

# 3. npm으로 설치한 경우 직접 명령도 가능
npm update -g @anthropic-ai/claude-code

# 4. brew로 설치한 경우
brew upgrade --cask claude-code

# 5. 특정 버전 고정 (조직 표준)
npm install -g @anthropic-ai/claude-code@1.4.2

# 6. 자동 업데이트 체크 비활성화 (CI 환경)
export CLAUDE_DISABLE_UPDATE_CHECK=1
```

## Speaker Notes

업그레이드는 claude update 명령으로 간단히 처리됩니다.
1단계 claude --version으로 현재 버전을 확인하고 claude update --check로 최신 버전과 비교합니다.
2단계 claude update를 실행하면 사용한 설치 방식에 따라 자동으로 npm, brew, 또는 native 업그레이드가 적용됩니다.
3단계와 4단계 npm 또는 brew 명령을 직접 사용해도 됩니다.
5단계 엔터프라이즈 환경에서는 npm install로 특정 버전을 고정하는 것이 일반적입니다.
새 버전이 사내 표준 도구와 호환되는지 검증된 후에만 업데이트하는 것이 안전합니다.
6단계 CI 환경에서는 매 실행마다 업데이트 체크 네트워크 호출이 발생하는 것을 막기 위해 CLAUDE_DISABLE_UPDATE_CHECK 환경변수를 1로 설정합니다.
