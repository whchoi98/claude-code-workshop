# Slide 134: ask mode

**Part 6: CORE CAPABILITIES**

## Code Blocks

### Ask UX

```bash
# 사용자 경험 - 매 위험 작업마다 확인 받음

  Claude: I want to modify src/services/payment.js:

    -  return amount;
    +  return amount * (1 + taxRate);

  Approve this change? [y/N/q/a/d]
    y - yes, apply this single change
    N - no, skip and continue
    q - quit, cancel rest of work
    a - yes, and auto-approve similar future Edits
    d - drop into debug, show me the file context

# 그룹 승인
- 같은 도구의 연속 호출은 한 번에 승인 가능
- 'a' 응답으로 세션 동안 자동 승인

# 안전 장치
- 무한 자동 동의 방지 (n번 후 재확인)
- 사용자 abort 시 즉시 중단
```

## Speaker Notes

Ask 모드는 대화형 사용 시 기본 동작입니다.
위험한 작업, 즉 파일 수정이나 변경 명령을 시도할 때마다 사용자에게 확인을 받습니다.
화면 예시처럼 Claude가 어떤 변경을 할 것인지 diff 형식으로 보여주고, y N q a d 5가지 선택지를 제공합니다.
y는 이번 변경만 승인, 대문자 N은 건너뛰기로 기본값입니다.
q는 전체 작업 취소, a는 이번 변경을 승인하면서 세션 동안 비슷한 변경도 자동 승인, d는 디버그 모드로 진입합니다.
