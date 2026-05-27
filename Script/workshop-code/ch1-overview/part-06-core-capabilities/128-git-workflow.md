# Slide 128: Git workflow

**Part 6: CORE CAPABILITIES**

## Code Blocks

### Git basics

```bash
# Claude Code는 Git 명령을 자유롭게 활용

# 상태 확인 (자주 사용됨)
Bash("git status")
Bash("git diff")
Bash("git log --oneline -20")

# 브랜치 생성/전환
Bash("git checkout -b feat/user-pagination")
Bash("git switch main")

# 변경사항 스테이징 / 커밋
Bash("git add src/users/")
Bash("git commit -m '...'", ...)  # 메시지 자동 작성

# 푸시
Bash("git push -u origin feat/user-pagination")

# 권한 정책 예시 (settings.json)
"allow": ["Bash(git status)", "Bash(git diff:*)",
          "Bash(git log:*)", "Bash(git branch:*)"],
"ask":   ["Bash(git push:*)", "Bash(git merge:*)"]
```

## Speaker Notes

Claude Code는 Git 명령을 Bash 도구로 자유롭게 활용합니다.
상태 확인을 위해 git status, git diff, git log를 자주 자동 호출합니다.
브랜치 생성과 전환은 git checkout이나 git switch를 사용합니다.
변경사항 스테이징과 커밋은 git add와 git commit을 사용하는데, 커밋 메시지는 Claude가 변경 내용을 분석해 자동 작성합니다.
권한 정책 예시에서 git status, diff, log, branch 같은 읽기 명령은 자동 허용, push와 merge는 사용자 확인을 받는 것이 일반적인 안전 정책입니다.
