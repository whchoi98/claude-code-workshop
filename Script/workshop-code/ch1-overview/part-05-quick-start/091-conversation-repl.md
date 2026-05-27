# Slide 91: 대화형 REPL 입문

**Part 5: QUICK START**

## Code Blocks

### REPL session

```bash
$ cd ~/projects/my-app
$ claude
Welcome to Claude Code 1.x.x

  /help    Show available commands
  /init    Initialize CLAUDE.md
  /status  Show session status

> 안녕 Claude, 이 프로젝트 구조 좀 봐 줄래?

[Claude calls tools]
  • Read package.json
  • Glob src/**/*.{ts,tsx}
  • Read README.md

이 프로젝트는 Next.js 14 기반의 풀스택 앱이네요.
주요 구조는...

> 좋아. src/components 안에 새로운 Modal 컴포넌트를 만들어 줘.
  Tailwind 사용하고, ESC로 닫히게.
```

## Speaker Notes

대화형 REPL의 첫 세션 흐름을 살펴봅니다.
프로젝트 디렉토리로 cd 한 후 claude를 실행하면 환영 메시지와 함께 슬래시 명령 안내가 표시됩니다.
사용자 입력 프롬프트는 꺾쇠 기호로 시작하며, 자연어로 자유롭게 요청할 수 있습니다.
예시처럼 프로젝트 구조를 분석해달라고 하면 Claude는 자동으로 Read와 Glob 도구를 호출해 package.json과 소스 파일을 확인한 후 분석 결과를 보고합니다.
이어서 새 컴포넌트 생성 같은 후속 요청을 자연스럽게 이어갈 수 있습니다.
핵심은 현재 디렉토리가 Claude의 워크스페이스가 된다는 점입니다.
