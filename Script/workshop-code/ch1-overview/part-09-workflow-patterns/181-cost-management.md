# Slide 181: Cost Management

**Part 9: WORKFLOW PATTERNS**

## Code Blocks

### /cost

```
> /cost

Current Session
  Model           Input tokens     Output tokens    Cost (USD)
  sonnet-4-5      45,231 (cached:8,420)   12,453    $0.328
  haiku-4-5       2,140 (subagent)          892     $0.013

  Tools used     38 calls (Read:18, Edit:8, Bash:7, Grep:5)

Today (UTC)
  Total cost:     $1.42
  Sessions:       7
  Most expensive: 'Refactoring auth module' ($0.92)

Daily limit:    $20.00  ($1.42 / $20.00 = 7.1%)

To save costs:
  - 큰 작업 분할
  - 단순 작업은 --model haiku
  - 컨텍스트는 /clear로 정기 초기화
```

## Speaker Notes

/cost 슬래시 명령은 현재 세션과 누적 비용을 보여 줍니다.
모델별 입력 토큰과 출력 토큰, 비용을 분리해 표시하며, 캐시된 토큰은 별도로 표기되어 캐시 효율을 확인할 수 있습니다.
도구 사용 횟수도 종류별로 집계되어 어떤 도구가 많이 호출되었는지 파악할 수 있습니다.
오늘의 총 비용과 세션 수, 가장 비용이 큰 세션이 표시되며, 설정한 일일 한도 대비 사용률도 함께 보여 줍니다.
비용 절감 팁으로 큰 작업 분할, 단순 작업은 haiku 모델 사용, 정기적인 /clear가 안내됩니다.
