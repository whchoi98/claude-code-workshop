# Slide 84: Pattern 4 / 보안 감사 스크립트

**Part 5: 자동화 패턴**

## Code Blocks

### security-audit.sh

```bash
#!/bin/bash
# security-audit.sh - 정기 보안 감사
set -euo pipefail

REPORT_DIR="reports/security-$(date +%Y-%m-%d)"
mkdir -p "$REPORT_DIR"

# 1. 의존성 스캔
echo "[1/4] 의존성 스캔..."
npm audit --json > "$REPORT_DIR/npm-audit.json" || true

# 2. 코드 스캔 (semgrep)
echo "[2/4] 코드 스캔..."
semgrep --config=auto --json -o "$REPORT_DIR/semgrep.json" . || true

# 3. 비밀 노출 검사
echo "[3/4] 비밀 노출 검사..."
gitleaks detect --report-path "$REPORT_DIR/gitleaks.json" \
  --no-banner -f json || true

# 4. AI 통합 분석
echo "[4/4] AI 통합 분석..."
claude -p "$(cat <<EOF
다음 보안 스캔 결과를 통합 분석:

npm audit:
$(cat "$REPORT_DIR/npm-audit.json" | head -200)

semgrep:
$(cat "$REPORT_DIR/semgrep.json" | head -200)

gitleaks:
$(cat "$REPORT_DIR/gitleaks.json" 2>/dev/null | head -100)

응답 형식 (JSON):
{
  "critical_count": 0,
  "high_count": 0,
  "medium_count": 0,
  "low_count": 0,
  "false_positive_likely": [],
  "top_priorities": [
    {"rank": 1, "issue": "...", "severity": "...",
     "location": "...", "fix": "..."}
  ],
  "executive_summary": "한 단락 요약"
}
EOF
)" \
  --allowed-tools "Read,Grep" \
  --max-turns 20 \
  --output-format json | jq -r '.result' | jq . \
  > "$REPORT_DIR/ai-analysis.json"

# 5. 마크다운 보고서 생성
ANALYSIS=$(cat "$REPORT_DIR/ai-analysis.json")
SUMMARY=$(echo "$ANALYSIS" | jq -r '.executive_summary')

{
  echo "# 보안 감사 보고서 - $(date +%Y-%m-%d)"
  echo ""
  echo "## 요약"
  echo "$SUMMARY"
  echo ""
  echo "## 우선순위 Top 5"
  echo "$ANALYSIS" | jq -r '.top_priorities[] |
    "### \(.rank). [\(.severity)] \(.issue)\n위치: \(.location)\n수정: \(.fix)\n"'
} > "$REPORT_DIR/REPORT.md"

echo "✓ 보고서: $REPORT_DIR/REPORT.md"
```

## Speaker Notes

Pattern 4 보안 감사 스크립트 security-audit.sh입니다.
REPORT_DIR을 날짜별로 만들어 결과를 보존합니다.
4단계로 진행됩니다.
1단계 의존성 스캔은 npm audit으로 JSON 결과를 저장합니다.
2단계 코드 스캔은 semgrep auto config로 스캔합니다.
3단계 비밀 노출 검사는 gitleaks로 git 이력 전체를 스캔합니다.
각 스캐너의 종료 코드가 0이 아니어도 OR true로 계속 진행합니다.
4단계 AI 통합 분석이 핵심입니다.
claude에게 3가지 스캐너 결과를 모두 전달하고 통합 분석을 요청합니다.
각 결과의 첫 부분만 사용해 컨텍스트 크기를 통제합니다.
응답은 구조화 JSON입니다.
critical_count, high_count 등 심각도별 개수를 받습니다.
false_positive_likely 배열로 오탐일 가능성이 높은 항목을 별도 분류합니다.
top_priorities로 우선 처리해야 할 5가지를 받습니다.
executive_summary로 경영진 보고용 한 단락 요약을 받습니다.
5단계 마크다운 보고서 생성으로 사람이 읽기 쉬운 형식으로 변환합니다.
jq로 top priorities를 순회하며 등급, 위치, 수정 방법을 정리합니다.
