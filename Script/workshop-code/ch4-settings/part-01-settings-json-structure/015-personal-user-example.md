# Slide 15: Personal user example

**Part 1: settings.json 구조**

## Code Blocks

### personal

```bash
# ~/.claude/settings.json
{
  "permissions": {
    "allow": [
      "Read", "Grep", "Glob", "WebFetch",
      "Bash(git diff:*)", "Bash(git log:*)",
      "Bash(npm test:*)", "Bash(npm run:*)"
    ],
    "ask": ["Edit", "Write", "Bash(git push:*)"]
  },
  "model": "claude-sonnet-4-5",
  "modelAlias": {
    "fast": "claude-haiku-4-5",
    "smart": "claude-opus-4-5"
  },
  "theme": "dark",
  "outputStyle": "concise",
  "editor": {
    "tabWidth": 2,
    "preferredQuotes": "single"
  },
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem",
                "/Users/me/Documents"]
    }
  }
}
```

## Speaker Notes

완성 예시 첫 번째는 개인 사용자입니다.
~/.claude/settings.json에 작성하는 형태입니다.
permissions를 봅니다.
allow에 Read, Grep, Glob, WebFetch 같은 안전한 도구를 모두 자동 허용합니다.
git diff와 git log, npm test와 npm run 같은 안전한 명령도 자동 허용합니다.
ask에는 Edit, Write, git push만 두어 변경 작업은 확인을 받습니다.
model을 Sonnet으로 기본 지정하고 fast와 smart 별명을 등록합니다.
theme은 dark이고 outputStyle은 concise로 간결한 응답을 선호합니다.
editor 선호에서 tab width 2와 single quotes를 명시합니다.
mcpServers에 filesystem 서버를 추가해 Documents 디렉토리에 접근 가능하게 합니다.
개인 개발자의 일상 사용에 최적화된 설정입니다.
