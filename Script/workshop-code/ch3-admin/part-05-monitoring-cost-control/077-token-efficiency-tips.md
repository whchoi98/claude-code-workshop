# Slide 77: Token efficiency tips

**Part 5: MONITORING & COST CONTROL**

## Code Blocks

### Token tips

```bash
# 1. CLAUDE.md를 간결하게
# ❌ 길고 모호한 설명
"## Architecture
This project follows clean architecture principles with
domain layer, application layer, and infrastructure layer..."  # 500+ tokens

# ✅ 핵심만 간결하게
"## Architecture
3-layer: domain (src/domain), app (src/app), infra (src/infra)"  # 30 tokens

# 2. 큰 파일은 부분 읽기
# ❌ 전체 파일 읽고 분석 (10K tokens)
Read("src/giant-file.ts")

# ✅ 필요한 부분만
Read("src/giant-file.ts", { offset: 100, limit: 50 })

# 3. Grep으로 미리 좁히기
# 먼저 Grep으로 관련 코드 위치 파악 (적은 토큰)
# 그 후 해당 파일/라인만 Read

# 4. Subagent로 큰 분석 위임
# 큰 분석을 메인이 직접 하면 컨텍스트 폭발
# Subagent에 위임하면 결과만 받음 (90%+ 절감)

# 5. 출력 형식 명시
# JSON 스키마를 미리 지시하여 불필요한 설명 제거
```

## Speaker Notes

토큰 효율성을 높이는 실용적 팁입니다.
작은 변화가 큰 효과를 가져옵니다.
첫째, CLAUDE.md를 간결하게 작성합니다.
길고 모호한 설명 대신 핵심만 간결하게 작성하면 500토큰이 30토큰으로 줄어듭니다.
둘째, 큰 파일은 부분 읽기를 합니다.
Read 도구에 offset과 limit 옵션으로 필요한 부분만 읽습니다.
셋째, Grep으로 미리 좁힙니다.
먼저 Grep으로 관련 코드 위치를 파악한 후 해당 파일과 라인만 Read합니다.
넷째, Subagent로 큰 분석을 위임합니다.
큰 분석을 메인이 직접 하면 컨텍스트 폭발이 일어납니다.
Subagent에 위임하면 결과만 받으므로 90퍼센트 이상 절감됩니다.
다섯째, 출력 형식을 명시합니다.
JSON 스키마를 미리 지시하여 불필요한 설명을 제거합니다.
이 다섯 가지를 적용하면 일상 사용 비용이 크게 줄어듭니다.
