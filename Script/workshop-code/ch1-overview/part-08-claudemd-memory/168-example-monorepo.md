# Slide 168: Example - Monorepo

**Part 8: CLAUDE.md & MEMORY**

## Code Blocks

### Monorepo example

```bash
# Monorepo: company-platform

## Structure (Turborepo)
- apps/web         Next.js 15 프론트엔드
- apps/api         Fastify 4 백엔드
- apps/admin       Admin SPA
- packages/ui      공유 컴포넌트 라이브러리
- packages/types   공유 TypeScript 타입
- packages/utils   공통 유틸 함수

## Commands (루트에서)
- 전체 개발: pnpm dev
- 특정 앱만: pnpm dev --filter web
- 빌드: pnpm build
- 패키지 전체 테스트: pnpm test
- 한 패키지만 테스트: pnpm test --filter @company/ui

## Conventions
- 새 공유 코드는 packages/ 아래 (apps 간 직접 import 금지)
- 버전 관리: changesets (pnpm changeset)
- 의존성 추가: pnpm add -F <package-name>

@./docs/architecture.md
@./docs/release-process.md
```

## Speaker Notes

두 번째 실전 예시는 모노레포 프로젝트입니다.
Structure 섹션에 apps와 packages 디렉토리 구조를 명확히 설명합니다.
Commands 섹션에서는 루트에서 실행하는 pnpm 명령과 --filter 플래그로 특정 패키지만 다루는 방법을 명시합니다.
Conventions에서는 모노레포 핵심 규칙을 명시합니다.
마지막으로 @import 문법으로 문서를 모듈화해 큰 CLAUDE.md도 깔끔하게 분할 관리합니다.
