# Slide 160: /memory Edit Command

**Part 8: CLAUDE.md & MEMORY**

## Code Blocks

### /memory

```bash
> /memory

Memory Files:
  1. Project    ./CLAUDE.md          [edit]
  2. User       ~/.claude/CLAUDE.md  [edit]
  3. Local      ./.claude/local.md   [edit]
  4. Enterprise /etc/claude/CLAUDE.md  [read-only]

Select [1-4]: 1

# Project: my-app
## Stack
- TypeScript 5.4 / React 18 / Vite 5
...

[ 자동 편집기 열림 - $EDITOR 환경변수 기준 ]
# 편집 완료 후 :wq 또는 Ctrl-S

✓ ./CLAUDE.md 갱신됨 (다음 메시지부터 반영)
```

## Speaker Notes

/memory 명령은 메모리 파일을 대화형으로 편집할 수 있게 해 줍니다.
명령을 입력하면 4개 메모리 파일 목록이 나오고, 번호를 선택하면 그 파일이 시스템 환경변수 EDITOR에 지정된 편집기로 열립니다.
편집을 마치고 저장하면 다음 메시지부터 즉시 새 내용이 반영됩니다.
별도로 텍스트 편집기를 열 필요 없이 작업 흐름 안에서 빠르게 메모리를 갱신할 수 있어 유용한 명령입니다.
