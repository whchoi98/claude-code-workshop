# Slide 96: Import path migration

**Part 8: PATTERN 5 / MIGRATION BOT**

## Code Blocks

### lodash migration

```python
# 시나리오: 트리 셰이킹을 위해 lodash 전체 import를 lodash-es로 변경

# 변경 전
import _ from 'lodash';
const result = _.debounce(fn, 300);

# 변경 후 (가능한 경우 named import 우선)
import { debounce } from 'lodash-es';
const result = debounce(fn, 300);

# migration-bot의 진행
1. Glob "**/*.{js,ts,tsx}" → 187개 파일
2. Grep "import _ from 'lodash'" → 42개 매칭
3. 각 파일의 _.xxx 사용 추출 → named import로 재작성
4. package.json: lodash → lodash-es 교체
5. 시범 5개 → 빌드 + 테스트 통과
6. 나머지 일괄 진행 → 최종 검증
7. 번들 크기 변화 측정 보고
```

## Speaker Notes

시나리오 2는 import 경로 변경입니다.
트리 셰이킹을 위해 lodash 전체 import를 lodash-es로 변경하는 시나리오입니다.
변경 전후 패턴을 봅니다.
변경 전은 import _ from lodash 형태로 전체를 가져옵니다.
변경 후는 named import로 debounce만 가져와 트리 셰이킹이 가능합니다.
migration-bot의 진행을 봅니다.
1단계 Glob으로 모든 JS, TS, TSX 파일 187개를 스캔합니다.
2단계 Grep으로 lodash import 패턴 42개를 매칭합니다.
3단계 각 파일에서 _.xxx 사용을 추출해 named import로 재작성합니다.
4단계 package.json의 lodash를 lodash-es로 교체합니다.
5단계 시범 5개로 빌드와 테스트 통과를 확인합니다.
6단계 나머지 일괄 진행 후 최종 검증합니다.
7단계 번들 크기 변화를 측정해 보고합니다.
트리 셰이킹 효과를 정량적으로 확인할 수 있습니다.
