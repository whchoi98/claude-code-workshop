# Slide 45: SessionStart example

**Part 3: HOOKS 4가지 시점**

## Code Blocks

### session start

```bash
#!/bin/bash
# /opt/claude/hooks/session-start.sh

# 1. 정책 배너 출력 (사용자에게 표시)
cat <<EOF >&1
══════════════════════════════════════════════════
  Claude Code - Company Internal Use
══════════════════════════════════════════════════
  ✓ 사용 활동은 사내 SIEM에 기록됩니다
  ✓ 민감 정보 입력은 자동 차단됩니다
  ✓ 비용 한도: 월 $50/인 (초과 시 사용 제한)
  ✓ 정책 위반 시: security@company.com
  
  허용 모델: Sonnet, Haiku (Opus는 별도 신청)
  허용 MCP: jira, confluence, gitlab, github
══════════════════════════════════════════════════
EOF

# 2. 환경 검증
if [ -z "$AWS_PROFILE" ]; then
  echo "⚠ AWS_PROFILE 미설정. SSO 로그인 필요." >&2
fi

if ! aws sts get-caller-identity >/dev/null 2>&1; then
  echo "⚠ AWS 자격증명 만료. aws sso login 실행." >&2
fi

# 3. 사용자 컨텍스트 주입 (stdout이 메인 프롬프트에 추가됨)
echo "## Session Context"
echo "User: $(whoami)"
echo "Project: $(basename $(pwd))"
echo "Git branch: $(git branch --show-current 2>/dev/null)"

exit 0
```

## Speaker Notes

SessionStart 실전 예시입니다.
세 가지 작업을 한 스크립트에서 수행합니다.
첫째, 정책 배너를 stdout으로 출력합니다.
사용자에게 표시되어 정책을 매 세션 인지하게 합니다.
사용 기록, DLP 자동 차단, 비용 한도, 연락처가 명시됩니다.
허용 모델과 MCP 서버 목록도 함께 표시합니다.
둘째, 환경 검증입니다.
AWS_PROFILE 환경변수가 없으면 stderr로 경고합니다.
aws sts get-caller-identity로 자격증명이 유효한지 확인하고 만료 시 SSO 로그인을 안내합니다.
셋째, 사용자 컨텍스트 주입입니다.
stdout으로 출력되는 내용이 메인 프롬프트에 추가됩니다.
user, project, git branch 같은 정보를 포함시켜 Claude가 현재 환경을 즉시 이해하게 합니다.
exit 0으로 종료해 세션이 정상 시작되게 합니다.
