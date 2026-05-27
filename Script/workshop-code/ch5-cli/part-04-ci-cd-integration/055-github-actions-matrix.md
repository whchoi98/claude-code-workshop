# Slide 55: GitHub Actions / Matrix 빌드

**Part 4: CI/CD 통합**

## Code Blocks

### matrix

```bash
# .github/workflows/multi-analysis.yml
name: Multi-dimension Analysis

on: [push]

jobs:
  analyze:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        dimension: [security, performance, accessibility, seo]
        node: [18, 20]
        include:
          - dimension: security
            prompt-file: prompts/security.md
            allowed-tools: "Read,Grep,Glob"
          - dimension: performance
            prompt-file: prompts/performance.md
            allowed-tools: "Read,Grep,Bash(npm run benchmark)"

    name: ${{ matrix.dimension }}-node${{ matrix.node }}

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
      - run: npm install -g @anthropic-ai/claude-code

      - name: Run analysis
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p "$(cat ${{ matrix.prompt-file }})" \
            --allowed-tools "${{ matrix.allowed-tools }}" \
            --output-format json > result.json

      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: ${{ matrix.dimension }}-node${{ matrix.node }}
          path: result.json

  aggregate:
    needs: analyze
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
      - run: ls -la
        # 모든 차원의 결과 통합 처리
```

## Speaker Notes

GitHub Actions Matrix 빌드 패턴입니다.
여러 차원을 병렬 실행할 때 사용합니다.
strategy 블록에 matrix를 정의합니다.
dimension 4개와 node 2개의 조합으로 8개 job이 동시 실행됩니다.
fail-fast를 false로 두면 하나가 실패해도 나머지는 계속 실행됩니다.
include로 각 dimension별 추가 변수를 정의할 수 있습니다.
security는 보안 프롬프트와 좁은 권한, performance는 성능 프롬프트와 벤치마크 허용처럼 차별화합니다.
name을 동적으로 만들어 UI에서 식별이 쉽게 합니다.
각 job은 자신의 dimension에 맞는 프롬프트와 권한으로 claude를 호출합니다.
upload-artifact로 결과를 저장합니다.
aggregate job은 needs로 모든 analyze job을 기다린 후 download-artifact로 모든 결과를 가져와 통합 처리합니다.
복잡한 다차원 분석을 자동화할 때 매우 유용한 패턴입니다.
