# Slide 113: Read multimodal

**Part 6: CORE CAPABILITIES**

## Code Blocks

### examples

```bash
# 사용 예시
User: design.png을 보고 React 컴포넌트로 구현해 주세요.
Claude: [Read(design.png) → 이미지 분석] → 컴포넌트 생성

User: spec.pdf의 3페이지 요구사항을 코드로 옮겨 주세요.
Claude: [Read(spec.pdf) → PDF 읽기] → 해당 페이지 분석 → 구현
```

## Speaker Notes

Read 도구는 텍스트 파일뿐만 아니라 멀티모달 입력도 지원합니다.
PNG, JPG, GIF, WebP 같은 이미지 파일을 직접 인식해 UI 스크린샷의 텍스트와 레이아웃을 분석할 수 있습니다.
PDF 문서도 텍스트와 페이지 레이아웃을 동시에 분석할 수 있어 사양서나 설계서 분석에 적합합니다.
Jupyter 노트북 .ipynb 파일은 셀 단위로 코드와 출력을 모두 인식해 ML 워크플로 통합이 가능합니다.
화면 예시처럼 사용자가 design.png를 React 컴포넌트로 만들어 달라거나 spec.pdf의 특정 페이지를 코드로 옮겨 달라고 요청하면 Claude가 직접 파일을 분석해 작업을 수행합니다.
