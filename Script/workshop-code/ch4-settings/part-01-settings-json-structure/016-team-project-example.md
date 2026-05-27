# Slide 16: Team project example

**Part 1: settings.json 구조**

## Code Blocks

### team

```bash
# .claude/settings.json (Git 커밋, 팀 공유)
{
  "permissions": {
    "allow": [
      "Read(src/**)", "Read(tests/**)", "Read(docs/**)",
      "Edit(src/**)", "Edit(tests/**)", "Edit(docs/**)",
      "Bash(npm test:*)", "Bash(npm run lint)",
      "Bash(npm run build)"
    ],
    "ask": [
      "Write(**)", "Bash(git push:*)", "Bash(git commit:*)"
    ],
    "deny": [
      "Read(**/.env*)", "Read(**/secrets/**)",
      "Bash(rm -rf:*)", "Bash(curl:*)"
    ]
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [{
          "type": "command",
          "command": "npm run lint -- --fix"
        }]
      }
    ]
  },
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"]
    }
  }
}
```

## Speaker Notes

완성 예시 두 번째는 팀 프로젝트입니다.
.claude/settings.json에 작성해 Git에 커밋, 팀과 공유합니다.
permissions의 allow에는 프로젝트 디렉토리만 명시합니다.
src, tests, docs 디렉토리만 Read와 Edit이 자동 허용됩니다.
npm test, lint, build 같은 빌드 명령이 자동 허용됩니다.
ask에는 Write, git push, git commit을 두어 영구 영향 작업은 확인을 받습니다.
deny에는 환경 파일이나 secrets 디렉토리 읽기, rm 명령, curl 명령을 차단합니다.
hooks의 PostToolUse에 Write나 Edit 후 자동 lint fix를 적용합니다.
매번 Claude가 파일을 수정하면 자동으로 lint가 실행되어 코드 스타일이 일관 유지됩니다.
mcpServers에 github 서버를 추가해 PR 검토나 issue 작성 같은 작업이 가능하게 합니다.
팀 전체가 같은 설정을 쓰므로 일관된 경험을 보장합니다.
