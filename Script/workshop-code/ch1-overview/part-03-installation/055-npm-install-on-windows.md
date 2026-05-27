# Slide 55: npm Install on Windows

**Part 3: INSTALLATION**

## Code Blocks

### Windows PowerShell

```bash
# 1. Node.js 설치 - 권장: nvm-windows 사용
# https://github.com/coreybutler/nvm-windows/releases
nvm install 20
nvm use 20

# 2. PowerShell에서 설치
npm install -g @anthropic-ai/claude-code

# 3. 실행 정책 확인 (필요 시)
Get-ExecutionPolicy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 4. PATH 확인 및 검증
$env:Path -split ';' | Select-String 'npm'
claude --version

# (대안) WSL2를 사용한다면 Linux와 동일한 절차
# wsl.exe 실행 후 위 Linux 가이드 참조
```

## Speaker Notes

Windows 환경의 npm 설치입니다.
Native Windows에서 설치하려면 nvm-windows를 사용하는 것을 권장합니다.
nvm install 20과 nvm use 20으로 Node 20을 활성화한 후 PowerShell에서 npm install로 Claude Code를 설치합니다.
PowerShell의 실행 정책이 너무 엄격하면 스크립트 실행에 문제가 생길 수 있으니 Set-ExecutionPolicy를 RemoteSigned로 설정해 줍니다.
설치 후 PATH 환경변수에 npm 경로가 포함되어 있는지 확인합니다.
다만 Native Windows에서는 일부 쉘 명령이 호환되지 않을 수 있으므로 WSL2 사용을 강력히 권장합니다.
