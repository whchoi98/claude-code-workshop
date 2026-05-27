# Slide 60: User policy banner

**Part 4: GOVERNANCE & POLICY**

## Code Blocks

### policy-banner.sh

```bash
#!/bin/bash
# /opt/claude/hooks/policy-banner.sh

cat <<EOF
════════════════════════════════════════════════════════════
  Claude Code - Company Internal Use
════════════════════════════════════════════════════════════
  ✓ 본인 활동은 사내 SIEM에 기록됩니다
  ✓ 민감 정보 (Key, 비밀번호) 입력은 자동 차단됩니다
  ✓ 비용 한도: 월 $50/인 (초과 시 사용 제한)
  ✓ 정책 위반 시 IT 보안팀 연락: security@company.com
  
  허용 모델: Sonnet, Haiku  /  Opus: 별도 신청 필요
  허용 MCP: jira, confluence, gitlab, github
════════════════════════════════════════════════════════════
EOF

# 매 세션 시작 시 정책 안내
# 사용자가 이미 알고 있어도 매번 표시 (의식 제고)
exit 0
```

## Speaker Notes

Policy Banner Hook 예시입니다.
세션 시작 시 사용 정책을 안내하는 스크립트입니다.
표시되는 내용은 사용자 활동이 사내 SIEM에 기록된다는 알림, 민감 정보 입력이 자동 차단된다는 알림, 비용 한도가 월 50달러라는 안내, 정책 위반 시 연락처입니다.
허용 모델과 허용 MCP 서버 목록도 함께 표시합니다.
매 세션 시작 시 표시되며 사용자가 이미 알고 있어도 매번 보여줍니다.
의식 제고 효과가 있습니다.
목적은 두 가지입니다.
사용자의 정책 인식을 제고하는 것과 사고 발생 시 몰랐다는 변명을 차단하는 컴플라이언스 효과입니다.
실행 시점은 SessionStart 후크입니다.
매 세션마다 한 번씩 실행됩니다.
