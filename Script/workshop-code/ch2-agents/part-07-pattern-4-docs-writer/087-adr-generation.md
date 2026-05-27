# Slide 87: ADR generation

**Part 7: PATTERN 4 / DOCS WRITER**

## Code Blocks

### ADR example

```bash
# 사용자 요청
"PostgreSQL을 MongoDB로 교체한 결정에 대한 ADR을 작성해 줘"

# docs-writer 출력 (docs/adr/0008-mongodb-migration.md)
# ADR 0008: PostgreSQL에서 MongoDB로 전환

Status: Accepted
Date: 2026-05-25
Deciders: 백엔드 팀

## Context
- 사용자 프로필 데이터가 빠르게 진화하는 스키마를 가짐
- PostgreSQL의 alter table 대기 시간이 운영에 영향
- 읽기 부하가 쓰기의 100배 (스케일 아웃 필요)

## Decision
사용자 프로필 도메인만 MongoDB Atlas로 전환.
주문/결제 도메인은 PostgreSQL 유지.

## Consequences
+ 스키마 변경이 마이그레이션 없이 가능
+ 읽기 스케일이 샤딩으로 확장
- 트랜잭션 보장 약화 (보상 트랜잭션 패턴 도입)
- 운영팀이 두 DB 모두 관리
```

## Speaker Notes

ADR, 즉 Architecture Decision Record 작성 예시입니다.
ADR은 중요한 기술 결정을 기록으로 남기는 문서입니다.
예시는 PostgreSQL을 MongoDB로 교체한 결정에 대한 ADR입니다.
파일은 docs/adr 디렉토리에 번호와 함께 저장합니다.
Status, Date, Deciders 같은 메타데이터를 헤더에 명시합니다.
Context 섹션에서 결정에 이른 배경을 설명합니다.
예시처럼 스키마 진화, alter table 지연, 읽기 부하 같은 구체적 이유를 나열합니다.
Decision 섹션에서 실제 결정 내용을 기술합니다.
전부 전환이 아니라 사용자 프로필만 전환하는 식의 정확한 범위 명시가 중요합니다.
Consequences 섹션에서 긍정과 부정 영향을 모두 명시합니다.
트레이드오프를 솔직하게 기록하는 것이 ADR의 가치입니다.
