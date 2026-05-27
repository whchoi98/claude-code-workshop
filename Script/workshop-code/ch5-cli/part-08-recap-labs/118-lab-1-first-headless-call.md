# Slide 118: Lab 1 / 첫 Headless 호출

**Part 8: RECAP & 4 LABS**

## Code Blocks

### Lab 1

```bash
# 1. 단순 호출
$ claude -p "Python에서 리스트와 튜플의 차이를 3줄로"
# 결과: 마크다운 텍스트

# 2. JSON 출력
$ claude -p "Python 리스트와 튜플 비교" \
    --output-format json | jq .

# 3. result만 추출
$ claude -p "..." --output-format json | jq -r '.result'

# 4. 토큰 사용량 확인
$ claude -p "..." --output-format json | \
    jq '.usage | "in=\(.input_tokens) out=\(.output_tokens)"'

# 5. 파일로 저장
$ claude -p "README 초안 작성" \
    --output-format json | jq -r '.result' > README.md

# 6. pipe 입력
$ cat package.json | claude -p "이 의존성 보안 검토"

# 7. 환경변수 활용
$ MODEL=claude-haiku-4-5 claude -p "..." --model "$MODEL"

# 8. 다단계 (세션 재사용)
$ S=$(claude -p "Python 정렬 알고리즘 5가지" \
      --output-format json | jq -r '.session_id')
$ claude --continue "$S" -p "그 중 가장 빠른 2개의 코드"

# 9. doctor로 환경 확인
$ claude doctor

# 10. 도움말 탐색
$ claude --help
$ claude doctor --help
```

## Speaker Notes

Lab 1은 첫 Headless 호출 실습입니다.
약 20분 소요됩니다.
10가지 기본 패턴을 차례로 실행해 봅니다.
1번 단순 호출로 -p 옵션 사용법을 익힙니다.
2번 JSON 출력으로 구조화 응답을 확인합니다.
3번 result만 추출하는 jq 활용법을 익힙니다.
4번 토큰 사용량 확인으로 비용 의식을 키웁니다.
5번 파일로 저장하는 redirect 패턴입니다.
6번 pipe 입력으로 다른 명령의 결과를 분석합니다.
7번 환경변수로 모델을 동적 지정합니다.
8번 다단계 세션으로 session_id를 활용한 연속 작업을 해 봅니다.
9번 doctor로 환경을 확인합니다.
10번 도움말 탐색으로 새 옵션을 발견하는 습관을 들입니다.
이 10가지 패턴이 Headless 사용의 기본기입니다.
본인 환경에서 직접 실행하면서 출력을 확인하시기 바랍니다.
