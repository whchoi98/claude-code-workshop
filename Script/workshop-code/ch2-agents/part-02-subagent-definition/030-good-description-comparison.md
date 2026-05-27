# Slide 30: Good description comparison

**Part 2: SUBAGENT 정의 방법**

## Code Blocks

### comparison

```bash
# 시나리오: 사용자가 "이 PR의 보안 이슈를 점검해 줘" 요청

# ❌ 모호한 description (잘못된 디스패치 위험)
agent A:  description: 코드 관련 분석을 수행합니다.
agent B:  description: 코드 검사를 도와줍니다.
→ 메인이 어떤 걸 골라야 할지 모름

# ✅ 명확한 description
agent A:  description: |
  PR diff를 가독성, 명명 규칙, 잠재 버그 관점에서 검토.
  사용 시점: 일반 코드 리뷰가 필요한 경우.
  
agent B:  description: |
  코드와 의존성을 보안 취약점(injection, XSS, secrets) 관점에서 분석.
  사용 시점: 보안 이슈 점검이 필요한 경우.
→ 메인이 보안 키워드를 보고 agent B를 정확히 선택
```

## Speaker Notes

description 작성 비교 예시입니다.
사용자가 이 PR의 보안 이슈를 점검해 달라고 요청한 상황을 가정합니다.
모호한 description의 경우를 봅니다.
agent A의 description은 코드 관련 분석을 수행한다는 정도입니다.
agent B는 코드 검사를 도와준다는 정도입니다.
둘 다 너무 광범위해 메인이 어떤 걸 골라야 할지 모릅니다.
명확한 description의 경우를 봅니다.
agent A는 PR diff를 가독성, 명명 규칙, 잠재 버그 관점에서 검토한다고 구체화합니다.
agent B는 보안 취약점, injection, XSS, secrets 관점에서 분석한다고 명시합니다.
사용 시점까지 함께 기술합니다.
이렇게 작성하면 메인이 사용자 요청의 보안이라는 키워드를 보고 정확히 agent B를 선택합니다.
