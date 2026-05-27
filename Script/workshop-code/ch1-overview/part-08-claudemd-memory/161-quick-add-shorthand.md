# Slide 161: # Quick Add Shorthand

**Part 8: CLAUDE.md & MEMORY**

## Code Blocks

### # shortcut

```bash
# 사용 예시

> 이 프로젝트는 pnpm 사용해. 항상 pnpm으로 명령 실행해 줘.
# pnpm 사용 (npm/yarn 대신)

✓ ./CLAUDE.md > ## Tools 섹션에 추가됨
  "pnpm 사용 (npm/yarn 대신)"

# 다른 예
> # 모든 PR은 반드시 reviewer 1명 이상 지정 필수
✓ ./CLAUDE.md > ## Workflow 섹션에 추가됨

# 어느 메모리에 추가할지 명시
> # @user 개인 들여쓰기는 2칸 선호
✓ ~/.claude/CLAUDE.md > ## Code Style 섹션에 추가됨

# 단축 문법: 메시지 시작 부분에 #
# Claude가 적절한 섹션을 추론해 추가
```

## Speaker Notes

# 단축 문법은 대화 중 빠르게 메모리에 한 줄을 추가하는 방법입니다.
메시지 시작 부분에 # 기호를 두면 그 줄이 메모리 파일에 추가됩니다.
Claude가 적절한 섹션을 자동으로 추론해 그 섹션에 추가하므로 사용자가 어느 섹션인지 일일이 명시할 필요가 없습니다.
어느 메모리 파일에 추가할지 지정하고 싶으면 @user나 @local 같은 마커를 함께 사용합니다.
