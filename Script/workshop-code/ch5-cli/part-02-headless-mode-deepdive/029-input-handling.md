# Slide 29: 큰 입력 처리

**Part 2: HEADLESS 모드 심화**

## Code Blocks

### large input

```bash
# 문제: 컨텍스트 윈도우는 약 200K 토큰
# 대용량 파일/디렉토리는 한 번에 안 들어감

# 전략 1: split으로 분할
$ split -l 1000 large.log chunk_
$ for f in chunk_*; do
    claude -p "이 청크 요약" < "$f" >> summary.md
  done
$ # 마지막에 모든 요약을 종합
$ claude -p "$(cat summary.md) 통합 결론" > final.md

# 전략 2: Subagent에 위임
$ claude -p "다음 디렉토리 전체를 분석. 큰 파일은 \
    Subagent에게 위임하고 결과만 받아 종합 보고서 작성. \
    대상: ./src"

# 전략 3: tail/head로 부분만
$ tail -5000 huge.log | claude -p "최근 패턴 분석"
$ head -100 huge.csv | claude -p "이 CSV 스키마 추론"

# 전략 4: 사전 처리 (압축/요약)
$ grep ERROR huge.log | claude -p "에러 패턴 분류"
$ # 1GB 로그 → 10MB 에러만 → claude 입력 가능

# 전략 5: 점진적 처리 (세션 재사용)
$ S=$(claude -p "디렉토리 구조 파악" --output-format json \
      | jq -r '.session_id')
$ claude --continue "$S" -p "이제 src/ 하위 자세히"
$ claude --continue "$S" -p "이제 tests/ 검토"

# 전략 6: 코드 검색으로 좁히기
$ grep -rn "function handlePayment" src/ | \
    claude -p "이 함수의 호출 패턴 분석"
```

## Speaker Notes

큰 입력 처리 6가지 전략입니다.
컨텍스트 윈도우는 약 200K 토큰으로 매우 큰 파일은 한 번에 들어가지 않습니다.
전략 1은 split으로 분할입니다.
파일을 1000줄씩 청크로 나누고 각각 요약한 후 종합합니다.
전략 2는 Subagent 위임입니다.
Claude에게 큰 파일은 Subagent에게 위임하라고 명시하면 자동으로 분할 처리합니다.
전략 3은 tail이나 head로 부분만 처리합니다.
로그는 최근만, CSV는 헤더만으로 충분한 경우가 많습니다.
전략 4는 사전 처리입니다.
grep으로 ERROR 라인만 추출하면 1GB 로그도 10MB로 줄어듭니다.
전략 5는 점진적 처리입니다.
같은 세션을 유지하며 단계별로 다른 부분을 분석합니다.
전략 6은 코드 검색으로 좁히기입니다.
grep으로 관심 패턴이 있는 위치만 찾아 그 컨텍스트만 분석합니다.
실무에서는 이 전략들을 조합해 사용합니다.
