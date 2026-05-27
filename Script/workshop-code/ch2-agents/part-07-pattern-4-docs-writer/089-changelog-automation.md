# Slide 89: Changelog automation

**Part 7: PATTERN 4 / DOCS WRITER**

## Code Blocks

### CHANGELOG.md

```bash
# 사용자 요청
"최근 release v2.3.0의 changelog를 작성해 줘"

# docs-writer의 작업
1. Bash git log v2.2.0..v2.3.0 --oneline
2. 커밋 메시지를 카테고리별 분류 (feat, fix, docs, refactor)
3. 사용자 영향 중심으로 재작성
4. CHANGELOG.md에 추가

# 결과: CHANGELOG.md

## [2.3.0] - 2026-05-25

### Added
- 사용자 API에 페이지네이션 지원 (page, limit 쿼리)
- WebSocket 기반 실시간 알림 채널
- Rate limit 헤더 응답 추가

### Fixed
- /users 엔드포인트에서 deleted 사용자 노출 버그
- JWT 토큰 만료 시 401 대신 500 반환 문제

### Changed
- API 응답 형식 통일 (data/errors envelope)
- 최소 Node 버전 18로 상향
```

## Speaker Notes

Changelog 자동 생성을 살펴봅니다.
사용자가 최근 릴리스 v2.3.0의 changelog를 작성해 달라고 요청합니다.
docs-writer의 작업은 4단계로 진행됩니다.
1단계 git log 명령으로 두 태그 사이 커밋을 모두 수집합니다.
2단계 커밋 메시지를 카테고리별로 분류합니다.
feat, fix, docs, refactor 같은 컨벤셔널 커밋 prefix를 활용합니다.
3단계 사용자 영향 중심으로 재작성합니다.
내부 구현 디테일이 아니라 사용자가 알아야 할 변화로 표현합니다.
4단계 CHANGELOG.md에 추가합니다.
결과는 Keep a Changelog 형식을 따릅니다.
Added, Fixed, Changed 같은 표준 섹션으로 정리됩니다.
각 항목은 사용자가 이해할 수 있는 자연어로 기술됩니다.
