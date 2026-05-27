# Slide 24: YAML frontmatter structure

**Part 2: SUBAGENT 정의 방법**

## Code Blocks

### YAML frontmatter

```bash
# .claude/agents/example.md

---
name: code-reviewer
description: PR diff를 검토하고 개선 사항을 제안하는 시니어 리뷰어
tools: Read, Grep, Glob, Bash(git diff:*)
model: claude-sonnet-4-5
---

여기서부터는 시스템 프롬프트 본문입니다.
당신은 시니어 코드 리뷰어입니다.
주어진 코드 변경을 다음 관점에서 검토하세요.
- 가독성
- 안전성
- 성능
- 테스트 커버리지
```

## Speaker Notes

YAML frontmatter 구조를 살펴봅니다.
Subagent 정의 파일은 두 부분으로 나뉩니다.
파일 상단의 frontmatter와 그 아래 시스템 프롬프트 본문입니다.
frontmatter는 세 개의 하이픈으로 시작하고 끝납니다.
그 안에 YAML 형식으로 4가지 필드를 정의합니다.
name은 에이전트의 고유 이름입니다.
description은 어떤 작업에 적합한지 설명합니다.
tools는 사용 가능한 도구 화이트리스트입니다.
model은 사용할 Claude 모델을 지정합니다.
frontmatter가 끝난 후 빈 줄을 두고 시스템 프롬프트 본문이 시작됩니다.
본문은 자연어로 에이전트의 역할과 행동 규칙을 작성합니다.
