# Slide 124: Glob

**Part 6: CORE CAPABILITIES**

## Code Blocks

### Glob tool

```bash
# Glob 도구 - 파일 경로 패턴 매칭
Glob(pattern: "**/*.test.ts")
# → 모든 *.test.ts 파일 (재귀)

Glob(pattern: "src/**/components/*.tsx")
# → src 아래 components 폴더의 tsx 파일

# 자주 쓰는 패턴
**/*.{js,ts,jsx,tsx}    # JS/TS 전체
src/**/index.ts         # 모든 index.ts
**/*.{test,spec}.*      # 테스트 파일 전체
docs/**/*.md            # 문서 파일
**/!(node_modules)/*    # node_modules 제외

# 활용 패턴
- 마이그레이션 대상 파일 식별
- 테스트 커버리지 범위 계산
- 빌드 산출물 정리
- 파일 명명 규칙 일관성 점검
```

## Speaker Notes

Glob 도구는 파일 경로 패턴 매칭에 특화된 도구입니다.
Grep이 파일 내용을 검색한다면 Glob은 파일명과 경로를 검색합니다.
별표 두 개는 재귀 매칭, 별표 하나는 단일 디렉토리 매칭, 중괄호는 대체 매칭, 물음표는 단일 문자 매칭을 의미합니다.
자주 쓰는 패턴으로 모든 JS와 TS 파일을 찾을 때 중괄호 안에 확장자를 나열하거나, 모든 index 파일, 모든 테스트 파일, 모든 마크다운 문서 등을 패턴으로 표현할 수 있습니다.
활용 시나리오는 마이그레이션 대상 파일 식별, 테스트 커버리지 범위 계산, 빌드 산출물 정리, 파일 명명 규칙 일관성 점검 등이 있습니다.
