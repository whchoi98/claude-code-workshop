# Slide 136: Yolo mode

**Part 6: CORE CAPABILITIES**

## Code Blocks

### ⚠️ DANGEROUS

```bash
# 활성화 (CLI 플래그)
claude --dangerously-skip-permissions

# 또는 환경변수
export CLAUDE_DANGEROUSLY_SKIP_PERMISSIONS=true

# Yolo 모드 동작
- allow/ask/deny 정책 모두 무시
- 모든 도구 호출이 즉시 실행
- 사용자 확인 없음

# 절대 권장하지 않는 경우
- 프로덕션 시스템에 직접 연결된 환경
- 자격증명이 있는 머신
- 검토 없이 대량 변경이 누적될 수 있는 환경

# 적절한 사용 사례 (제한적)
- 격리된 컨테이너/VM 안
- 일회성 자동화 작업
- 충분히 검증된 작업 + 사용자 모니터링
- 단, 항상 Git으로 변경 추적 가능해야 함
```

## Speaker Notes

Safe Yolo Mode는 모든 권한 규칙을 일괄로 무시하는 매우 위험한 모드입니다.
CLI 플래그 dangerously-skip-permissions로 활성화하거나 동명의 환경변수로 설정할 수 있습니다.
플래그 이름 자체에 dangerously라는 경고가 들어 있는 만큼 신중하게 사용해야 합니다.
절대 권장하지 않는 환경은 프로덕션 시스템에 연결된 머신, 자격증명이 있는 머신입니다.
적절한 사용은 격리된 컨테이너나 VM, 일회성 자동화로 제한됩니다.
