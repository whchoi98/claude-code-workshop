# Slide 79: Pre-commit hook integration

**Part 6: PATTERN 3 / SECURITY SCANNER**

## Code Blocks

### pre-commit

```bash
# .git/hooks/pre-commit (또는 husky 등 사용)
#!/bin/bash

# 1. 스테이지된 파일에서 시크릿 검사
git diff --cached | claude -p \
  "security-scanner로 이 변경에 시크릿이 있는지 검사" \
  --output-format json > /tmp/sec-check.json

# 2. critical 시 커밋 차단
CRITICAL=$(jq '.issues[] | select(.severity == "critical") | length' \
           /tmp/sec-check.json)

if [ "$CRITICAL" -gt 0 ]; then
  echo "❌ Critical security issues found. Commit blocked."
  jq '.issues[] | select(.severity == "critical")' /tmp/sec-check.json
  exit 1
fi

echo "✓ Security check passed."
exit 0

# 사용자 경험
$ git commit -m "feat: new feature"
[claude 실행 중...]
❌ Critical security issues found. Commit blocked.
[Secret Leak] src/config.js:5 — AWS_SECRET_ACCESS_KEY 하드코딩
```

## Speaker Notes

Pre-commit Hook 통합 예시입니다.
커밋 직전에 자동으로 보안 검사를 수행하는 워크플로입니다.
Git pre-commit hook 또는 husky 같은 도구로 구현합니다.
2단계로 동작합니다.
1단계는 스테이지된 파일에서 시크릿 검사입니다.
git diff --cached 결과를 claude 명령에 파이프합니다.
security-scanner로 변경에 시크릿이 있는지 검사합니다.
JSON 출력 형식을 사용합니다.
2단계는 critical 발견 시 커밋 차단입니다.
jq로 critical severity 이슈를 카운트합니다.
하나라도 있으면 exit 1로 커밋을 차단합니다.
사용자 경험을 보겠습니다.
git commit 명령 실행 시 claude가 백그라운드에서 실행됩니다.
Critical 이슈가 발견되면 명확한 메시지와 함께 커밋이 차단됩니다.
어떤 시크릿이 어디서 발견되었는지 함께 표시됩니다.
사용자는 즉시 수정하고 다시 커밋할 수 있습니다.
