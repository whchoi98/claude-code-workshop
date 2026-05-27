# Slide 32: 로깅과 관측성

**Part 2: HEADLESS 모드 심화**

## Code Blocks

### log_claude

```bash
# 모든 호출을 구조화 JSON 로그로 남김
log_claude() {
  local prompt="$1"
  local task_name="${2:-unnamed}"

  local start_ts=$(date +%s%3N)
  local response
  response=$(claude -p "$prompt" --output-format json)
  local rc=$?
  local end_ts=$(date +%s%3N)
  local elapsed_ms=$((end_ts - start_ts))

  # JSON 로그 (한 줄)
  local log_entry
  log_entry=$(jq -nc \
    --arg ts "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
    --arg task "$task_name" \
    --arg user "$(whoami)" \
    --arg host "$(hostname)" \
    --argjson elapsed "$elapsed_ms" \
    --argjson rc "$rc" \
    --argjson resp "$response" \
    '{
      ts: $ts, task: $task, user: $user, host: $host,
      elapsed_ms: $elapsed,
      exit_code: $rc,
      session_id: $resp.session_id,
      duration_ms: $resp.duration_ms,
      usage: $resp.usage,
      subtype: $resp.subtype
    }')

  # 사내 로그 시스템 전송 (비동기)
  echo "$log_entry" >> "/var/log/claude/$(date +%Y-%m-%d).log"
  {
    curl -s -X POST "$LOG_ENDPOINT" \
      -H "Content-Type: application/json" \
      -d "$log_entry"
  } &

  # 호출자에게 응답 전달
  echo "$response"
  return $rc
}

# 사용 예시
RESPONSE=$(log_claude "PR 리뷰" "pr-review")
```

## Speaker Notes

로깅과 관측성을 위한 log_claude 함수입니다.
모든 호출을 구조화 JSON 로그로 남깁니다.
prompt와 task_name을 인자로 받고 task_name이 없으면 unnamed가 기본입니다.
start_ts와 end_ts로 시작과 종료 시각을 밀리초 단위로 기록합니다.
claude 호출 후 rc로 exit code를 받습니다.
jq -nc로 구조화 JSON 로그를 생성합니다.
-n은 입력 없이 새로 만들고 -c는 한 줄로 압축합니다.
args로 모든 값을 안전하게 주입합니다.
ts, task, user, host 같은 메타데이터와 elapsed_ms, exit_code, session_id, duration_ms, usage 같은 호출 정보를 모두 포함합니다.
로컬 파일에 기록 후 curl로 사내 로그 시스템에 비동기 POST합니다.
백그라운드 amp로 응답을 기다리지 않습니다.
마지막에 호출자에게 원본 response를 전달하고 rc를 리턴합니다.
감사와 디버깅, 비용 추적 모두에 활용됩니다.
