# Slide 135: Auto-accept mode

**Part 6: CORE CAPABILITIES**

## Code Blocks

### auto-accept

```bash
# 활성화 방법
# 1. 대화형 세션에서 Shift+Tab으로 모드 토글
# 2. 또는 --permission-mode auto-accept 플래그

# Auto-accept 동작
- ask 목록의 도구도 자동 진행 (사용자 확인 없이)
- deny 목록은 여전히 거부됨
- 변경은 모두 적용되지만 사용자가 추후 git diff로 검토 가능

# 활용 시점
- 신뢰할 수 있는 작업 (예: 단순 리팩토링)
- 대량의 반복 변경 처리
- 사용자가 옆에서 모니터링 중인 경우

# 주의사항
- 한밤중 대량 실행은 피하기 (검토 없이 누적되면 위험)
- Git을 통한 변경 가시화 필수
- Yolo 모드와는 다름 (deny 여전히 동작)
```

## Speaker Notes

Auto-accept 모드는 ask 목록의 도구도 자동 진행하는 모드입니다.
대화형 세션에서는 Shift+Tab 키로 토글하며, 헤드리스에서는 permission-mode auto-accept 플래그로 활성화합니다.
동작은 ask 목록 도구도 사용자 확인 없이 자동 진행하지만 deny 목록은 여전히 거부됩니다.
활용 시점은 신뢰할 수 있는 작업, 대량의 반복 변경 처리, 사용자가 옆에서 모니터링 중인 경우입니다.
