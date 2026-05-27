# Slide 158: Enterprise Memory

**Part 8: CLAUDE.md & MEMORY**

## Code Blocks

### /etc/claude/CLAUDE.md

```bash
# /etc/claude/CLAUDE.md  (시스템 전체 적용)

## Company Policy
- 사내 코드를 외부에 절대 노출 금지
- 모든 commit message는 한국어 + 영어 병행
- AI 생성 코드는 PR description에 [AI-generated] 표기

## Required Practices
- 모든 신규 API는 OpenAPI 스펙 포함
- DB 변경은 마이그레이션 파일 필수
- 비밀번호/API Key/PII는 코드에 절대 포함 금지

## Approved Tools
- 사내 패키지 저장소: https://npm.company.internal
- 사내 Docker registry: registry.company.internal
- 사내 MCP 서버: mcp://internal.company.local

## Restrictions
- 외부 패키지 신규 도입은 보안팀 승인 후
```

## Speaker Notes

Enterprise Memory는 시스템 전체에 적용되는 조직 차원의 정책 파일로, /etc/claude/CLAUDE.md에 위치합니다.
IT 팀이 MDM이나 Ansible 같은 도구로 모든 사용자 머신에 배포하며, 일반 사용자가 수정할 수 없도록 권한이 제한됩니다.
사내 코드 노출 금지, 커밋 메시지 규칙 같은 회사 정책, OpenAPI 스펙 의무화 같은 필수 관행, 사내 패키지 저장소나 Docker registry 같은 승인된 도구, 그리고 외부 패키지 도입 절차 같은 제약 사항을 명시합니다.
Chapter 3 Admin Setup에서 이 파일의 배포와 관리를 자세히 다룹니다.
