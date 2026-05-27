# Slide 76: Pattern 2 / 이슈 트리아지 설계

**Part 5: 자동화 패턴**

## Code Blocks

### categories

```bash
# 이슈 자동 분류 카테고리 예시
- bug:              버그 보고
- feature-request:  기능 요청
- documentation:    문서 개선
- question:         질문
- security:         보안 관련
- performance:      성능 이슈
- enhancement:      개선 제안
```

## Speaker Notes

Pattern 2 이슈 트리아지 설계입니다.
동작 흐름은 6단계입니다.
새 이슈가 생성되면 내용을 분석하고 카테고리 분류, 우선순위 결정, 담당자 할당 후 Slack에 알림을 보냅니다.
해결하는 문제를 먼저 이해해야 합니다.
하루 수십 개의 이슈가 들어오면 트리아지에만 많은 시간이 듭니다.
AI가 1차 분류와 우선순위를 자동 결정하고 사람은 검토만 합니다.
이슈 자동 분류 카테고리 예시를 봅니다.
bug, feature-request, documentation, question, security, performance, enhancement 7가지 표준 카테고리가 있습니다.
조직에 맞게 추가하거나 조정할 수 있습니다.
특히 security 라벨은 별도 채널로 알림을 보내야 신속한 대응이 가능합니다.
