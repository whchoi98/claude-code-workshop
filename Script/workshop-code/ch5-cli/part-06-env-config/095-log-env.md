# Slide 95: 로그와 디버깅 환경변수

**Part 6: 환경변수와 설정**

## Code Blocks

### log env

```bash
# 1. 로그 레벨
export CLAUDE_CODE_LOG_LEVEL=debug    # debug|info|warn|error
# debug: 모든 상세 로그
# info: 일반 정보 (기본)
# warn: 경고 이상
# error: 오류만

# 2. 로그 파일 출력
export CLAUDE_CODE_LOG_FILE=/var/log/claude.log
# 미설정 시 stderr로만 출력

# 3. 텔레메트리 비활성화
export CLAUDE_CODE_DISABLE_TELEMETRY=1
# Anthropic으로 사용 통계 전송 안 함

# 4. 도구 호출 추적
export CLAUDE_CODE_TRACE_TOOLS=1
# 각 도구 호출 상세 로그

# 5. JSON 응답 추적
export CLAUDE_CODE_LOG_REQUESTS=1
# API 요청과 응답 전체를 로그

# 6. Node.js 디버그
export NODE_OPTIONS="--inspect-brk"
# 디버거 attach 가능

# 7. 사용자 정의 user agent
export CLAUDE_CODE_USER_AGENT="company-internal/1.0"
# API 요청에 사용자 정의 헤더

# 8. 명령줄 옵션과의 관계
# --debug 옵션 = CLAUDE_CODE_LOG_LEVEL=debug
# --verbose 옵션 = CLAUDE_CODE_LOG_LEVEL=info + extra info

# 9. 로그 패턴 사용 예시
# 개발 (모든 로그)
export CLAUDE_CODE_LOG_LEVEL=debug
export CLAUDE_CODE_LOG_FILE=/tmp/claude-dev.log

# 프로덕션 (간결)
export CLAUDE_CODE_LOG_LEVEL=warn
export CLAUDE_CODE_LOG_FILE=/var/log/claude/prod.log

# CI (구조화 + 자세히)
export CLAUDE_CODE_LOG_LEVEL=info
export CLAUDE_CODE_LOG_REQUESTS=1
```

## Speaker Notes

로그와 디버깅 환경변수입니다.
1번 CLAUDE_CODE_LOG_LEVEL로 로그 레벨을 명시합니다.
debug는 모든 상세 로그, info는 일반 정보, warn은 경고 이상, error는 오류만입니다.
2번 CLAUDE_CODE_LOG_FILE로 파일 출력 경로를 명시합니다.
미설정 시 stderr로만 출력됩니다.
3번 텔레메트리 비활성화로 Anthropic으로 사용 통계 전송을 막을 수 있습니다.
사내 정책상 외부 통신을 통제하는 경우 필수입니다.
4번 도구 호출 추적으로 각 도구 호출의 상세 로그를 활성화합니다.
5번 JSON 응답 추적으로 API 요청과 응답 전체를 로그에 남깁니다.
디버깅에 매우 유용하지만 로그 양이 폭증할 수 있습니다.
6번 Node.js 디버그로 디버거 attach가 가능합니다.
7번 사용자 정의 user agent로 API 요청에 사내 식별자를 추가할 수 있습니다.
8번 명령줄 옵션과의 관계를 정리합니다.
--debug 옵션은 LOG_LEVEL debug와 같고 --verbose는 info에 추가 정보를 더합니다.
9번 환경별 패턴 사용 예시도 정리되어 있습니다.
개발, 프로덕션, CI 환경에 적합한 설정 조합을 보여줍니다.
