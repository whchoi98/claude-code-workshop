# Slide 8: --help system

**Part 1: claude 명령 기본**

## Code Blocks

### --help

```bash
# 1. 전체 도움말
$ claude --help

Usage: claude [options] [prompt]

Options:
  -p, --print <prompt>          Headless 모드 (한 번 응답)
  --output-format <fmt>          text|json|stream-json
  --model <model>                사용할 모델 ID
  --max-turns <n>                최대 도구 호출 수
  --max-tokens <n>               최대 응답 토큰
  --allowed-tools <tools>        허용 도구 (콤마 구분)
  --disallowed-tools <tools>     차단 도구
  --dangerously-skip-permissions 권한 확인 우회 (위험)
  --cwd <dir>                    작업 디렉토리
  --system-prompt <text>         시스템 프롬프트 추가
  --resume                       마지막 세션 이어서
  --continue                     특정 세션 ID 이어서
  --debug                        디버그 로그
  --version                      버전 정보
  --help                         이 도움말

# 2. 하위 명령 도움말
$ claude doctor --help
$ claude mcp --help

# 3. 환경변수 정보
$ claude doctor --verbose
# 모든 환경변수와 현재 값 표시
```

## Speaker Notes

--help 시스템을 가장 먼저 익혀야 합니다.
claude --help를 입력하면 전체 도움말이 표시됩니다.
Usage 라인이 명령 형식을 보여주고 Options에 모든 플래그가 나열됩니다.
각 옵션의 약어와 설명을 한눈에 볼 수 있습니다.
print, output-format, model 같은 핵심 옵션부터 cwd, system-prompt, resume 같은 고급 옵션까지 정리되어 있습니다.
하위 명령에도 --help가 있습니다.
claude doctor --help, claude mcp --help 같은 형태로 확인합니다.
환경 정보는 claude doctor --verbose로 확인합니다.
모든 환경변수와 현재 값이 표시되어 디버깅에 매우 유용합니다.
새로운 옵션이나 명령이 추가되면 가장 먼저 확인하시기 바랍니다.
