# Slide 107: Command basics

**Part 7: CUSTOM SLASH COMMANDS**

## Code Blocks

### basics

```bash
# 1. 디렉토리 생성 (프로젝트 또는 사용자 전역)
$ mkdir -p .claude/commands
# 또는 사용자 전역:
$ mkdir -p ~/.claude/commands

# 2. 명령 파일 생성 (Markdown)
$ cat > .claude/commands/review.md <<'EOF'
다음 git diff를 코드 리뷰해 주세요.
관점: 가독성, 안전성, 성능.
출력 형식: 우선순위별 정리 (Critical/Important/Suggestion).
EOF

# 3. claude에서 호출
> /review
# 또는 인자와 함께:
> /review HEAD~3

# 4. 파일 이름이 명령 이름이 됨
# review.md → /review
# deploy.md → /deploy
# fix-bug.md → /fix-bug

# 5. 자동 노출
> /                # 슬래시 입력 시 사용 가능한 명령 목록 표시
  /review
  /deploy
  /fix-bug
  ...

# 6. 우선순위
# 프로젝트 명령 > 사용자 명령 > 빌트인 명령
# 같은 이름이면 더 상위가 사용됨
```

## Speaker Notes

Slash Command 기본을 살펴봅니다.
1단계 디렉토리를 생성합니다.
프로젝트별은 .claude/commands, 사용자 전역은 홈 디렉토리에 만듭니다.
2단계 Markdown 파일로 명령을 정의합니다.
review.md 파일에 코드 리뷰 요청 내용을 작성합니다.
파일 내용 전체가 프롬프트로 전달됩니다.
3단계 claude에서 슬래시와 함께 호출합니다.
/review 명령으로 호출하며 인자도 함께 전달할 수 있습니다.
4단계 파일 이름이 명령 이름이 됩니다.
review.md는 /review, deploy.md는 /deploy로 호출됩니다.
5단계 자동 노출입니다.
슬래시만 입력하면 사용 가능한 모든 명령이 목록으로 표시됩니다.
6단계 우선순위는 프로젝트, 사용자, 빌트인 순입니다.
같은 이름이면 더 상위 명령이 사용됩니다.
프로젝트에 정의된 review가 빌트인 review보다 우선입니다.
