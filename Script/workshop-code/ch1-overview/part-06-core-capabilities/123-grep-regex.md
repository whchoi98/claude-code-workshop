# Slide 123: Grep regex

**Part 6: CORE CAPABILITIES**

## Code Blocks

### Regex patterns

```bash
# 자주 쓰는 정규식 패턴

# 1. HTTP 메서드 호출 패턴
Grep(pattern: "(get|post|put|delete)\\(['\"]")
# → axios.get("..."), fetch("..."), etc.

# 2. 환경변수 사용 위치
Grep(pattern: "process\\.env\\.[A-Z_]+")
# → process.env.API_KEY, process.env.DB_HOST

# 3. 비밀 키 패턴 (보안 점검)
Grep(pattern: "(sk-|api[_-]?key|secret)['\"]?[:=]['\"]")
# → 하드코딩된 비밀 발견

# 4. TODO/FIXME 분류
Grep(pattern: "(TODO|FIXME|HACK|XXX):", output_mode: "content")

# 5. 함수 시그니처 검색
Grep(pattern: "^(export\\s+)?async\\s+function\\s+\\w+",
     glob: "*.ts")
```

## Speaker Notes

Grep의 정규식 활용 패턴 몇 가지를 살펴봅니다.
첫째 HTTP 메서드 호출 패턴은 axios get post put delete 함수 호출을 찾을 때 유용합니다.
둘째 환경변수 사용 위치는 process.env 다음에 대문자 변수명 패턴으로 찾습니다.
셋째 비밀 키 패턴은 보안 점검에 매우 중요한데, sk-로 시작하거나 api_key, secret 같은 키워드와 함께 사용되는 하드코딩된 비밀을 찾아냅니다.
넷째 TODO와 FIXME, HACK, XXX 같은 마커를 일괄 분류할 때 사용합니다.
다섯째 함수 시그니처 검색은 export async function 같은 패턴으로 정의 위치를 찾습니다.
JSON 안의 정규식이므로 백슬래시는 두 번 이스케이프해야 한다는 점에 주의하시기 바랍니다.
