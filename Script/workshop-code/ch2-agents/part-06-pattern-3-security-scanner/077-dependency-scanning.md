# Slide 77: Dependency scanning

**Part 6: PATTERN 3 / SECURITY SCANNER**

## Code Blocks

### dependency scan

```bash
# 에이전트가 사용하는 표준 도구들

# JavaScript/TypeScript
npm audit --json
yarn audit --json
pnpm audit --json

# Python
pip-audit --format json
safety check --json

# Ruby
bundle audit check --update

# Go
govulncheck ./...

# 에이전트가 결과를 통합 분석
- 같은 CVE라도 컨텍스트별 영향도 평가
- 직접 사용 vs 간접 의존성 구분
- 패치 경로 제안 (직접 업데이트 vs 우회)
- 패치 불가 시 mitigation 제안
```

## Speaker Notes

의존성 스캐닝을 자세히 살펴봅니다.
에이전트는 언어별 표준 도구를 활용합니다.
JavaScript와 TypeScript는 npm audit, yarn audit, pnpm audit을 사용합니다.
Python은 pip-audit와 safety check를 사용합니다.
Ruby는 bundle audit, Go는 govulncheck를 사용합니다.
모두 JSON 출력을 활용해 후처리를 쉽게 합니다.
에이전트는 결과를 단순 보고하지 않고 통합 분석을 수행합니다.
첫째, 같은 CVE라도 컨텍스트별 영향도를 평가합니다.
취약한 함수를 실제로 사용하는지 코드를 확인합니다.
둘째, 직접 사용과 간접 의존성을 구분합니다.
간접은 우선순위가 낮을 수 있습니다.
셋째, 패치 경로를 제안합니다.
직접 업데이트가 가능한지, 우회가 필요한지를 판단합니다.
넷째, 패치 불가 시 mitigation을 제안합니다.
취약 함수 사용 회피, 입력 검증 강화 같은 우회책입니다.
