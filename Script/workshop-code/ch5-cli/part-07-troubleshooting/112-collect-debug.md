# Slide 112: 디버그 정보 수집

**Part 7: 디버깅과 트러블슈팅**

## Code Blocks

### collect-debug

```bash
#!/bin/bash
# collect-debug-info.sh - 종합 디버그 정보 수집
# 사내 Slack이나 Support 에스컬레이션 시 사용

REPORT=/tmp/claude-debug-$(date +%Y%m%d-%H%M%S).txt

{
  echo "=== Claude Code Debug Info ==="
  echo "Date: $(date)"
  echo "User: $(whoami)"
  echo "Host: $(hostname)"
  echo ""

  echo "=== Versions ==="
  echo "Node: $(node --version)"
  echo "Claude: $(claude --version)"
  echo "OS: $(uname -a)"
  echo ""

  echo "=== Environment (filtered) ==="
  env | grep -iE 'claude|anthropic|aws_region|aws_profile|proxy|node_extra' \
      | sed 's/=.\{6,\}.*$/=<redacted>/'
  echo ""

  echo "=== Settings ==="
  cat ~/.claude/settings.json 2>/dev/null | \
    jq 'del(.. | objects | select(has("token") or has("key")) | .)'
  echo ""

  echo "=== Doctor ==="
  claude doctor --verbose 2>&1
  echo ""

  echo "=== Recent Log (last 100 lines) ==="
  tail -100 ~/.claude/logs/$(date +%Y-%m-%d).log 2>/dev/null
  echo ""

  echo "=== Network Test ==="
  curl -sSI https://api.anthropic.com 2>&1
  echo ""

  echo "=== Failed command (manual paste) ==="
  echo "<여기에 실패한 명령과 결과 붙여넣기>"

} > "$REPORT"

echo "✓ Debug report: $REPORT"
echo "  업로드 방법: 사내 Slack #claude-help"

# 시크릿 마스킹 확인
$ grep -i 'sk-\|akia\|password\|token=' "$REPORT"
# 비어 있으면 안전
```

## Speaker Notes

디버그 정보 수집 스크립트입니다.
에스컬레이션 시 첨부할 종합 정보를 한 번에 수집합니다.
REPORT 변수에 타임스탬프 포함 파일명을 만듭니다.
수집 항목 6가지입니다.
첫째, 메타데이터로 날짜, 사용자, 호스트입니다.
둘째, 버전으로 Node, Claude, OS를 명시합니다.
셋째, 환경변수는 필터링해서 마스킹합니다.
sed로 6자 이상 값은 redacted로 치환해 시크릿 노출을 방지합니다.
넷째, settings 파일을 jq로 token과 key 필드를 삭제 후 출력합니다.
다섯째, doctor --verbose 전체 출력입니다.
여섯째, 최근 로그 100줄과 네트워크 테스트 결과입니다.
마지막에 사용자가 직접 실패한 명령과 결과를 붙여넣을 자리를 만듭니다.
중요한 점은 시크릿 마스킹 확인입니다.
grep으로 sk- AKIA password token 패턴이 없는지 검증합니다.
비어 있으면 안전하게 공유 가능합니다.
사내 Slack의 claude-help 채널에 업로드해 도움을 요청할 수 있습니다.
