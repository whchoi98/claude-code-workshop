# Slide 28: 자동화 5 / 검증

**Part 2: HEADLESS 모드 심화**

## Code Blocks

### validate-code.sh

```bash
#!/bin/bash
# validate-code.sh - 변경 코드 검증 (pre-commit hook용)
set -euo pipefail

# Git에서 staged 파일 가져옴
STAGED=$(git diff --cached --name-only --diff-filter=ACM | \
         grep -E '\.(js|ts|py|go)$' || true)

if [ -z "$STAGED" ]; then
  echo "검증할 코드 파일 없음"
  exit 0
fi

echo "검증 대상: $STAGED"

# 각 파일 검증
FAILED=0
for file in $STAGED; do
  RESULT=$(claude -p "$(cat <<EOF
다음 파일을 검증하세요. 문제가 있으면 PROBLEM, 없으면 OK 한 단어로 응답.

검증 항목:
- 시크릿/토큰 노출
- 명백한 보안 취약점
- 데이터 손실 위험

파일 ($file):
$(cat "$file")
EOF
)" \
    --allowed-tools "Read" \
    --max-turns 3 \
    --output-format json | jq -r '.result' | head -1)

  if [ "$RESULT" != "OK" ]; then
    echo "✗ $file: $RESULT"
    FAILED=$((FAILED + 1))
  else
    echo "✓ $file"
  fi
done

if [ $FAILED -gt 0 ]; then
  echo "🚫 $FAILED개 파일 검증 실패. commit 차단" >&2
  exit 1
fi

echo "✓ 모든 파일 검증 통과"

# .git/hooks/pre-commit에 심볼릭 링크
# $ ln -s ../../validate-code.sh .git/hooks/pre-commit
```

## Speaker Notes

자동화 5번 코드 검증 스크립트입니다.
pre-commit 훅용으로 설계되었습니다.
Git에서 staged 파일을 추출하되 .js, .ts, .py, .go 확장자만 대상으로 합니다.
파일이 없으면 즉시 통과합니다.
각 파일을 검증합니다.
claude에게 PROBLEM 또는 OK 한 단어로만 응답하라고 지시합니다.
검증 항목은 시크릿이나 토큰 노출, 명백한 보안 취약점, 데이터 손실 위험입니다.
allowed-tools에 Read만 허용해 안전합니다.
max-turns 3으로 빠른 응답을 강제합니다.
결과가 OK가 아니면 실패 카운트를 증가시키고 어떤 파일이 어떤 문제로 실패했는지 표시합니다.
하나라도 실패하면 exit 1로 커밋을 차단합니다.
설치는 .git/hooks/pre-commit에 심볼릭 링크로 연결합니다.
매 commit 전 자동으로 안전성을 검증하는 안전망입니다.
