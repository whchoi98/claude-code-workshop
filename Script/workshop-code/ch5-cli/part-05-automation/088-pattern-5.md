# Slide 88: Pattern 5 / 스케줄 등록

**Part 5: 자동화 패턴**

## Code Blocks

### daily-report.yml

```bash
# .github/workflows/daily-report.yml
name: Daily Team Report

on:
  schedule:
    - cron: '0 0 * * 1-5'    # 평일 오전 9시 KST (UTC 0시)
  workflow_dispatch:

permissions:
  contents: read
  issues: read
  pull-requests: read

jobs:
  report:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: npm install -g @anthropic-ai/claude-code

      - name: Generate report
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          GH_TOKEN: ${{ github.token }}
          SLACK_WEBHOOK: ${{ secrets.DAILY_REPORT_WEBHOOK }}
        run: |
          chmod +x .github/scripts/daily-report.sh
          .github/scripts/daily-report.sh

# Cron 표현식 참고
# 0 0 * * 1-5  : 평일 (월~금) 오전 9시 KST
# 0 9 * * *    : 매일 오후 6시 KST
# 0 1 * * 1    : 매주 월요일 오전 10시 KST

# 시간대 주의
# GitHub Actions의 cron은 UTC 기준
# KST = UTC + 9
# 한국 오전 9시 = UTC 0시

# 다양한 보고서 응용
# - 주간 보고서: cron '0 1 * * 1' (월요일)
# - 월간 보고서: cron '0 1 1 * *' (매월 1일)
# - 분기 보고서: 별도 트리거 또는 workflow_dispatch

# 메트릭 (1개월 운영 후 예시)
# - stand-up 시간: 평균 25분 → 12분
# - 정보 누락 빈도: 30% → 5%
# - 비활동자 식별: 자동
# - 매니저 보고 시간: 50% 절감
```

## Speaker Notes

Pattern 5 스케줄 등록 워크플로입니다.
on schedule cron으로 평일 오전 9시 KST에 자동 실행됩니다.
UTC 기준이므로 한국 오전 9시는 UTC 0시로 명시합니다.
1-5는 월요일부터 금요일까지를 의미합니다.
workflow_dispatch도 함께 두어 필요 시 수동 트리거가 가능합니다.
permissions는 모두 read만으로 충분합니다.
메시지 게시는 Slack webhook이 처리합니다.
Generate report 스텝에서 3가지 환경변수를 주입합니다.
ANTHROPIC_API_KEY, GH_TOKEN, SLACK_WEBHOOK입니다.
daily-report.sh를 실행합니다.
Cron 표현식 참고를 정리합니다.
평일 오전 9시 KST, 매일 오후 6시 KST, 매주 월요일 오전 10시 KST 같은 패턴들이 자주 사용됩니다.
GitHub Actions의 cron은 UTC 기준이므로 한국 시간 변환이 필요합니다.
다양한 보고서 응용도 가능합니다.
주간은 월요일 트리거, 월간은 매월 1일, 분기는 별도 트리거로 만들 수 있습니다.
1개월 운영 후 메트릭이 인상적입니다.
stand-up 시간이 평균 25분에서 12분으로 줄고 정보 누락이 30 퍼센트에서 5 퍼센트로 감소합니다.
매니저 보고 시간도 50 퍼센트 절감됩니다.
