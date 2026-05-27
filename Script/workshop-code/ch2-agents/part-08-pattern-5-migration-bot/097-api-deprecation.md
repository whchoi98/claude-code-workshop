# Slide 97: API deprecation

**Part 8: PATTERN 5 / MIGRATION BOT**

## Code Blocks

### fetch transition

```typescript
# 시나리오: node-fetch 외부 라이브러리 제거, Node 내장 fetch로 전환

# 변경 전
const fetch = require('node-fetch');
const res = await fetch(url);
const data = await res.json();

# 변경 후 (Node 18+ 내장 fetch)
// require 제거, 내장 fetch 사용
const res = await fetch(url);
const data = await res.json();

# migration-bot의 차이점 처리
- node-fetch v2: cjs, AbortController 폴리필 필요
- 내장 fetch:    cjs/esm, AbortController 내장
- 일부 옵션 비호환:
  - agent → undici Agent (별도 처리 필요)
  - timeout → AbortSignal.timeout()로 대체

# 작업
1. node-fetch require 제거 (88개 파일)
2. 옵션 호환성 매핑 적용
3. .nvmrc 확인 → Node 18+ 보장
4. 테스트 + 통합 테스트 통과 확인
```

## Speaker Notes

시나리오 3은 Deprecated API 교체입니다.
node-fetch 외부 라이브러리를 제거하고 Node 내장 fetch로 전환하는 시나리오입니다.
변경 전은 node-fetch를 require해서 사용합니다.
변경 후는 require를 제거하고 Node 18 이상의 내장 fetch를 사용합니다.
migration-bot이 처리해야 할 차이점이 있습니다.
node-fetch v2는 CommonJS이며 AbortController 폴리필이 필요합니다.
내장 fetch는 CommonJS와 ESM 모두 지원하며 AbortController가 내장입니다.
일부 옵션이 비호환입니다.
agent 옵션은 undici Agent로 별도 처리가 필요합니다.
timeout 옵션은 AbortSignal.timeout으로 대체합니다.
작업은 88개 파일에서 node-fetch require를 제거하고 옵션 호환성을 매핑합니다.
.nvmrc로 Node 18 이상을 보장하고 테스트와 통합 테스트 통과를 확인합니다.
