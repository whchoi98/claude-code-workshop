# Slide 85: Pattern 4 / 정기 실행

**Part 5: 자동화 패턴**

## Code Blocks

### security-audit.yml

```bash
# .github/workflows/security-audit.yml
name: Weekly Security Audit

on:
  schedule:
    - cron: '0 9 * * 1'    # 매주 월요일 오전 9시 UTC
  workflow_dispatch:      # 수동 트리거도 가능

permissions:
  contents: read
  issues: write
  pull-requests: write

jobs:
  audit:
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0    # gitleaks는 전체 이력 필요

      - uses: actions/setup-node@v4
        with: { node-version: '20' }

      - name: Install tools
        run: |
          npm install -g @anthropic-ai/claude-code
          python3 -m pip install semgrep
          curl -sSfL https://raw.githubusercontent.com/gitleaks/\
            gitleaks/master/install.sh | sh -s -- -b /usr/local/bin

      - name: Run audit
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          chmod +x .github/scripts/security-audit.sh
          .github/scripts/security-audit.sh

      - name: Upload report
        uses: actions/upload-artifact@v4
        with:
          name: security-audit-${{ github.run_id }}
          path: reports/security-*

      - name: Create issue if critical
        env:
          GH_TOKEN: ${{ github.token }}
        run: |
          CRITICAL=$(jq '.critical_count' reports/*/ai-analysis.json)
          if [ "$CRITICAL" -gt 0 ]; then
            gh issue create \
              --title "🚨 보안 감사: $CRITICAL Critical 발견" \
              --body-file reports/*/REPORT.md \
              --label "security,critical"
          fi
```

## Speaker Notes

Pattern 4 정기 실행 워크플로입니다.
on schedule cron으로 매주 월요일 오전 9시 UTC에 자동 실행됩니다.
workflow_dispatch도 함께 두어 수동 트리거도 가능합니다.
permissions에 contents read, issues write, pull-requests write를 명시합니다.
actions/checkout v4로 fetch-depth 0으로 전체 git 이력을 받습니다.
gitleaks가 전체 이력을 스캔하기 위해 필요합니다.
Install tools 스텝에서 claude-code, semgrep, gitleaks 3가지를 모두 설치합니다.
Run audit 스텝에서 ANTHROPIC_API_KEY를 주입하고 security-audit.sh를 실행합니다.
Upload report에서 모든 보고서를 artifact로 저장합니다.
run_id를 이름에 포함시켜 실행별로 구분합니다.
Create issue if critical 스텝이 중요합니다.
critical_count가 0보다 크면 자동으로 GitHub Issue를 생성합니다.
제목에 critical 개수를 표시하고 body는 보고서 파일을 사용합니다.
security와 critical 라벨을 부착해 즉시 처리되도록 합니다.
매주 자동 실행으로 보안 관리가 체계화됩니다.
