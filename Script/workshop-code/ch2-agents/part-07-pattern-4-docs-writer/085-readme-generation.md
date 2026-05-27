# Slide 85: README generation

**Part 7: PATTERN 4 / DOCS WRITER**

## Code Blocks

### README example

```typescript
# 사용자 요청
"이 프로젝트의 README를 작성해 줘"

# docs-writer의 작업 흐름
1. Read package.json → 프로젝트명, 의존성, 스크립트 파악
2. Read src/index.js → 진입점과 주요 함수 파악
3. Glob examples/**/*.js → 예시 코드 수집
4. Bash git log --oneline -10 → 최근 변경 동향
5. Write README.md (다음 구조로):

# Project Name
한 문장 설명.

## Installation
```
npm install
```

## Usage
```js
const lib = require('./src');
lib.start({ port: 3000 });
```

## Examples
examples/ 디렉토리 참고.

## License
MIT
```

## Speaker Notes

README 자동 생성 예시를 봅니다.
사용자가 이 프로젝트의 README를 작성해 달라고 요청한 상황입니다.
docs-writer의 작업 흐름은 5단계로 진행됩니다.
1단계 package.json을 읽어 프로젝트명과 의존성, 스크립트를 파악합니다.
2단계 src/index.js 같은 진입점을 읽어 주요 함수와 사용법을 파악합니다.
3단계 examples 디렉토리의 예시 코드를 수집합니다.
4단계 git log로 최근 변경 동향을 파악합니다.
5단계 README.md를 표준 섹션 구조로 작성합니다.
섹션 구조는 Project Name 한 줄 설명부터 Installation, Usage, Examples, License 순입니다.
예시는 examples 디렉토리 참고로 안내하며 실제 실행 가능한 형태로 작성합니다.
자동 탐색과 구조화된 출력이 핵심입니다.
