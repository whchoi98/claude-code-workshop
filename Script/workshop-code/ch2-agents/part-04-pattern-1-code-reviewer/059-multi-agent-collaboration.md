# Slide 59: Multi-agent collaboration

**Part 4: PATTERN 1 / CODE REVIEWER**

## Code Blocks

### multi-agent

```bash
# 시나리오: PR 종합 점검 (4개 에이전트 병렬)

> PR #234를 머지 전에 전반적으로 점검해 주세요.

[메인] 4개 에이전트를 병렬 호출합니다.
       → Task(code-reviewer)      코드 품질
       → Task(security-scanner)   보안 이슈
       → Task(test-coverage)      테스트 부족
       → Task(docs-checker)       문서 동기화 여부

# 결과 종합 (메인이 자동 집계)
## 종합 보고서

### Critical (5건)
- [security] auth.js:42 ...
- [code]     payment.js:88 ...
- ...

### Recommended (8건)
- [test]     ...
- [docs]     ...

### 머지 가능 여부: Critical 해결 후 가능

# 사용자는 단일 명령으로 4관점 보고서 획득
```

## Speaker Notes

Code Reviewer와 다른 에이전트의 협업을 살펴봅니다.
시나리오는 PR 종합 점검입니다.
사용자가 PR을 머지 전에 전반적으로 점검해 달라고 요청합니다.
메인은 4개의 에이전트를 병렬로 호출합니다.
code-reviewer는 코드 품질을 보고, security-scanner는 보안 이슈를, test-coverage는 테스트 부족을, docs-checker는 문서 동기화를 검사합니다.
4개 에이전트가 동시에 실행되어 시간이 최소화됩니다.
메인은 결과를 자동 집계해 종합 보고서를 만듭니다.
Critical 이슈와 Recommended 이슈로 분류합니다.
각 항목에는 발견한 에이전트 유형이 라벨로 표시됩니다.
마지막에 머지 가능 여부를 종합 판단합니다.
Critical을 해결한 후에만 머지 가능하다는 결론을 제시합니다.
사용자는 단일 명령으로 4관점 보고서를 획득할 수 있습니다.
