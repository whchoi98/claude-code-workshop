# Slide 155: Project Memory

**Part 8: CLAUDE.md & MEMORY**

## Code Blocks

### ./CLAUDE.md

```bash
# Project: my-app

## Stack
- TypeScript 5.4 / React 18 / Vite 5
- Express 4 / Prisma / PostgreSQL 15
- Jest + React Testing Library

## Commands
- 개발: pnpm dev
- 빌드: pnpm build
- 테스트: pnpm test (감시: pnpm test:watch)
- 린트: pnpm lint
- 마이그레이션: pnpm prisma migrate dev

## Conventions
- 함수형 컴포넌트 + Hooks (Class 금지)
- 타입은 src/types/ 에 모음
- 신규 API는 src/server/routes/ 아래 추가
- 모든 PR에는 테스트 동반 필수
```

## Speaker Notes

Project Memory는 프로젝트 루트의 ./CLAUDE.md에 위치하며 가장 자주 사용되는 메모리 계층입니다.
화면 예시처럼 Stack 섹션에 사용 기술과 버전을, Commands 섹션에 빌드, 테스트, 린트 같은 자주 쓰는 명령을, Conventions 섹션에 함수형 컴포넌트 사용 같은 코드 컨벤션을 명시합니다.
이 파일은 Git에 포함되어 버전 관리되므로 팀 전체가 공유합니다.
claude 명령으로 세션을 시작하면 자동으로 로드되어 매번 동일한 컨텍스트에서 작업이 시작됩니다.
