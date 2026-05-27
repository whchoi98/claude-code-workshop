# Slide 66: Installation Verification

**Part 3: INSTALLATION**

## Code Blocks

### verification

```bash
# 1. 버전 확인
$ claude --version
claude-code 1.x.x (build 20251101)

# 2. 도움말 확인
$ claude --help
Usage: claude [options] [prompt]

Options:
  -p, --prompt <text>      One-shot prompt (headless)
  -c, --continue           Continue last session
  -r, --resume <id>        Resume specific session
  --model <name>           Override model (e.g., sonnet, opus)
  --output-format <fmt>    text | json | stream-json
  --allowed-tools <list>   Comma-separated tool names
  --dangerously-skip-permissions  (위험: 모든 권한 부여)
  --debug                  Verbose tracing
```

## Speaker Notes

설치 검증의 가장 기본은 claude --version입니다.
출력 형식은 claude-code 다음에 버전 번호와 빌드 일자가 포함된 형태입니다.
claude --help로 사용 가능한 모든 옵션을 확인할 수 있습니다.
주요 옵션들을 살펴보면, -p 또는 --prompt는 헤드리스 일회성 프롬프트, -c 또는 --continue는 마지막 세션 이어가기, -r 또는 --resume은 특정 세션 ID로 재개, --model은 모델 오버라이드, --output-format은 응답 포맷 선택, --allowed-tools는 도구 화이트리스트, --dangerously-skip-permissions는 모든 권한 일괄 부여를 의미하는 위험 옵션입니다.
--debug는 상세 트레이스를 활성화합니다.
