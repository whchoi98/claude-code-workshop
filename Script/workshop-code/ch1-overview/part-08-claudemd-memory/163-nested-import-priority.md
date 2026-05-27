# Slide 163: Nested Import Priority

**Part 8: CLAUDE.md & MEMORY**

## Code Blocks

### PRIORITY

```bash
# 적용 우선순위 예시

Enterprise   /etc/claude/CLAUDE.md
  @/etc/claude/security-policy.md
  @/etc/claude/approved-tools.md

User         ~/.claude/CLAUDE.md
  @~/.claude/code-style.md

Project      ./CLAUDE.md
  @./docs/architecture.md
  @./docs/api-conventions.md

Local        ./.claude/local.md

# 충돌 시 (예: 들여쓰기 4칸 vs 2칸)
1. Local      → 가장 강함 (개인 X 프로젝트)
2. Project    → 팀 컨벤션
3. User       → 개인 기본값
4. Enterprise → 조직 정책

# Claude는 모든 내용을 합쳐 컨텍스트로 활용
```

## Speaker Notes

중첩 임포트가 일어날 때 우선순위가 중요합니다.
4계층 메모리가 모두 임포트를 사용해 여러 파일을 끌어올 수 있는데, 충돌이 발생하면 Local이 가장 우선하고, 그 다음 Project, User, Enterprise 순서입니다.
즉, 더 구체적이고 더 가까운 컨텍스트가 우선합니다.
보안 정책 같은 강제 사항은 Enterprise가 명시적으로 강제할 수 있습니다.
