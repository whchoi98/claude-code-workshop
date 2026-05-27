# Slide 43: Markdown → HTML 변환

**Part 3: 출력 형식과 파싱 심화**

## Code Blocks

### MD to HTML

```typescript
# 시나리오: Claude의 Markdown 응답을 HTML 리포트로

# 1. pandoc로 변환 (가장 쉬움)
$ claude -p "주간 보고서 작성" --output-format json | \
    jq -r '.result' | \
    pandoc -f markdown -t html5 -s \
      --metadata title="Weekly Report" \
      -o report.html

# 2. CSS 스타일 적용
$ claude -p "..." --output-format json | jq -r '.result' | \
    pandoc -f markdown -t html5 -s \
      --css style.css \
      --highlight-style tango \
      -o report.html

# 3. 템플릿 사용
$ claude -p "..." --output-format json | jq -r '.result' > body.md
$ cat <<EOF > report.html
<!DOCTYPE html>
<html><head>
<title>Report - $(date +%Y-%m-%d)</title>
<style>body { max-width: 800px; margin: auto; }</style>
</head><body>
$(pandoc body.md -t html5)
</body></html>
EOF

# 4. node로 변환 (marked 라이브러리)
$ claude -p "..." --output-format json | jq -r '.result' | \
    node -e "
      const marked = require('marked');
      const stdin = require('fs').readFileSync(0, 'utf8');
      console.log(marked.parse(stdin));
    " > report.html

# 5. 메타데이터 포함
$ RESP=$(claude -p "..." --output-format json)
$ TOKENS=$(echo "$RESP" | jq '.usage.output_tokens')
$ DURATION=$(echo "$RESP" | jq '.duration_ms')
$ {
    echo "<!-- Tokens: $TOKENS, Duration: ${DURATION}ms -->"
    echo "$RESP" | jq -r '.result' | pandoc -f markdown -t html5
  } > report.html
```

## Speaker Notes

Markdown을 HTML로 변환하는 패턴입니다.
Claude의 Markdown 응답을 HTML 리포트로 만드는 시나리오입니다.
1번 pandoc은 가장 표준적인 도구입니다.
-f markdown -t html5로 변환하고 -s로 standalone HTML을 만듭니다.
metadata title로 페이지 제목을 명시합니다.
2번 CSS 스타일을 적용합니다.
--css 옵션으로 외부 스타일시트, --highlight-style로 코드 하이라이팅 스타일을 지정합니다.
3번 템플릿 사용 패턴입니다.
heredoc으로 HTML 골격을 만들고 그 안에 pandoc 변환 결과를 삽입합니다.
4번 node와 marked 라이브러리도 사용 가능합니다.
require marked 후 stdin을 읽어 변환합니다.
5번 메타데이터 포함입니다.
HTML 주석으로 토큰 사용량과 응답 시간을 기록해 추적 가능하게 합니다.
이 패턴들로 자동 생성된 리포트를 웹에 게시할 수 있습니다.
