# Slide 58: Native Installer Windows

**Part 3: INSTALLATION**

## Code Blocks

### Windows Native

```bash
# 1. 공식 MSI 설치 - 권장 (관리자 권한 필요)
# https://claude.ai/download/windows.msi 에서 다운로드 후 실행
# 또는 PowerShell:
Invoke-WebRequest -Uri https://claude.ai/install.ps1 -OutFile install.ps1
.\install.ps1

# 2. WinGet (Windows Package Manager) - Windows 10/11
winget install Anthropic.ClaudeCode

# 3. Scoop (서드파티 패키지 매니저)
scoop bucket add claude https://github.com/anthropics/scoop-claude
scoop install claude-code

# 4. 검증
claude --version

# 5. (강력 권장) WSL2 사용 - Linux 가이드 참조
wsl --install -d Ubuntu-22.04
```

## Speaker Notes

Windows Native Installer에는 여러 옵션이 있습니다.
첫째 공식 MSI 패키지가 가장 권장되며, 관리자 권한으로 실행해 시스템 전체에 설치합니다.
PowerShell의 install.ps1 스크립트로도 동일하게 설치 가능합니다.
둘째 Windows Package Manager인 WinGet으로 winget install Anthropic.ClaudeCode 명령 한 줄로 설치할 수 있습니다.
셋째 서드파티 패키지 매니저 Scoop도 지원되어 scoop install claude-code로 설치 가능합니다.
검증은 동일하게 claude --version입니다.
강력하게 권장드리는 것은 WSL2 사용입니다.
Native Windows는 일부 도구의 동작에 제약이 있을 수 있어, wsl --install -d Ubuntu-22.04 명령으로 WSL2를 설치하고 Linux 가이드대로 진행하는 것이 가장 안정적입니다.
