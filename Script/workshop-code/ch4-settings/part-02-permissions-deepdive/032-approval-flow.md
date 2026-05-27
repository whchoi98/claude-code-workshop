# Slide 32: Approval flow

**Part 2: PERMISSIONS 심화**

## Code Blocks

### approval UX

```bash
# 사용자에게 표시되는 확인 메시지 예시

> Edit src/payment.js
─────────────────────────────────────────
Allow this Edit operation?

File: src/payment.js
Diff preview:
- function processPayment(amount) {
+ function processPayment(amount, currency = 'USD') {
+   if (!amount || amount <= 0) throw new Error(...);

  [y] Yes, allow once
  [a] Yes, allow this tool for session
  [n] No, deny this time
  [d] No, and add to deny list
─────────────────────────────────────────
Your choice:

# 세션 동안 'a' 선택 시 같은 도구는 자동 허용
# 'd' 선택 시 settings.local.json에 deny 추가됨
```

## Speaker Notes

Ask 승인 흐름의 UX를 살펴봅니다.
5단계로 진행됩니다.
Claude가 도구 호출을 시도하면 ask 규칙 매칭을 확인합니다.
매칭되면 사용자에게 확인을 요청합니다.
사용자가 승인 또는 거부하면 도구가 실행되거나 중단됩니다.
실제 표시되는 확인 메시지를 봅니다.
Edit src payment.js 호출 시 파일 경로와 diff 미리보기가 표시됩니다.
4가지 응답 옵션이 있습니다.
y는 이번만 허용, a는 이 세션 동안 같은 도구 자동 허용, n은 이번 거부, d는 거부하고 deny 리스트에 추가입니다.
a를 선택하면 세션 동안 같은 도구는 자동 허용됩니다.
d를 선택하면 settings.local.json에 deny 규칙이 자동 추가되어 영구적으로 차단됩니다.
사용자가 작업 흐름을 잃지 않으면서도 통제할 수 있는 좋은 UX입니다.
