# Slide 41: Parallel example

**Part 3: TASK 도구와 디스패치**

## Code Blocks

### Parallel call

```bash
# 사용자 요청
> 이 PR을 전반적으로 점검해 줘. 리뷰, 보안, 테스트 추가까지.

# 메인의 응답 (3개 Task를 한 번에 발행)
Task(subagent_type="code-reviewer",     prompt="...PR diff...")
Task(subagent_type="security-scanner",  prompt="...PR files...")
Task(subagent_type="test-writer",       prompt="...changed funcs...")

# 실행 (병렬)
  code-reviewer:    45초 → 8개 이슈 발견
  security-scanner: 60초 → 2개 high severity 발견
  test-writer:      50초 → 4개 테스트 추가

총 소요 시간: max(45, 60, 50) = 60초

# 메인이 3개 결과를 통합해 사용자에게 보고
"전체 검토 완료: 코드 이슈 8건, 보안 이슈 2건, 신규 테스트 4개."
```

## Speaker Notes

병렬 호출의 구체적 예시를 보겠습니다.
사용자가 이 PR을 전반적으로 점검해 달라고 요청합니다.
리뷰, 보안, 테스트 추가까지 한 번에 부탁한 상황입니다.
메인은 3개의 Task 호출을 한 번에 발행합니다.
code-reviewer, security-scanner, test-writer를 모두 호출합니다.
각 Subagent는 독립적으로 병렬 실행됩니다.
code-reviewer는 45초 만에 8개 이슈를 발견합니다.
security-scanner는 60초 만에 2개의 high severity 이슈를 발견합니다.
test-writer는 50초 만에 4개의 테스트를 추가합니다.
총 소요 시간은 가장 오래 걸린 60초입니다.
직렬이었다면 155초가 걸렸을 것입니다.
61퍼센트의 시간 절감입니다.
메인은 3개의 결과를 통합해 사용자에게 한 번에 보고합니다.
