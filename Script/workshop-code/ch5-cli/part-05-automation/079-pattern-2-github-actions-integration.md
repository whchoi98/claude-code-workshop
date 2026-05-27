# Slide 79: Pattern 2 / GitHub Actions 통합

**Part 5: 자동화 패턴**

## Code Blocks

### triage-issue.yml

```bash
# .github/workflows/triage-issue.yml
name: Auto-triage Issues

on:
  issues:
    types: [opened, reopened]

permissions:
  issues: write
  contents: read

jobs:
  triage:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: npm install -g @anthropic-ai/claude-code

      - name: Triage
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          GH_TOKEN: ${{ github.token }}
          SECURITY_SLACK_WEBHOOK: ${{ secrets.SECURITY_WEBHOOK }}
        run: |
          chmod +x .github/scripts/triage-issue.sh
          .github/scripts/triage-issue.sh \
            ${{ github.event.issue.number }}

# 통합 활용
# - 매일 100개 이슈가 들어와도 즉시 분류
# - 보안 이슈는 별도 채널로 5분 내 알림
# - 사람은 검토와 우선순위 조정에 집중

# 메트릭 (3개월 운영 후 예시)
# - 평균 분류 시간: 사람 8분 → AI 30초
# - 잘못된 라벨 비율: 사람 12% → AI 8%
# - 응답 시간: 평균 12시간 → 즉시
# - 사람이 트리아지에 쓰는 시간: 70% 감소
```

## Speaker Notes

Pattern 2를 GitHub Actions에 통합합니다.
on issues로 opened와 reopened 이벤트를 잡습니다.
permissions에 issues write와 contents read를 명시합니다.
트리아지 액션 실행에 필요한 권한입니다.
actions/checkout, setup-node, claude-code 설치까지 일반 패턴입니다.
Triage 스텝에서 3가지 환경변수를 주입합니다.
ANTHROPIC_API_KEY, GH_TOKEN, SECURITY_SLACK_WEBHOOK입니다.
issue 번호는 github.event.issue.number에서 가져옵니다.
통합 활용 효과는 즉시적입니다.
매일 100개 이슈가 들어와도 즉시 분류됩니다.
보안 이슈는 별도 채널로 5분 내 알림됩니다.
사람은 검토와 우선순위 조정에 집중할 수 있습니다.
3개월 운영 후 메트릭은 인상적입니다.
평균 분류 시간이 사람 8분에서 AI 30초로 단축됩니다.
잘못된 라벨 비율은 사람 12 퍼센트에서 AI 8 퍼센트로 오히려 개선됩니다.
응답 시간은 평균 12시간에서 즉시로 줄어듭니다.
사람이 트리아지에 쓰는 시간이 70 퍼센트 감소합니다.
