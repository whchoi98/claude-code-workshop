# Slide 136: Lab 4 / Custom Slash Command

**Part 9: RECAP & 4 LABS**

## Code Blocks

### Lab 4

```bash
# 1. 프로젝트에 .claude/commands 디렉토리 생성
$ cd ~/my-project
$ mkdir -p .claude/commands

# 2. 명령 파일 작성 (.claude/commands/standup.md)
$ cat > .claude/commands/standup.md <<'EOF'
---
description: 매일 stand-up 자동 생성 (어제 한 일 + 오늘 할 일)
allowed-tools:
  - Bash(git log:*)
  - Read
---

# 1. 어제 한 일 - 본인의 어제 commit 추출
어제 (yesterday) 본인의 git commit 목록을 가져와서
사람이 읽기 쉬운 형태로 정리해 주세요.

# 2. 오늘 할 일 - $ARGUMENTS 분석
$ARGUMENTS 가 있다면 오늘 할 일 후보입니다.
없다면 진행 중인 PR이나 issue를 살펴보고 추천해 주세요.

# 3. 출력 형식
## Standup - 2026-05-25

### 어제
- ✅ <commit message 1>
- ✅ <commit message 2>

### 오늘
- 🎯 <task 1>
- 🎯 <task 2>

### 블로커
- (있다면) <blocker description>

복사해서 Slack에 붙여넣기 좋은 형식으로 작성.
EOF

# 3. 사용
> /standup
> /standup "이슈 #123 마무리, 코드 리뷰 2건"

# 4. Git에 공유
$ git add .claude/commands/standup.md
$ git commit -m "feat: add /standup command"
$ git push

# 5. 팀 데모 (선택)
```

## Speaker Notes

Lab 4는 Custom Slash Command 작성 실습입니다.
약 25분 소요됩니다.
팀에 실제 도움이 되는 standup 명령을 만듭니다.
1단계 프로젝트에 .claude/commands 디렉토리를 생성합니다.
2단계 standup.md 파일을 작성합니다.
frontmatter에 description과 allowed-tools를 명시합니다.
git log와 Read만 허용합니다.
명령 본문은 3가지 작업입니다.
어제 한 일은 어제 본인의 git commit을 정리합니다.
오늘 할 일은 $ARGUMENTS가 있으면 사용하고 없으면 진행 중인 PR이나 issue에서 추천합니다.
출력 형식을 명시합니다.
어제, 오늘, 블로커 섹션으로 구조화합니다.
복사해서 Slack에 붙여넣기 좋은 형식으로 작성하도록 안내합니다.
3단계 사용 테스트입니다.
/standup으로 호출하거나 인자를 함께 전달합니다.
4단계 Git에 커밋해 팀과 공유합니다.
5단계 팀 stand-up에서 데모를 합니다.
매일 사용할 실용 명령을 직접 만든 경험을 얻습니다.
