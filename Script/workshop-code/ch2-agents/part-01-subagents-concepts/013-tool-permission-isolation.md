# Slide 13: Tool permission isolation

**Part 1: SUBAGENTS 개념과 원리**

## Code Blocks

### tools field

```bash
# .claude/agents/code-reviewer.md
---
name: code-reviewer
description: PR diff를 검토하고 개선 사항을 제안
tools: Read, Grep, Glob, Bash(git diff:*)
model: claude-sonnet-4-5
---

당신은 시니어 코드 리뷰어입니다.
주어진 PR diff를 다음 관점에서 검토하세요:
- 가독성과 명명 규칙
- 잠재적 버그와 엣지 케이스
- 성능 영향
- 테스트 커버리지
```

## Speaker Notes

Subagent의 도구 권한 격리를 살펴봅니다.
각 Subagent는 자신의 정의 파일에 tools 필드로 사용 가능한 도구를 화이트리스트로 명시합니다.
예시는 code-reviewer 에이전트의 정의입니다.
YAML frontmatter에서 name, description, tools, model을 명시합니다.
tools 필드에 Read, Grep, Glob, 그리고 Bash 중에서도 git diff 명령만 허용합니다.
이렇게 권한을 좁히면 에이전트가 Edit이나 Write 같은 위험한 동작을 할 수 없습니다.
리뷰 작업에 필요한 읽기 도구만 가지므로 안전합니다.
시스템 프롬프트 부분은 frontmatter 아래 본문에 작성합니다.
역할과 검토 관점을 명확히 지시합니다.
이 패턴이 최소 권한 원칙을 Subagent 단위로 적용하는 핵심 메커니즘입니다.
