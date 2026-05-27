# Slide 99: 시나리오 1 디버깅 (문제 정의)

**Part 5: QUICK START**

## Code Blocks

### 문제 정의

```bash
# 첫 메시지 - 맥락과 증상을 정확히 전달
> 운영에서 다음 에러가 발생합니다. 원인 추적과 수정 부탁드립니다.

  Error: Cannot read property 'preferences' of null
    at UserProfile.render (src/pages/user/profile.tsx:78)
    at processChild (next/dist/...)

영향: 사용자 약 5% (전체 1만명 중 500명)
재현: profile 페이지에서 일부 사용자만 발생

문맥:
- 어제 user 모델에 'preferences' jsonb 컬럼 추가
- 기존 사용자에 대한 마이그레이션은 미수행
- 이 컬럼이 null인 사용자들에서 발생할 가능성
```

## Speaker Notes

첫 번째 시나리오는 디버깅입니다.
우선 문제를 정확히 정의하는 것이 가장 중요합니다.
운영 환경에서 사용자 프로필 페이지가 500 에러를 일부 사용자에게만 반환하는 상황을 가정합니다.
첫 메시지에서는 4가지를 포함합니다.
첫째 스택 트레이스를 그대로 전달, 둘째 영향 범위를 구체적 숫자로 명시, 셋째 최근 변경사항 같은 컨텍스트, 넷째 가능한 가설을 함께 제공합니다.
이 정도 정보가 있으면 Claude가 헛된 추측 없이 효율적으로 원인 추적을 시작할 수 있습니다.
