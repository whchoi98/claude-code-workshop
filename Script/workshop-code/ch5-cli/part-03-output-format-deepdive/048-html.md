# Slide 48: HTML 대시보드 생성

**Part 3: 출력 형식과 파싱 심화**

## Code Blocks

### dashboard

```typescript
#!/bin/bash
# generate-dashboard.sh - 일일 사용량 대시보드

DATA=$(jq -s '
  map({
    ts: .timestamp,
    model: .model,
    duration: .duration_ms,
    in: .usage.input_tokens,
    out: .usage.output_tokens,
    cost: (
      if (.model | startswith("claude-sonnet")) then
        (.usage.input_tokens * 3 + .usage.output_tokens * 15) / 1e6
      else 0 end
    )
  })' /var/log/claude/$(date +%Y-%m-%d)/*.json)

cat <<HTML > dashboard.html
<!DOCTYPE html>
<html><head>
<title>Claude Code Dashboard - $(date +%Y-%m-%d)</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
body { font-family: sans-serif; max-width: 1200px; margin: auto; }
.cards { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; }
.card { padding: 1rem; border: 1px solid #ddd; border-radius: 8px; }
canvas { max-height: 300px; }
</style>
</head><body>
<h1>📊 일일 사용량 - $(date +%Y-%m-%d)</h1>
<div class="cards">
  <div class="card">
    <h3>총 호출</h3>
    <p id="total"></p>
  </div>
  <div class="card">
    <h3>총 비용</h3>
    <p id="cost"></p>
  </div>
</div>
<canvas id="chart"></canvas>
<script>
const data = $DATA;
document.getElementById('total').textContent = data.length;
document.getElementById('cost').textContent =
  '$' + data.reduce((s,r) => s + r.cost, 0).toFixed(2);
// Chart.js 그래프 추가 가능
</script>
</body></html>
HTML

echo "✓ dashboard.html 생성"
```

## Speaker Notes

HTML 대시보드 생성 스크립트입니다.
일일 사용량을 시각화하는 운영 도구입니다.
DATA 변수에 모든 로그를 jq로 정리합니다.
timestamp, model, duration, input, output, cost 필드를 가진 객체 배열로 변환합니다.
cost는 Sonnet 단가 기준으로 자동 계산됩니다.
heredoc으로 HTML 파일을 생성합니다.
Chart.js를 CDN에서 로드해 시각화에 활용합니다.
CSS Grid로 카드 레이아웃을 만들고 canvas 요소로 그래프 영역을 준비합니다.
body 안의 script에서 DATA 변수를 JavaScript 객체로 직접 주입합니다.
총 호출 수와 총 비용을 자동 계산해 표시합니다.
주석으로 Chart.js 그래프를 추가할 수 있다고 명시합니다.
이 패턴으로 매일 자동 생성되는 운영 대시보드를 구축할 수 있습니다.
사내 웹 서버에 호스팅하면 팀 전체가 사용량을 모니터링할 수 있습니다.
