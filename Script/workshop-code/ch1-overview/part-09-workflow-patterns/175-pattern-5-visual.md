# Slide 175: Pattern 5 Visual

**Part 9: WORKFLOW PATTERNS**

## Code Blocks

### VISUAL

```bash
# 1. 디자인 시안 → 코드
$ claude
> [이미지 첨부: figma-design.png]
> 이 디자인을 React 컴포넌트로 구현해 주세요.

Claude:
  ✓ Read figma-design.png (이미지 분석)
  ✓ 색상, 레이아웃, 타이포그래피 추출
  ✓ Write src/components/PricingCard.tsx
  ✓ Write src/components/PricingCard.module.css

# 2. 버그 스크린샷 → 수정
$ claude
> [이미지 첨부: bug-screenshot.png]
> 이 UI에서 버튼이 잘려 보입니다. 원인을 찾고 수정해 주세요.

Claude:
  ✓ Read bug-screenshot.png
  ✓ 잘린 영역 식별 (overflow 추정)
  ✓ Grep 관련 컴포넌트 검색 → Read → Edit
```

## Speaker Notes

Pattern 5 Visual Workflow는 이미지를 입력으로 활용하는 패턴입니다.
Claude의 멀티모달 능력을 활용해 두 가지 시나리오가 가능합니다.
첫째 디자인 시안을 첨부하고 React 컴포넌트로 구현해 달라고 요청하면, Claude가 이미지에서 색상, 레이아웃, 타이포그래피를 추출해 코드와 CSS를 만들어 줍니다.
둘째 버그 스크린샷을 첨부하고 원인 분석을 요청하면, Claude가 잘린 영역을 식별하고 overflow 같은 가능한 원인을 추정해 관련 컴포넌트를 찾아 수정합니다.
UI 작업에서 매우 강력한 패턴입니다.
