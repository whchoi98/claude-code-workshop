# Slide 81: Pattern 3 / 변환 스크립트

**Part 5: 자동화 패턴**

## Code Blocks

### migrate-files.sh

```bash
#!/bin/bash
# migrate-files.sh - 대규모 코드 마이그레이션
set -euo pipefail

PATTERN="${1:?Usage: migrate-files.sh <glob> <rules-file>}"
RULES_FILE="${2:?}"

mkdir -p .migration/{backup,failed,success}

# 변환 규칙 로드
RULES=$(cat "$RULES_FILE")

# 파일 목록
FILES=$(find . -type f -name "$PATTERN" \
  -not -path "./node_modules/*" \
  -not -path "./.migration/*")

TOTAL=$(echo "$FILES" | wc -l)
COUNT=0

echo "총 $TOTAL개 파일 마이그레이션 시작"

# 각 파일 변환
for file in $FILES; do
  COUNT=$((COUNT + 1))
  echo "[$COUNT/$TOTAL] $file"

  # 백업
  cp "$file" ".migration/backup/$(echo "$file" | tr '/' '_')"

  # AI 변환
  ORIGINAL=$(cat "$file")
  NEW=$(claude -p "$(cat <<EOF
다음 코드를 변환 규칙에 따라 마이그레이션:

변환 규칙:
$RULES

원본 코드 ($file):
$ORIGINAL

변환된 코드만 출력 (설명 없이).
EOF
)" \
    --allowed-tools "Read" \
    --max-turns 3 \
    --output-format json | jq -r '.result')

  # 결과 저장
  echo "$NEW" > "$file"

  # 즉시 테스트
  if npm test --silent -- "$file" 2>/dev/null; then
    cp "$file" ".migration/success/$(echo "$file" | tr '/' '_')"
    echo "  ✓ 통과"
  else
    # 실패 시 원본 복원
    cp ".migration/backup/$(echo "$file" | tr '/' '_')" "$file"
    cp "$file.failed" ".migration/failed/" 2>/dev/null || true
    echo "  ✗ 실패 (롤백 완료)"
  fi
done

# 통계
SUCCESS=$(ls .migration/success | wc -l)
FAILED=$(ls .migration/failed | wc -l)
echo "완료: $SUCCESS 성공, $FAILED 실패"
```

## Speaker Notes

Pattern 3 변환 스크립트 migrate-files.sh입니다.
인자로 파일 패턴과 변환 규칙 파일을 받습니다.
.migration 디렉토리를 만들고 그 안에 backup, failed, success 서브 디렉토리를 준비합니다.
변환 규칙을 파일에서 로드합니다.
예를 들어 Vue 2에서 Vue 3 변환 규칙들이 들어 있습니다.
find로 변환 대상 파일 목록을 만듭니다.
node_modules와 .migration 자체는 제외합니다.
각 파일에 대해 변환을 진행합니다.
먼저 .migration/backup에 백업합니다.
슬래시를 언더스코어로 바꿔 파일명으로 사용합니다.
claude에게 변환 규칙과 원본을 주고 변환된 코드만 출력하라고 합니다.
새 내용으로 파일을 덮어씁니다.
즉시 npm test로 테스트를 실행합니다.
통과하면 .migration/success로 복사 표시합니다.
실패하면 백업에서 원본을 복원합니다.
자동 롤백으로 안전성을 확보합니다.
마지막에 성공과 실패 통계를 보고합니다.
