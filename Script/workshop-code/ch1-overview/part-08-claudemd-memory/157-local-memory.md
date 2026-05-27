# Slide 157: Local Memory

**Part 8: CLAUDE.md & MEMORY**

## Code Blocks

### .claude/local.md

```bash
# Local-only Memory (.gitignore 포함)

## Local Dev Environment
- 데이터베이스: postgres://localhost:5433 (포트 충돌)
- API Key: 시크릿 매니저에서 자동 로드 → ENV 주입
- 사내 프록시: 사용 안함 (집에서 작업)

## Personal Workarounds
- node_modules 손상 시: rm -rf node_modules && pnpm i
- VSCode TS 서버 멈춤 시: Cmd+Shift+P → Restart TS

## TODO (개인용)
- @username 부분 리팩토링 시 함께 검토 부탁
- 새 컴포넌트 라이브러리 평가 중
```

## Speaker Notes

Local Memory는 프로젝트 내 .claude/local.md 파일이며, 보통 .gitignore에 포함시켜 버전 관리에서 제외합니다.
같은 프로젝트라도 개발자마다 다른 내용을 가질 수 있습니다.
로컬 개발 환경의 특수 사정, 개인이 발견한 워크어라운드, 또는 개인적인 TODO나 메모 같은 것을 적습니다.
비밀번호나 실제 API Key 같은 정보는 적지 않는 것이 좋습니다.
