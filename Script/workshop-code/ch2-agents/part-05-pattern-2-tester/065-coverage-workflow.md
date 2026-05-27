# Slide 65: Coverage workflow

**Part 5: PATTERN 2 / TESTER**

## Code Blocks

### workflow

```bash
# Subagent의 실제 진행 흐름
1. Bash: npm test -- --coverage          → 현재 67% 측정
2. Read: coverage/lcov-report/summary    → 갭 위치 식별
3. Grep: 미커버 함수의 호출 지점 분석     → 입력 패턴 파악
4. Read: 대상 함수 본문                  → 분기와 조건 분석
5. Read: 기존 테스트 (있다면)             → 스타일 학습
6. Write: tests/new.test.js              → 신규 테스트 작성
7. Bash: npm test -- new.test.js         → 실행 통과 확인
   → 실패 시 자동 수정 후 재실행 (최대 2회)
8. Bash: npm test -- --coverage          → 92% 달성 확인
9. Return: 변경 요약 + 커버리지 향상 보고
```

## Speaker Notes

Tester 에이전트의 커버리지 확장 워크플로를 살펴봅니다.
4단계 큰 흐름과 9단계 세부 흐름으로 동작합니다.
1단계는 현재 커버리지 측정입니다.
npm test --coverage 명령으로 현재 상태를 파악합니다.
예시에서는 67%로 나옵니다.
2단계는 갭 위치 식별입니다.
coverage 리포트를 읽어 어느 파일의 어느 함수가 커버되지 않았는지 식별합니다.
3단계는 미커버 함수의 호출 지점 분석입니다.
Grep으로 호출 패턴을 파악합니다.
4단계는 대상 함수의 본문을 읽어 분기와 조건을 분석합니다.
5단계는 기존 테스트 파일이 있다면 스타일을 학습합니다.
6단계는 신규 테스트 파일을 작성합니다.
7단계는 작성한 테스트를 실행해 통과 확인입니다.
실패 시 자동 수정 후 재실행을 최대 2회까지 시도합니다.
8단계는 전체 커버리지를 다시 측정해 92% 달성을 확인합니다.
9단계는 변경 요약과 커버리지 향상 보고를 반환합니다.
