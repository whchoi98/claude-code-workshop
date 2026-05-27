# Slide 71: CI Integration

**Part 5: PATTERN 2 / TESTER**

## Code Blocks

### CI workflow

```bash
# .github/workflows/auto-test.yml
name: Auto Test Coverage
on:
  pull_request:
    paths: ['src/**']

jobs:
  extend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci && npm test -- --coverage
      
      - name: Extend coverage if low
        if: failure()  # 커버리지 한계 미달 시
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p "test-writer로 PR 변경 함수의 커버리지를 90% 이상으로" \
            --allowed-tools "Read,Edit,Write,Bash(npm test:*)"
      
      - name: Open PR for new tests
        run: gh pr create --title "auto-tests for #${{ github.event.number }}"
```

## Speaker Notes

Tester 에이전트의 CI 통합 예시입니다.
PR마다 자동으로 커버리지를 보강하는 워크플로입니다.
on pull_request 트리거로 src 폴더 변경 시에만 동작합니다.
3단계로 구성됩니다.
1단계는 기존 커버리지 측정입니다.
npm ci와 npm test --coverage를 실행합니다.
2단계는 커버리지가 한계 미달일 때만 실행됩니다.
if failure 조건으로 미달 시에만 발동합니다.
claude -p 명령으로 test-writer 에이전트를 호출해 PR 변경 함수의 커버리지를 90% 이상으로 끌어올립니다.
allowed-tools 플래그로 CI 환경에서 권한을 좁힙니다.
3단계는 신규 테스트를 위한 별도 PR을 자동 생성합니다.
gh CLI로 auto-tests for 원본 PR 번호 형식의 PR을 만듭니다.
원 PR과 별도로 머지할 수 있어 안전합니다.
이런 닫힌 루프 구조가 자동화의 핵심입니다.
