# Slide 33: 완성 스크립트 예시

**Part 2: HEADLESS 모드 심화**

## Code Blocks

### daily-report.sh

```bash
#!/bin/bash
# daily-report.sh - 매일 자동 실행되는 일일 보고서
set -euo pipefail

DATE=$(date -d "yesterday" +%Y-%m-%d)
WORKDIR="/tmp/daily-$DATE"
mkdir -p "$WORKDIR"

# Stage 1: 데이터 수집
echo "[1/4] 데이터 수집..."
gh pr list --state merged --search "merged:$DATE" \
  --json title,author,labels > "$WORKDIR/prs.json"
gh issue list --state closed --search "closed:$DATE" \
  --json title,author > "$WORKDIR/issues.json"
git log --since="$DATE 00:00" --until="$DATE 23:59" \
  --pretty=format:'%h %an %s' > "$WORKDIR/commits.log"

# Stage 2: AI 분석 (세션 재사용)
echo "[2/4] AI 분석..."
S=$(claude -p "다음 데이터에서 어제의 작업 패턴 분석: \
  $(cat $WORKDIR/prs.json $WORKDIR/issues.json)" \
  --model claude-haiku-4-5 \
  --output-format json | jq -r '.session_id')

# Stage 3: 요약 생성
echo "[3/4] 요약 생성..."
claude --continue "$S" \
  -p "위 분석을 기반으로 일일 보고서 (Markdown) 작성. \
      구성: 어제 완료, 진행 중, 차단 사항, 오늘 계획" \
  --output-format json | jq -r '.result' > "$WORKDIR/report.md"

# Stage 4: Slack 게시
echo "[4/4] Slack 게시..."
curl -X POST "$SLACK_WEBHOOK" \
  -H 'Content-Type: application/json' \
  -d "$(jq -n --rawfile r "$WORKDIR/report.md" '{text:$r}')"

echo "✓ 일일 보고서 완료"

# Cron 등록 (매일 오전 9시)
# 0 9 * * * /opt/daily-report.sh >> /var/log/daily-report.log 2>&1
```

## Speaker Notes

완성 스크립트 예시는 4단계 일일 보고서입니다.
매일 자동 실행되는 스케줄 작업입니다.
DATE 변수로 어제 날짜를 가져옵니다.
작업 디렉토리는 /tmp에 날짜별로 생성합니다.
Stage 1은 데이터 수집입니다.
gh CLI로 어제 머지된 PR과 클로즈된 issue를 JSON으로 수집하고 git log로 commit 이력을 가져옵니다.
Stage 2는 AI 분석입니다.
claude에게 데이터를 주고 작업 패턴을 분석하게 합니다.
Haiku로 비용을 절감하고 session_id를 추출합니다.
Stage 3는 요약 생성입니다.
같은 세션을 이어가며 일일 보고서를 마크다운으로 작성하게 합니다.
어제 완료, 진행 중, 차단 사항, 오늘 계획 4 섹션 구성을 명시합니다.
Stage 4는 Slack 게시입니다.
curl로 webhook에 POST하면서 jq의 rawfile 옵션으로 마크다운을 안전하게 JSON에 포함시킵니다.
cron에 매일 오전 9시 실행으로 등록하면 완전 자동화됩니다.
