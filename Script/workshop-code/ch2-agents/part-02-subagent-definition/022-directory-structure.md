# Slide 22: Directory structure

**Part 2: SUBAGENT 정의 방법**

## Code Blocks

### Directory

```bash
# 1. 프로젝트 수준 (팀 공유, Git 커밋 대상)
your-project/
├── .claude/
│   ├── agents/
│   │   ├── code-reviewer.md      ← Subagent 정의 파일
│   │   ├── test-writer.md
│   │   ├── docs-writer.md
│   │   └── security-scanner.md
│   ├── settings.json
│   └── CLAUDE.md
└── src/

# 2. 사용자 수준 (개인 전역, 모든 프로젝트에서 사용)
~/.claude/
└── agents/
    ├── my-personal-helper.md
    └── language-translator.md

# 3. 파일 형식: 항상 .md (Markdown with YAML frontmatter)
```

## Speaker Notes

Subagent 파일이 저장되는 디렉토리 구조를 살펴봅니다.
두 가지 위치가 있습니다.
첫 번째는 프로젝트 수준입니다.
프로젝트 루트의 .claude/agents 디렉토리에 저장합니다.
팀 전체가 공유하며 Git에 커밋해 버전 관리합니다.
code-reviewer.md, test-writer.md 같은 형태로 파일을 만듭니다.
두 번째는 사용자 수준입니다.
홈 디렉토리 아래 ~/.claude/agents에 저장합니다.
개인 전역으로 모든 프로젝트에서 사용할 수 있습니다.
파일 형식은 항상 .md 확장자입니다.
Markdown 본문에 YAML frontmatter를 함께 사용하는 형식입니다.
같은 이름이 두 위치에 모두 있으면 프로젝트 수준이 우선됩니다.
