# Slide 63: 비용 통제

**Part 4: CI/CD 통합**

## Code Blocks

### cost control

```bash
# 1. --max-turns로 도구 호출 제한
$ claude -p "..." --max-turns 10
# 10번 호출 후 강제 종료

# 2. --max-tokens로 응답 토큰 제한
$ claude -p "..." --max-tokens 2000
# 응답이 2000 토큰 초과 시 잘림

# 3. 모델 선택 (Haiku 활용)
# CI의 단순 작업은 Haiku로 충분, 10x 절감
# 복잡 분석만 Sonnet, 핵심 결정만 Opus

# 4. timeout으로 시간 제한
$ timeout 300 claude -p "..." # 5분 제한
# Unix timeout 명령으로 강제 종료

# 5. 일일 사용량 모니터링
# GitHub Actions에서:
- name: Check daily usage
  run: |
    USAGE=$(curl -H "x-api-key: $API_KEY" \
      https://api.anthropic.com/v1/usage)
    SPENT=$(echo "$USAGE" | jq -r '.daily_spent_usd')
    if [ "$(echo "$SPENT > 100" | bc)" = "1" ]; then
      echo "❌ 일일 한도 초과 ($$SPENT)" >&2
      exit 1
    fi

# 6. PR 라벨로 분기 (작은 PR만 자동 리뷰)
- name: Check PR size
  run: |
    CHANGES=$(gh pr view $PR --json additions,deletions \
      | jq '.additions + .deletions')
    if [ "$CHANGES" -gt 1000 ]; then
      echo "PR 너무 큼 ($CHANGES줄), 수동 리뷰 필요"
      exit 0    # 정상 종료, 리뷰 스킵
    fi

# 7. 캐싱으로 재호출 방지
# 같은 입력은 결과 캐싱
# Redis나 GitHub Actions cache 활용
```

## Speaker Notes

CI에서 비용 통제 7가지 패턴입니다.
1번 --max-turns로 도구 호출 제한입니다.
10번 호출 후 강제 종료되어 폭주를 방지합니다.
2번 --max-tokens로 응답 토큰 제한입니다.
응답이 2000 토큰을 초과하면 잘립니다.
3번 모델 선택입니다.
CI의 단순 작업은 Haiku로 10배 절감합니다.
복잡 분석만 Sonnet, 핵심 결정만 Opus를 사용합니다.
4번 timeout으로 시간 제한입니다.
Unix timeout 명령으로 5분 같은 제한을 강제합니다.
5번 일일 사용량 모니터링입니다.
API에서 daily_spent_usd를 가져와 임계치 초과 시 워크플로를 실패시킵니다.
6번 PR 라벨로 분기입니다.
변경 라인이 1000줄을 넘는 큰 PR은 자동 리뷰를 스킵하고 수동 리뷰로 안내합니다.
7번 캐싱으로 재호출 방지입니다.
같은 입력의 결과를 Redis나 GitHub Actions cache에 저장해 두 번째 호출을 즉시 응답합니다.
이 패턴들로 CI 비용이 통제됩니다.
