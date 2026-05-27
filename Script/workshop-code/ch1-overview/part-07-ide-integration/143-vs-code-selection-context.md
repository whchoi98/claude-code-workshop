# Slide 143: VS Code selection context

**Part 7: IDE INTEGRATION**

## Code Blocks

### Selection workflow

```bash
# 선택 영역 전달 워크플로

1. 편집기에서 코드 블록 선택 (드래그 or Shift+화살표)
2. 우클릭 → "Ask Claude about this code"
   또는 Cmd/Ctrl+Shift+P → "Send Current Selection"
3. 사이드바에 자연스럽게 컨텍스트 추가됨
4. 자연어 질문 입력

# 활용 예시
[선택: function processPayment() { ... }]
User: 이 함수의 에러 처리를 개선해 주세요.

# 또는 다중 영역
1. Cmd/Ctrl+Click로 여러 영역 선택
2. 모두 한 번에 컨텍스트로 전달
3. 함수 사이의 관계 분석 등 다중 영역 작업 가능

# 단축키
- Shift+Alt+M: 선택 영역 + 자연어 질문 (한 번에)
- Cmd+I: 선택 영역 인라인 편집 요청
```

## Speaker Notes

선택 영역 컨텍스트 활용은 IDE 통합의 가장 강력한 기능 중 하나입니다.
1단계 편집기에서 코드 블록을 드래그나 Shift 화살표로 선택합니다.
2단계 우클릭 메뉴에서 Ask Claude about this code를 선택하거나 명령 팔레트에서 Send Current Selection을 사용합니다.
3단계 사이드바에 선택 영역이 컨텍스트로 자동 추가됩니다.
4단계 자연어 질문을 입력합니다.
다중 영역도 가능한데, Cmd Ctrl Click로 여러 영역을 선택한 후 한 번에 전달하면 함수 사이의 관계 분석 같은 다중 영역 작업이 가능합니다.
단축키 Shift Alt M은 선택 영역과 질문을 한 번에 전달하고, Cmd I는 선택 영역의 인라인 편집을 요청합니다.
