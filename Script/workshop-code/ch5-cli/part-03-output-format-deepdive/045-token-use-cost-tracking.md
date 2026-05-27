# Slide 45: 토큰 사용량과 비용 추적

**Part 3: 출력 형식과 파싱 심화**

## Code Blocks

### cost tracking

```bash
# Anthropic API 단가 (예시, 1M 토큰당 USD)
# claude-haiku-4-5  : in $1.00,  out $5.00
# claude-sonnet-4-5 : in $3.00,  out $15.00
# claude-opus-4-5   : in $15.00, out $75.00

# 1. 단일 호출 비용 계산
$ jq '
  .usage as $u |
  if .model | startswith("claude-haiku") then
    ($u.input_tokens * 1.0 + $u.output_tokens * 5.0) / 1e6
  elif .model | startswith("claude-sonnet") then
    ($u.input_tokens * 3.0 + $u.output_tokens * 15.0) / 1e6
  elif .model | startswith("claude-opus") then
    ($u.input_tokens * 15.0 + $u.output_tokens * 75.0) / 1e6
  else 0 end
' response.json
# 결과: 0.0023 (약 $0.0023)

# 2. 일일 비용 합계 (모든 응답 파일)
$ jq -s '
  map(.usage as $u |
    if .model | startswith("claude-haiku") then
      ($u.input_tokens * 1.0 + $u.output_tokens * 5.0) / 1e6
    elif .model | startswith("claude-sonnet") then
      ($u.input_tokens * 3.0 + $u.output_tokens * 15.0) / 1e6
    elif .model | startswith("claude-opus") then
      ($u.input_tokens * 15.0 + $u.output_tokens * 75.0) / 1e6
    else 0 end)
  | add' /var/log/claude/$(date +%Y-%m-%d)/*.json

# 3. 모델별 토큰 사용량 (보고용)
$ jq -s '
  group_by(.model) | map({
    model: .[0].model,
    calls: length,
    total_in: ([.[].usage.input_tokens] | add),
    total_out: ([.[].usage.output_tokens] | add)
  })' logs/*.json

# 4. CloudWatch/Datadog 메트릭 전송
$ COST=$(jq '...' response.json)
$ aws cloudwatch put-metric-data \
    --namespace ClaudeCode \
    --metric-name DailyCost \
    --value "$COST"
```

## Speaker Notes

토큰 사용량과 비용 추적 운영 메트릭입니다.
Anthropic API 단가를 먼저 정리합니다.
Haiku는 입력 $1, 출력 $5, Sonnet은 입력 $3 출력 $15, Opus는 입력 $15 출력 $75입니다.
모두 1M 토큰당 가격입니다.
1번 단일 호출 비용 계산은 if elif end 분기로 모델별 단가를 적용합니다.
2번 일일 비용 합계는 jq -s slurp으로 모든 응답을 합치고 map으로 각 비용을 계산한 후 add로 합계를 구합니다.
3번 모델별 토큰 사용량은 group_by로 모델별 그룹화 후 각 그룹의 호출 수와 토큰 합계를 만듭니다.
4번 CloudWatch나 Datadog에 메트릭 전송입니다.
aws cloudwatch put-metric-data 명령으로 ClaudeCode 네임스페이스의 DailyCost 메트릭에 값을 보냅니다.
이 메트릭으로 대시보드와 알람을 구축할 수 있습니다.
비용 추적은 운영 핵심입니다.
