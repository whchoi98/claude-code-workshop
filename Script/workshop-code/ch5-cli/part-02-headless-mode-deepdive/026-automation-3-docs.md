# Slide 26: 자동화 3 / 문서 생성

**Part 2: HEADLESS 모드 심화**

## Code Blocks

### generate-docs.sh

```bash
#!/bin/bash
# generate-docs.sh - API 문서 자동 생성
set -euo pipefail

SRC_DIR="${1:?Usage: generate-docs.sh <src-dir>}"
OUTPUT="docs/API.md"

mkdir -p docs

# 1. 모든 API 라우터 파일 수집
ROUTES=$(find "$SRC_DIR" -name "routes.js" -o -name "*Controller.ts" | head -50)

if [ -z "$ROUTES" ]; then
  echo "라우터 파일을 찾지 못함" >&2
  exit 1
fi

# 2. Claude에게 문서 생성 요청
claude -p "$(cat <<EOF
다음 API 라우터 파일들을 분석해서 종합 API 문서를 작성하세요.

대상 파일:
$ROUTES

문서 구성:
1. 개요 (API 카테고리 분류)
2. 인증 방법
3. 엔드포인트 (HTTP 메서드, 경로, 인자, 응답, 예시)
4. 에러 코드
5. Rate Limiting
6. 변경 이력

각 엔드포인트는 다음 형식으로:
\`\`\`
### POST /api/users
사용자 생성

**Request:**
{ "name": "...", "email": "..." }

**Response (201):**
{ "id": "...", "name": "...", "createdAt": "..." }
\`\`\`
EOF
)" \
  --allowed-tools "Read,Grep,Glob" \
  --max-turns 30 \
  --output-format json | jq -r '.result' > "$OUTPUT"

echo "✓ API 문서 생성: $OUTPUT ($(wc -l < $OUTPUT) lines)"
```

## Speaker Notes

자동화 3번 API 문서 생성 스크립트입니다.
소스 디렉토리를 인자로 받습니다.
1단계 모든 라우터 파일을 수집합니다.
routes.js나 Controller.ts 파일을 find로 찾습니다.
파일이 없으면 stderr로 에러를 출력하고 exit 1입니다.
2단계 Claude에게 문서 생성을 요청합니다.
heredoc으로 문서 구성 6가지를 명시합니다.
개요, 인증 방법, 엔드포인트, 에러 코드, Rate Limiting, 변경 이력입니다.
각 엔드포인트의 정확한 형식 예시도 제공합니다.
Return, Request, Response를 포함한 표준 형식입니다.
allowed-tools에 Read, Grep, Glob을 허용해 코드 탐색이 가능합니다.
max-turns 30으로 충분한 다단계 작업을 허용합니다.
출력은 docs/API.md로 저장되고 라인 수를 보고합니다.
