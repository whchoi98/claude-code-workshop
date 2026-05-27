# Slide 95: /init 명령

**Part 5: QUICK START**

## Code Blocks

### /init

```bash
$ claude
> /init

Analyzing project structure...
  • Detected: Node.js + TypeScript + Next.js 14
  • Detected: Tailwind CSS, Prisma ORM, PostgreSQL
  • Detected: Jest + Playwright tests
  • Detected: ESLint + Prettier

Generated CLAUDE.md (preview):
  # My App - Claude Code Memory
  ## Tech Stack
  - Next.js 14 (App Router)
  - TypeScript, Tailwind, Prisma
  ## Conventions
  - Components: src/components/**/*.tsx
  - API routes: src/app/api/**/route.ts
  - Tests: *.test.ts colocated
  ## Commands
  - Dev: pnpm dev
  - Test: pnpm test
  - Build: pnpm build

Write to ./CLAUDE.md? (y/N) y
```

## Speaker Notes

/init 명령은 프로젝트 시작 시 가장 먼저 실행하는 명령입니다.
Claude가 프로젝트를 자동 분석해 사용된 기술 스택, 디렉토리 구조, 테스트 도구, 코드 스타일 등을 파악하고 CLAUDE.md 초안을 생성합니다.
예시처럼 Next.js와 TypeScript, Prisma, Jest 같은 스택을 감지하고 컨벤션과 명령어를 정리해 줍니다.
생성 전에 미리보기로 내용을 확인할 수 있고, 동의하면 CLAUDE.md 파일이 프로젝트 루트에 작성됩니다.
이후 자유롭게 편집하면 됩니다.
한 번 만든 CLAUDE.md는 매 세션마다 자동 로드되어 일관된 맥락을 제공하므로 매우 중요합니다.
