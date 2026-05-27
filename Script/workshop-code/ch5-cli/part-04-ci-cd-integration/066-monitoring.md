# Slide 66: 모니터링과 알람

**Part 4: CI/CD 통합**

## Code Blocks

### monitoring

```bash
# 1. Slack 알림 (성공/실패)
- name: Notify Slack
  if: always()
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    channel: '#ci-claude'
    fields: repo,branch,commit,author,workflow

# 2. CloudWatch 메트릭 전송
- name: Send metrics
  if: always()
  env:
    AWS_REGION: us-east-1
  run: |
    DURATION=$(jq '.duration_ms' result.json)
    TOKENS=$(jq '.usage.output_tokens' result.json)
    aws cloudwatch put-metric-data \
      --namespace ClaudeCI \
      --metric-data \
        MetricName=Duration,Value=$DURATION \
        MetricName=Tokens,Value=$TOKENS

# 3. Datadog 전송
curl -X POST "https://api.datadoghq.com/api/v1/events" \
  -H "DD-API-KEY: $DD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Claude CI Result",
    "text": "PR #123 review: 5 issues found",
    "tags": ["service:ci", "result:warning"]
  }'

# 4. PagerDuty (심각도 높은 실패)
if [ "$EXIT_CODE" -ne 0 ] && [ "$BRANCH" = "main" ]; then
  curl -X POST "https://events.pagerduty.com/v2/enqueue" \
    -H "Content-Type: application/json" \
    -d "$(jq -nc \
      --arg key "$PD_KEY" \
      --arg msg "Claude CI failed on main" \
      '{routing_key: $key, event_action: "trigger", \
        payload: {summary: $msg, severity: "error"}}')"
fi

# 5. 메트릭 대시보드
# - Grafana
# - Datadog Dashboard
# - CloudWatch Dashboard
```

## Speaker Notes

CI 모니터링과 알람 패턴입니다.
1번 Slack 알림은 성공과 실패 모두 보냅니다.
if always 조건으로 항상 실행하고 8398a7/action-slack 액션을 사용합니다.
repo, branch, commit, author 정보를 자동 포함시킵니다.
2번 CloudWatch 메트릭 전송입니다.
aws cloudwatch put-metric-data로 Duration과 Tokens를 ClaudeCI 네임스페이스에 전송합니다.
시계열 그래프와 알람 설정에 활용됩니다.
3번 Datadog 전송입니다.
DD-API-KEY로 인증하고 이벤트 형식으로 메시지를 보냅니다.
tags로 분류해 필터링이 쉽습니다.
4번 PagerDuty는 심각도 높은 실패만 보냅니다.
main 브랜치 실패 같은 중요 이벤트는 즉시 on-call에게 알림됩니다.
routing_key, event_action, severity를 명시합니다.
5번 메트릭 대시보드 구축은 Grafana, Datadog Dashboard, CloudWatch Dashboard 같은 도구를 활용합니다.
시각화로 트렌드와 이상을 빠르게 감지합니다.
