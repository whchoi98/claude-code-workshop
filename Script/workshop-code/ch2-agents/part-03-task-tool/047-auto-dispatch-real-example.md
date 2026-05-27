# Slide 47: Auto dispatch real example

**Part 3: TASK 도구와 디스패치**

## Code Blocks

### auto dispatch demo

```
> 어제 머지된 PR #234의 보안과 테스트를 한 번에 점검해 줘.

[메인] 보안과 테스트를 동시에 점검하겠습니다.
       2개의 Subagent를 병렬로 호출합니다.

       → Task(security-scanner, "PR #234 diff and dependencies")
       → Task(test-writer, "PR #234 changed functions coverage")

[보안 ] 분석 중... 의존성 3개에 알려진 CVE 발견. 자세히 확인 중.

[테스트] 분석 중... 변경된 5개 함수 중 2개가 테스트 누락.

[메인]   결과 종합:
         보안: 의존성 3건 (CVE-2024-1234 등). 패치 권장.
         테스트: 누락 2건. 추가 작성 가능. 진행하시겠어요?

> 네, 진행해 주세요.
```

## Speaker Notes

자동 디스패치의 실전 대화 예시를 살펴봅니다.
사용자가 어제 머지된 PR #234의 보안과 테스트를 한 번에 점검해 달라고 요청합니다.
메인은 보안과 테스트라는 두 가지 키워드를 인식합니다.
2개의 Subagent를 병렬로 호출하는 것이 효율적이라고 판단합니다.
security-scanner와 test-writer를 동시에 Task 도구로 호출합니다.
사용자에게는 어떤 에이전트를 호출하는지 투명하게 안내합니다.
실행이 시작되면 각 에이전트가 분석 진행 상황을 보고합니다.
security-scanner는 의존성 3개에 알려진 CVE를 발견하고 자세히 확인 중이라고 보고합니다.
test-writer는 변경된 5개 함수 중 2개가 테스트 누락이라고 보고합니다.
둘 다 완료되면 메인이 결과를 종합합니다.
보안 의존성 3건과 테스트 누락 2건을 함께 요약합니다.
다음 단계로 패치와 테스트 작성을 제안하고 사용자 확인을 받습니다.
