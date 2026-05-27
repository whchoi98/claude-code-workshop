# Slide 45: Cost tracking

**Part 3: TASK 도구와 디스패치**

## Code Blocks

### /cost

```bash
# /cost 명령으로 현재 세션 비용 확인
> /cost
Current session cost: $2.34

Breakdown:
  Main agent (Sonnet):       $0.45 (12K in, 8K out)
  code-reviewer (Sonnet):    $0.32 (45K in, 5K out)
  security-scanner (Opus):   $1.41 (38K in, 6K out)
  test-writer (Sonnet):      $0.16 (22K in, 4K out)

Total tokens: 153K
Total time: 4m 32s

# 자동 알람 설정 (settings.json)
{
  "cost_alerts": {
    "session_max": 5.00,
    "daily_max":   50.00
  }
}
```

## Speaker Notes

Subagent 사용 비용을 추적하는 방법을 살펴봅니다.
/cost 슬래시 명령으로 현재 세션의 총 비용을 확인할 수 있습니다.
출력에는 전체 비용과 함께 Subagent별 세부 내역이 표시됩니다.
메인 에이전트, code-reviewer, security-scanner, test-writer 각각의 비용과 토큰 사용량이 분리되어 나옵니다.
예시에서 security-scanner는 Opus를 사용했기 때문에 비용이 1.41달러로 가장 큽니다.
나머지는 Sonnet으로 더 저렴합니다.
자동 알람도 설정할 수 있습니다.
settings.json의 cost_alerts 섹션에 session_max와 daily_max를 설정합니다.
세션 한도 또는 일별 한도를 넘으면 사용자에게 알림이 표시됩니다.
이를 통해 의도치 않은 비용 누적을 방지할 수 있습니다.
