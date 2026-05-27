# Slide 26: description field

**Part 2: SUBAGENT 정의 방법**

## Code Blocks

### description

```bash
# 좋은 description (구체적, 작동 시점이 명확)
description: |
  PR diff를 검토하고 가독성, 안전성, 성능 관점에서 개선 사항을 제안.
  사용 시점: 코드 리뷰가 필요하다고 사용자가 명시하거나 git diff 검토 시.

# 나쁜 description (모호함)
description: 코드를 분석하는 도우미

# 더 나쁜 description (너무 광범위)
description: 모든 개발 작업을 도와주는 만능 에이전트
```

## Speaker Notes

description 필드는 자동 디스패치의 핵심입니다.
메인 에이전트가 사용자 요청을 받으면 모든 에이전트의 description을 검토합니다.
그중 가장 적합한 에이전트를 자동 선택합니다.
그래서 description이 모호하면 잘못된 디스패치가 발생합니다.
좋은 description의 특징은 구체적이고 사용 시점이 명확하다는 것입니다.
예시처럼 어떤 작업을 수행하는지, 언제 사용되는지를 함께 기술합니다.
나쁜 description은 너무 모호합니다.
코드를 분석하는 도우미 같은 표현은 어떤 분석인지 알 수 없습니다.
더 나쁜 경우는 너무 광범위한 표현입니다.
모든 개발 작업을 도와주는 만능 에이전트 같은 description은 메인이 항상 이 에이전트를 선택하게 만들어 다른 전문 에이전트의 의미를 없앱니다.
