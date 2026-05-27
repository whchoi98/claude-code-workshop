# Slide 104: Versioning and updates

**Part 6: MCP 사내 서버 구축**

## Code Blocks

### versioning

```bash
# Semantic Versioning (SemVer)
# MAJOR.MINOR.PATCH
# - MAJOR: 호환 불가능한 변경 (도구 제거, 시그니처 변경)
# - MINOR: 호환 가능한 기능 추가 (새 도구)
# - PATCH: 버그 수정, 내부 개선

# 호환 가능한 변경 (MINOR/PATCH)
# 새 도구 추가
- get_employee
+ get_employee
+ list_employees    # 새 도구 (사용자 기존 코드 영향 없음)

# 도구에 optional 인자 추가
get_employee(employee_id)
get_employee(employee_id, include_history=false)  # default 있으면 OK

# 호환 불가능 변경 (MAJOR)
# 도구 시그니처 변경 - 이전 사용자 깨짐
get_employee(employee_id)  →  get_employee_v2(emp_uuid)

# 변경 전략
1. 새 도구를 _v2 suffix로 추가 (기존 유지)
2. 일정 기간 두 버전 모두 제공 (deprecation 안내)
3. 사용자 마이그레이션 완료 후 구버전 제거 (다음 major)

# Changelog 유지
## [1.2.0] - 2026-05-25
### Added
- list_employees 도구 추가
### Changed
- get_employee 응답에 department 필드 추가
```

## Speaker Notes

버전 관리와 업데이트 전략을 살펴봅니다.
Semantic Versioning을 따릅니다.
MAJOR는 호환 불가능한 변경, MINOR는 호환 가능한 기능 추가, PATCH는 버그 수정입니다.
호환 가능한 변경 예시를 봅니다.
새 도구를 추가하면 기존 사용자에게 영향이 없습니다.
도구에 default 값이 있는 optional 인자를 추가해도 OK입니다.
호환 불가능 변경은 주의가 필요합니다.
도구 시그니처를 변경하면 기존 사용자가 깨집니다.
employee_id를 emp_uuid로 바꾸는 식의 변경은 MAJOR 버전 변경입니다.
변경 전략은 3단계로 진행합니다.
1단계 새 도구를 _v2 suffix로 추가해 기존을 유지합니다.
2단계 일정 기간 두 버전을 모두 제공하며 deprecation을 안내합니다.
3단계 사용자 마이그레이션 완료 후 다음 major 버전에서 구버전을 제거합니다.
Changelog는 Keep a Changelog 형식으로 유지합니다.
Added, Changed, Removed 섹션으로 변경을 명확히 기록합니다.
