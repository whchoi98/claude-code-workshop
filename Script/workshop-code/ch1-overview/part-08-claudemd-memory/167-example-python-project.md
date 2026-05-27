# Slide 167: Example - Python Project

**Part 8: CLAUDE.md & MEMORY**

## Code Blocks

### Python project example

```bash
# Project: order-service

## Stack
- Python 3.12 / Django 5.0 / DRF
- PostgreSQL 16 / Celery + Redis
- pytest + pytest-django

## Commands
- 개발: python manage.py runserver
- 마이그레이션: python manage.py migrate
- 새 마이그레이션: python manage.py makemigrations
- 테스트: pytest -x --cov=src
- 린트: ruff check . && mypy src/

## Conventions
- Type hints 필수 (모든 함수/메서드)
- async View 사용 금지 (sync 만)
- 트랜잭션: @transaction.atomic 데코레이터 활용
- 비즈니스 로직은 service 레이어로 분리

## Don't
- DB에 직접 SQL 실행 X (Django ORM 사용)
- requirements.txt 직접 수정 X (poetry add 사용)
```

## Speaker Notes

실전 예시로 Python Django 프로젝트의 CLAUDE.md를 보여드립니다.
Stack 섹션에 사용 기술과 버전을 명시합니다.
Commands 섹션에는 그대로 복사 실행 가능한 명령을 적습니다.
Conventions에서는 Type hints 필수, async View 금지 같은 구체적 컨벤션을 명시합니다.
Dont 섹션에서는 DB 직접 SQL 금지 같은 명확한 금지 사항을 적습니다.
식으로 작성하면 Claude가 첫 메시지부터 정확한 컨텍스트로 작업을 시작할 수 있습니다.
