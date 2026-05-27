# Slide 23: Exit code 활용

**Part 2: HEADLESS 모드 심화**

## Code Blocks

### exit code

```bash
# Claude의 exit code
# 0   - 성공
# 1   - 일반 오류
# 2   - 인자 오류
# 124 - timeout
# 130 - SIGINT (Ctrl+C)
# 137 - SIGKILL (메모리 초과 등)

# 패턴 1: 성공/실패 분기
$ claude -p "테스트 실행" && echo "OK" || echo "Failed"

# 패턴 2: exit code 캡처
$ claude -p "..."; EC=$?
$ if [ $EC -eq 0 ]; then
    echo "성공"
  elif [ $EC -eq 124 ]; then
    echo "Timeout"
  else
    echo "에러 코드: $EC"
  fi

# 패턴 3: timeout 설정 (5분 제한)
$ timeout 300 claude -p "큰 작업"
# 5분 초과 시 exit code 124

# 패턴 4: 응답 안에서 결과 판단
$ RESULT=$(claude -p "이 코드 안전한가? yes/no만 응답" \
    --output-format json | jq -r '.result')
$ if [ "$RESULT" = "yes" ]; then
    echo "안전"
  else
    echo "위험"
    exit 1
  fi

# 패턴 5: 재시도 로직
$ MAX=3
$ for i in $(seq 1 $MAX); do
    claude -p "..." && break
    [ $i -lt $MAX ] && sleep $((2**i))
  done
```

## Speaker Notes

Exit Code 활용 패턴입니다.
Claude의 exit code는 명확합니다.
0은 성공, 1은 일반 오류, 2는 인자 오류, 124는 timeout, 130은 SIGINT 즉 Ctrl+C, 137은 SIGKILL 즉 메모리 초과입니다.
패턴 1은 성공과 실패 분기입니다.
앰퍼샌드 두 개와 파이프 두 개로 한 줄에 처리합니다.
패턴 2는 exit code 캡처입니다.
달러 물음표로 직전 명령의 exit code를 가져옵니다.
패턴 3은 timeout 설정입니다.
Unix의 timeout 명령으로 5분 제한을 강제할 수 있습니다.
초과 시 자동으로 종료되고 exit code 124가 됩니다.
패턴 4는 응답 안에서 결과 판단입니다.
Claude에게 yes나 no만 응답하라고 지시한 후 결과를 변수로 받아 분기합니다.
패턴 5는 재시도 로직입니다.
최대 3회까지 시도하고 실패 시 2의 i제곱 초만큼 backoff합니다.
