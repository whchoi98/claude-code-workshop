# Slide 40: jq 고급 패턴 (filter)

**Part 3: 출력 형식과 파싱 심화**

## Code Blocks

### jq filter

```bash
# 1. 단순 조건 필터
$ claude -p "..." --output-format json | \
    jq 'select(.is_error == false)'

# 2. 복합 조건 (AND/OR)
$ jq 'select(.usage.input_tokens > 1000 and .duration_ms < 5000)'
$ jq 'select(.subtype == "error" or .is_error == true)'

# 3. 정규식 매칭
$ jq 'select(.result | test("ERROR|FATAL"))'
$ jq 'select(.model | startswith("claude-opus"))'

# 4. null 체크 (안전한 접근)
$ jq 'select(.usage?.input_tokens // 0 > 500)'
$ # ? : 필드 없으면 null
$ # // : null이면 기본값

# 5. 배열 안에서 필터
$ echo '[{"a":1},{"a":2},{"a":3}]' | \
    jq 'map(select(.a > 1))'
# 결과: [{"a":2},{"a":3}]

# 6. 다중 조건 분기
$ jq 'if .is_error then "FAIL"
      elif .subtype == "max_turns_reached" then "PARTIAL"
      else "OK"
      end'

# 7. 응답 분류
$ for response in responses/*.json; do
    STATUS=$(jq -r '
      if .is_error then "fail"
      elif .duration_ms > 10000 then "slow"
      else "ok"
      end' "$response")
    echo "$response: $STATUS"
  done
```

## Speaker Notes

jq 고급 필터링 패턴입니다.
첫째, 단순 조건 필터로 select 함수에 boolean 표현식을 전달합니다.
둘째, 복합 조건은 and와 or로 결합합니다.
셋째, 정규식 매칭은 test 함수와 startswith 같은 문자열 함수를 사용합니다.
넷째, null 체크가 중요합니다.
물음표 연산자는 필드가 없으면 null을 반환하고 슬래시 슬래시 연산자는 null이면 기본값을 사용합니다.
다섯째, 배열 안에서 필터링은 map과 select를 조합합니다.
여섯째, 다중 조건 분기는 if then elif else end 구문을 사용합니다.
일곱째, 응답 분류 패턴입니다.
is_error면 fail, duration_ms가 길면 slow, 나머지는 ok로 분류합니다.
for 루프로 여러 응답 파일을 한 번에 분류할 수 있습니다.
