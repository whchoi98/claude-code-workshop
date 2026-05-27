# Slide 133: allow/deny patterns

**Part 6: CORE CAPABILITIES**

## Code Blocks

### permissions

```bash
# settings.json 또는 --allowed-tools 플래그
{
  "permissions": {
    "allow": [
      "Read(**)",                    # 모든 파일 읽기
      "Glob(**)", "Grep(**)",        # 모든 검색
      "Bash(git status)",            # 정확 매칭
      "Bash(git diff:*)",            # git diff 시작
      "Bash(git log:*)",
      "Bash(npm test:*)",
      "Bash(npm run test*)",
      "Bash(node --version)",
      "WebSearch(**)",
    ],
    "ask": [
      "Edit(**)", "Write(**)",
      "Bash(git push:*)",
      "Bash(git commit:*)",
      "Bash(npm install:*)",
    ],
    "deny": [
      "Bash(rm -rf:*)",
      "Bash(sudo:*)",
      "Bash(curl * | sh)",
      "Bash(* | bash)",
      "Edit(.env)", "Edit(secrets/**)"
    ]
  }
}
```

## Speaker Notes

실전에서 자주 쓰는 permissions 패턴을 정리했습니다.
allow 섹션에는 모든 파일 읽기, Glob과 Grep 같은 검색, git의 읽기 명령들, npm test 같은 비파괴 명령들이 들어갑니다.
ask 섹션에는 Edit과 Write 같은 파일 수정, git push와 commit, npm install 같은 변경 명령이 들어갑니다.
deny 섹션에는 rm -rf, sudo, curl pipe to shell 같은 위험 명령과 함께 .env 파일이나 secrets 폴더 같은 민감한 파일의 편집을 차단합니다.
