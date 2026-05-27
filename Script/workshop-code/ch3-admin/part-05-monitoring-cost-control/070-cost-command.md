# Slide 70: /cost command

**Part 5: MONITORING & COST CONTROL**

## Code Blocks

### /cost

```bash
# 1. 대화형 사용
$ claude
> /cost

Session Cost Summary
  Session ID: ses_abc123
  Started: 2026-05-25 09:15:30 KST
  Duration: 2h 14m

  Cost breakdown:
    Main agent     $0.82  (1,250 input + 320 output tokens, Sonnet)
    security-scanner $1.05  (Opus, 850 tokens output)
    test-writer    $0.41  (Sonnet, 920 tokens output)
    docs-writer    $0.19  (Sonnet, 410 tokens output)

  Total this session: $2.47
  Daily cumulative:   $12.83
  Monthly cumulative: $87.42 / $200 limit (44%)

# 2. 헤드리스 + JSON 출력
$ claude -p "..." --output-format json | jq '.usage'
{
  "input_tokens": 5200,
  "output_tokens": 850,
  "model": "claude-sonnet-4-5",
  "estimated_cost_usd": 0.0285
}

# 3. 모니터링 자동화에 활용
```

## Speaker Notes

/cost 명령으로 현재 세션 비용을 즉시 확인할 수 있습니다.
대화형 사용 시 /cost 명령은 풍부한 정보를 표시합니다.
Session ID, 시작 시간, duration이 표시됩니다.
Cost breakdown에서 메인 에이전트와 각 Subagent별 비용이 분리되어 표시됩니다.
어느 Subagent가 어떤 모델로 얼마나 토큰을 소비했는지 한눈에 볼 수 있습니다.
중요한 것은 누적 표시입니다.
이번 세션 비용, 일일 누적, 월간 누적, 그리고 월 한도 대비 사용률이 표시됩니다.
예시에서 200달러 한도에 87.42달러를 사용해 44퍼센트라고 명시됩니다.
헤드리스 모드에서는 --output-format json으로 구조화 출력을 받을 수 있습니다.
jq로 usage 필드만 추출해 모니터링 자동화에 활용할 수 있습니다.
input tokens, output tokens, model, estimated cost가 정확히 표시됩니다.
