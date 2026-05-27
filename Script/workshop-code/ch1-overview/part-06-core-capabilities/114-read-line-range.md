# Slide 114: Read line range

**Part 6: CORE CAPABILITIES**

## Code Blocks

### Large file workflow

```bash
# 대용량 파일 처리 패턴

# 1. 전체 줄 수 확인 (Bash로)
wc -l src/app.js
# → 5234

# 2. 단계별 읽기 (Claude가 자동 수행)
Read(file_path: "src/app.js", offset: 1, limit: 100)
# → 헤더, import, 전역 변수 확인

Read(file_path: "src/app.js", offset: 1500, limit: 200)
# → 특정 함수 영역 정밀 분석

# 3. Grep과 조합 (가장 효율적)
Grep(pattern: "function processPayment", path: "src/")
# → src/app.js:1234
Read(file_path: "src/app.js", offset: 1230, limit: 80)
```

## Speaker Notes

대용량 파일을 다루는 패턴입니다.
수천 줄짜리 파일 전체를 한 번에 읽으면 컨텍스트를 낭비하게 됩니다.
Claude는 이를 피하기 위해 다음 패턴을 자동으로 사용합니다.
1단계 wc -l 명령으로 전체 줄 수를 확인합니다.
2단계 헤더 영역을 먼저 읽어 파일의 구조를 파악하고 필요한 영역만 정밀하게 읽습니다.
3단계 Grep으로 특정 함수나 패턴의 위치를 찾고, 그 위치 주변만 Read합니다.
이 패턴은 토큰 비용을 크게 절약하면서도 정확한 분석을 가능하게 해 줍니다.
사용자는 명시적으로 이렇게 지시하지 않아도 Claude가 알아서 효율적으로 작업합니다.
