# Slide 116: Edit Multi-file

**Part 6: CORE CAPABILITIES**

## Code Blocks

### Multi-file refactor

```python
# Claude는 여러 파일을 순차적으로 또는 병렬로 수정 가능

User: 모든 컴포넌트의 default export를 named export로 바꿔 주세요.

Claude:
  1. Grep "export default" → 23개 파일 식별
  2. Read 각 파일 → 컴포넌트 이름 확인
  3. Edit 각 파일 (병렬 실행 가능)
       - export default Button  → export { Button }
       - export default Card    → export { Card }
       - ...
  4. Grep "import .* from" → 호출자 47곳 식별
  5. Edit 47개 import 문 수정
       - import Button from  → import { Button } from
  6. Bash npm run lint && npm test
```

## Speaker Notes

Edit 도구는 여러 파일을 순차적으로 또는 병렬로 수정할 수 있습니다.
화면 예시는 모든 컴포넌트의 default export를 named export로 바꾸는 리팩토링입니다.
1단계 Grep으로 영향 파일을 식별하고, 2단계 각 파일을 Read하여 정확한 컴포넌트 이름을 파악합니다.
3단계 각 파일에 Edit을 적용합니다.
이 단계는 병렬 실행이 가능합니다.
4단계 호출자도 함께 식별하고 5단계 import 문을 수정합니다.
마지막 6단계 lint와 test를 자동 실행해 회귀가 없는지 확인합니다.
각 Edit은 원자적이므로 일부 파일만 수정되는 중간 상태가 발생하지 않습니다.
