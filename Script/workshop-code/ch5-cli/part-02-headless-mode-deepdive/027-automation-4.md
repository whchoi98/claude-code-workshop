# Slide 27: 자동화 4 / 번역

**Part 2: HEADLESS 모드 심화**

## Code Blocks

### translate-docs.sh

```bash
#!/bin/bash
# translate-docs.sh - 마크다운 문서 한/영 번역
set -euo pipefail

FILE="${1:?Usage: translate-docs.sh <file> <ko|en>}"
LANG="${2:?Usage: translate-docs.sh <file> <ko|en>}"
GLOSSARY="${GLOSSARY:-~/.claude/glossary.md}"

# 출력 파일명 결정
DIR=$(dirname "$FILE")
BASE=$(basename "$FILE" .md)
OUT="$DIR/${BASE}.${LANG}.md"

# 사내 용어 사전 로드
GLOSSARY_CONTENT=""
if [ -f "$GLOSSARY" ]; then
  GLOSSARY_CONTENT=$(cat "$GLOSSARY")
fi

# 번역 실행 (점진 - 큰 파일도 처리)
claude -p "$(cat <<EOF
다음 마크다운 문서를 ${LANG}로 번역하세요.

원칙:
- 자연스러운 톤 (직역 금지)
- 코드 블록과 명령어는 유지
- 마크다운 구조 보존
- 사내 용어 사전 적용

사내 용어 사전:
$GLOSSARY_CONTENT

원본:
$(cat "$FILE")

번역된 마크다운만 출력하세요 (다른 설명 X).
EOF
)" \
  --max-turns 5 \
  --output-format json | jq -r '.result' > "$OUT"

# 검증: 라인 수가 너무 다르면 경고
ORIG_LINES=$(wc -l < "$FILE")
TRANS_LINES=$(wc -l < "$OUT")
if [ $((ORIG_LINES - TRANS_LINES)) -gt 10 ] || \
   [ $((TRANS_LINES - ORIG_LINES)) -gt 10 ]; then
  echo "⚠ 라인 수 차이 큼: 원본 $ORIG_LINES vs 번역 $TRANS_LINES" >&2
fi

echo "✓ 번역 완료: $OUT"
```

## Speaker Notes

자동화 4번 문서 번역 스크립트입니다.
파일 경로와 대상 언어를 인자로 받습니다.
GLOSSARY 환경변수로 사내 용어 사전 위치를 지정할 수 있고 기본값은 ~/.claude/glossary.md입니다.
출력 파일명은 원본 이름에 .ko 또는 .en suffix를 추가합니다.
사내 용어 사전이 있으면 자동 로드합니다.
claude에게 번역을 요청하면서 4가지 원칙을 명시합니다.
자연스러운 톤, 코드 블록과 명령어 유지, 마크다운 구조 보존, 용어 사전 적용입니다.
사전 내용과 원본 내용을 함께 프롬프트에 포함시킵니다.
번역된 마크다운만 출력하라고 강조해 다른 설명을 막습니다.
max-turns 5로 충분합니다.
번역 후 검증으로 라인 수 차이를 확인합니다.
10줄 이상 차이가 나면 의심스럽다고 경고합니다.
사용자가 검토해야 할 시그널입니다.
