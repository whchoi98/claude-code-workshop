# Slide 101: 환경변수 보안

**Part 6: 환경변수와 설정**

## Code Blocks

### safe input

```bash
# 안전한 입력 (히스토리 회피)
$ read -s -p "API key: " ANTHROPIC_API_KEY && export ANTHROPIC_API_KEY

# pass(password-store) 통합
$ export ANTHROPIC_API_KEY=$(pass show anthropic/api-key)

# macOS Keychain
$ export ANTHROPIC_API_KEY=$(security find-generic-password -w -s anthropic)
```

## Speaker Notes

환경변수 보안 4가지 위험과 대응법입니다.
첫째, 히스토리 노출 위험입니다.
export 명령으로 시크릿을 직접 넣으면 .bash_history에 기록되어 다른 사람이 볼 수 있습니다.
read -s로 비공개 입력하면 히스토리에 시크릿이 남지 않습니다.
둘째, env 명령 노출입니다.
ps aux나 env에서 다른 사용자가 환경변수를 볼 수 있습니다.
/proc/PID/environ 파일 권한도 확인하시기 바랍니다.
셋째, 코드 커밋 위험입니다.
.envrc나 .env 파일이 실수로 커밋되는 경우가 흔합니다.
.gitignore에 추가하고 gitleaks 같은 pre-commit hook으로 차단합니다.
넷째, 로그 노출입니다.
CLAUDE_CODE_LOG_REQUESTS를 1로 설정 시 응답에 시크릿이 포함될 수 있습니다.
디버깅 후에는 반드시 비활성화하시기 바랍니다.
안전한 입력 방법 3가지를 봅니다.
read -s로 비공개 입력, pass 도구 통합, macOS Keychain 활용입니다.
모두 시크릿이 디스크나 메모리에 안전하게 저장됩니다.
