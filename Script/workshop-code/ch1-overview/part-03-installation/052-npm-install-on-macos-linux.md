# Slide 52: npm Install on macOS/Linux

**Part 3: INSTALLATION**

## Code Blocks

### macOS / Linux

```bash
# 1. Node.js 18 LTS 이상 설치 확인
node --version  # v18.x.x 이상이어야 함

# 2. Claude Code 글로벌 설치
npm install -g @anthropic-ai/claude-code

# 3. 설치 검증
claude --version
claude doctor      # 환경 자가 진단

# 4. 첫 실행
cd /path/to/your/project
claude
# > 처음에 인증 안내가 표시됩니다.

# (선택) 권한 오류 해결
npm config get prefix
# /usr/local 이면 sudo 필요할 수 있음
# nvm/fnm 사용 권장 (sudo 불필요)
```

## Speaker Notes

macOS와 Linux에서 npm으로 설치하는 단계입니다.
1단계 node --version으로 Node.js 18 이상이 설치되어 있는지 확인합니다.
2단계 npm install -g @anthropic-ai/claude-code 명령으로 글로벌 설치합니다.
3단계 claude --version과 claude doctor로 설치를 검증합니다.
doctor 명령은 환경 자가 진단을 실행해 누락된 의존성이나 설정 오류를 알려 줍니다.
4단계 본인의 프로젝트 디렉토리로 이동해 claude 명령을 실행하면 첫 인증 안내가 표시됩니다.
권한 오류가 발생할 경우 sudo를 사용해야 할 수도 있는데, sudo가 부담스러우면 nvm이나 fnm 같은 Node 버전 매니저를 사용하면 sudo 없이 글로벌 설치가 가능합니다.
