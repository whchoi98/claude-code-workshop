# Slide 31: 에러 처리와 재시도

**Part 2: HEADLESS 모드 심화**

## Code Blocks

### run_claude

```bash
# 견고한 호출을 위한 함수
run_claude() {
  local prompt="$1"
  local max_retries=3
  local retry=0
  local delay=2

  while [ $retry -lt $max_retries ]; do
    # JSON 출력으로 호출
    local response
    response=$(claude -p "$prompt" \
      --output-format json \
      --max-turns 20 \
      --max-tokens 4000 \
      2> "/tmp/claude-err-$$.log")
    local rc=$?

    # 성공: subtype이 success
    if [ $rc -eq 0 ]; then
      local subtype
      subtype=$(echo "$response" | jq -r '.subtype // "unknown"')
      if [ "$subtype" = "success" ]; then
        echo "$response"
        return 0
      fi
    fi

    # 실패: 재시도
    retry=$((retry + 1))
    if [ $retry -lt $max_retries ]; then
      echo "Retry $retry/$max_retries (delay ${delay}s)" >&2
      sleep $delay
      delay=$((delay * 2))    # exponential backoff
    fi
  done

  # 모든 재시도 실패
  echo "Failed after $max_retries attempts" >&2
  cat "/tmp/claude-err-$$.log" >&2
  rm -f "/tmp/claude-err-$$.log"
  return 1
}

# 사용
if RESPONSE=$(run_claude "이 코드 분석"); then
  echo "$RESPONSE" | jq -r '.result' > analysis.md
else
  echo "분석 실패" >&2; exit 1
fi
```

## Speaker Notes

에러 처리와 재시도 함수입니다.
run_claude 함수로 표준화된 호출을 만듭니다.
prompt를 인자로 받고 최대 3회 재시도, 초기 delay 2초로 시작합니다.
while 루프 안에서 claude를 호출하고 stderr는 /tmp 파일에 저장합니다.
프로세스 ID를 파일명에 포함해 동시 실행 시 충돌을 방지합니다.
rc로 exit code를 받아 0이면 추가 검증을 합니다.
subtype이 success인지 확인하고 그렇다면 response를 출력하고 0으로 리턴합니다.
실패 시 재시도 카운트를 증가시키고 delay만큼 sleep합니다.
delay는 매번 2배씩 증가하는 지수 backoff입니다.
2초, 4초, 8초로 늘어납니다.
모든 재시도 실패 시 stderr 로그를 표시하고 임시 파일을 정리한 후 1로 리턴합니다.
사용은 if 조건으로 받아 성공 시 jq로 결과를 추출하고 실패 시 에러 처리합니다.
