# Slide 75: Auth Method 2: Anthropic API Key

**Part 4: AUTHENTICATION**

## Code Blocks

### API Key

```bash
# 1. 환경변수 방식 (가장 일반적)
export ANTHROPIC_API_KEY="sk-ant-api03-..."
claude

# 2. 영구 저장 (~/.bashrc 또는 ~/.zshrc)
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-..."' >> ~/.zshrc
source ~/.zshrc

# 3. macOS Keychain 사용 (권장)
security add-generic-password \
  -s anthropic_api_key -a "$USER" -w "sk-ant-..."
# 사용 시:
export ANTHROPIC_API_KEY=$(security find-generic-password \
  -s anthropic_api_key -a "$USER" -w)

# 4. 1Password CLI 통합 (팀 권장)
export ANTHROPIC_API_KEY=$(op read "op://Personal/anthropic/key")
```

## Speaker Notes

두 번째 인증 방식, Anthropic API Key를 사용한 종량제 방식을 살펴봅니다.
1단계 가장 일반적인 방법은 ANTHROPIC_API_KEY 환경변수에 값을 넣고 claude를 실행하는 것입니다.
2단계 매번 입력하기 번거로우므로 .bashrc나 .zshrc에 export 구문을 영구 저장할 수 있습니다.
평문 저장은 보안상 위험합니다.
3단계 macOS에서는 Keychain을 활용하면 OS가 안전하게 보관해 줍니다.
4단계 팀 환경에서는 1Password CLI 같은 시크릿 매니저와 통합해 동료 간 키 공유와 회전을 안전하게 처리하는 것을 권장합니다.
API Key는 sk-ant 로 시작하는 특수한 접두사를 가집니다.
