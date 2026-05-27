# Slide 122: Grep basics

**Part 6: CORE CAPABILITIES**

## Code Blocks

### Grep tool

```bash
# Grep 도구 - ripgrep 기반
Grep(
  pattern: "function processPayment",
  path: "src/",           # 검색 디렉토리
  glob: "*.ts",           # 파일 필터 (선택)
  type: "ts",             # 또는 언어 타입
  output_mode: "files_with_matches",  # 기본
  -i: true,               # 대소문자 무시
  -n: true,               # 라인 번호 표시
  -A: 3, -B: 2,           # 매칭 앞뒤 라인 포함
)

# 출력 모드
- files_with_matches: 매칭된 파일만
- content: 매칭된 라인 내용
- count: 매칭 개수

# 활용 예시
- 함수/변수 정의 위치 찾기
- TODO/FIXME 일괄 수집
- 사용 위치(callsite) 분석
```

## Speaker Notes

Grep 도구는 ripgrep 기반의 빠른 패턴 검색 도구입니다.
pattern에 검색할 정규식, path에 검색 디렉토리를 지정합니다.
glob 옵션으로 파일 패턴 필터링, type 옵션으로 언어 타입 필터링이 가능합니다.
output_mode는 세 가지인데, files_with_matches는 매칭된 파일 목록만, content는 매칭된 라인 내용을, count는 매칭 개수를 반환합니다.
-i 대소문자 무시, -n 라인 번호 표시, -A와 -B는 매칭 앞뒤 라인 포함 등 ripgrep 옵션을 그대로 사용할 수 있습니다.
활용 예시는 함수나 변수의 정의 위치 찾기, TODO와 FIXME 일괄 수집, 사용 위치 분석 같은 시나리오입니다.
ripgrep은 .gitignore를 자동 인식하므로 node_modules 같은 폴더가 자동으로 제외되어 빠릅니다.
