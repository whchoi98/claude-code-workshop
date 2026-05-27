# Slide 41: jq 고급 (집계)

**Part 3: 출력 형식과 파싱 심화**

## Code Blocks

### aggregation

```bash
# 시나리오: 100개 응답에서 통계 추출

# 1. 모든 응답을 배열로 합치기 (slurp)
$ jq -s '.' responses/*.json > all.json
# -s : 모든 입력을 배열로 합침

# 2. 평균 응답 시간
$ jq '[.[].duration_ms] | add / length' all.json

# 3. 토큰 사용량 합계
$ jq '[.[].usage.input_tokens] | add' all.json
$ jq '[.[].usage.output_tokens] | add' all.json

# 4. 모델별 그룹화 + 카운트
$ jq 'group_by(.model) | map({
    model: .[0].model,
    count: length,
    avg_duration: ([.[].duration_ms] | add / length),
    total_in: ([.[].usage.input_tokens] | add),
    total_out: ([.[].usage.output_tokens] | add)
  })' all.json

# 5. 에러율 계산
$ jq '{
    total: length,
    errors: [.[] | select(.is_error)] | length
  } | .error_rate = (.errors / .total * 100)' all.json

# 6. p95 응답 시간 (백분위)
$ jq '[.[].duration_ms] | sort | .[((length * 0.95) | floor)]' \
    all.json

# 7. reduce로 누적
$ jq 'reduce .[] as $x (
    {count:0, sum:0};
    {count: (.count+1), sum: (.sum+$x.duration_ms)}
  ) | .avg = (.sum / .count)' all.json
```

## Speaker Notes

jq 고급 집계 패턴입니다.
100개 응답 파일에서 통계를 추출하는 시나리오입니다.
1단계 모든 응답을 배열로 합칩니다.
-s 옵션은 slurp으로 여러 JSON을 하나의 배열로 만듭니다.
2단계 평균 응답 시간을 계산합니다.
모든 duration_ms를 배열로 만들고 add로 합계를 구해 length로 나눕니다.
3단계 토큰 사용량 합계입니다.
4단계 모델별 그룹화와 카운트입니다.
group_by로 같은 모델끼리 묶고 map으로 각 그룹의 통계를 만듭니다.
5단계 에러율 계산입니다.
전체 수와 에러 수를 계산해 백분율로 변환합니다.
6단계 p95 응답 시간 백분위입니다.
sort 후 95 퍼센트 위치의 값을 인덱싱합니다.
7단계 reduce로 누적 계산입니다.
초기값을 주고 각 요소에 대해 누적 객체를 만들어갑니다.
이 패턴들로 운영 대시보드 데이터를 자동 생성할 수 있습니다.
