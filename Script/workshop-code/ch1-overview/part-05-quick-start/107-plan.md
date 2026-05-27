# Slide 107: Plan 모드 활성화 상세

**Part 5: QUICK START**

## Code Blocks

### plan mode

```bash
# 1. REPL에서 토글 (가장 일반적)
> [Shift + Tab]
> [Plan mode: ON]  (오렌지색 표시)

# 다시 누르면 OFF
> [Shift + Tab]
> [Plan mode: OFF]

# 2. 명령행 플래그로 시작 시 강제
$ claude --plan-mode
# 또는
$ claude -p "리팩토링해" --plan-mode

# 3. settings.json으로 기본값 설정
{
  "defaultMode": "plan"
}

# 4. Plan 모드에서 사용 가능한 추가 명령
> /plan        # 현재까지의 계획만 보기
> /accept      # 마지막 계획 승인
> /reject      # 계획 거부 후 재논의
```

## Speaker Notes

Plan 모드 활성화 방법을 자세히 살펴봅니다.
가장 일반적인 방법은 REPL에서 Shift+Tab 키 조합으로 토글하는 것입니다.
모드가 켜지면 오렌지색 표시가 입력 프롬프트 옆에 나타나고, 다시 누르면 OFF됩니다.
명령행에서 --plan-mode 플래그로 시작 시 강제 활성화할 수도 있고, 헤드리스 모드에서도 사용 가능합니다.
settings.json의 defaultMode 옵션을 plan으로 설정하면 매번 자동으로 Plan 모드로 시작합니다.
Plan 모드 전용 추가 명령으로 /plan은 현재까지의 계획만 다시 보기, /accept는 마지막 계획 승인, /reject는 계획 거부 후 재논의입니다.
