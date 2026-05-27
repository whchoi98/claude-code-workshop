# Slide 115: Real-world command 5: Translate

**Part 7: CUSTOM SLASH COMMANDS**

## Code Blocks

### translate

```bash
# .claude/commands/translate-doc.md
---
description: 문서를 한국어/영어로 번역 (사내 용어 사전 적용)
argument-hint: <file-path> <target-lang>
allowed-tools:
  - Read
  - Write
  - Edit
model: claude-sonnet-4-5
---

$ARGUMENTS 의 첫 인자는 번역할 파일, 둘째는 대상 언어 (ko 또는 en) 입니다.

# 절차
1. 파일을 Read로 읽음
2. 사내 용어 사전 적용 (~/.claude/glossary.md 참고)
3. 자연스러운 톤으로 번역 (직역 금지)
4. 코드 블록과 명령어는 번역하지 않음
5. 결과를 같은 경로의 .ko 또는 .en suffix로 저장

# 사내 용어 사전 예시 (~/.claude/glossary.md)
- user → 사용자 (회원, 유저 사용 금지)
- deploy → 배포 (디플로이 금지)
- repository → 저장소
- pull request → PR (한글: 풀 리퀘스트 사용 금지)
- bug → 버그 (오류 X)

# 출력
1. 번역된 파일 저장 보고
2. 변경된 핵심 용어 5-10개 요약
3. 잘 번역되지 않은 부분 (있다면) 알림

# 호출 예시
> /translate-doc docs/architecture.md ko
> /translate-doc docs/architecture.ko.md en
```

## Speaker Notes

실전 명령 다섯 번째는 문서 번역입니다.
frontmatter에 file-path와 target-lang 두 인자를 받음을 명시합니다.
allowed-tools에 Read, Write, Edit을 허용합니다.
명령 본문은 5단계 절차로 구성됩니다.
1단계 파일을 Read로 읽습니다.
2단계 사내 용어 사전을 ~/.claude/glossary.md에서 참고합니다.
3단계 자연스러운 톤으로 번역하며 직역을 피합니다.
4단계 코드 블록과 명령어는 번역하지 않습니다.
5단계 결과를 .ko 또는 .en suffix로 저장합니다.
사내 용어 사전 예시도 함께 제공합니다.
user는 사용자로 통일하고 유저나 회원 같은 용어를 금지합니다.
deploy는 배포로 deploy 디플로이를 금지합니다.
repository는 저장소, pull request는 PR로 통일합니다.
출력은 번역된 파일 저장 보고, 변경된 핵심 용어 요약, 잘 번역되지 않은 부분 알림입니다.
호출은 파일 경로와 대상 언어 두 인자를 함께 전달합니다.
