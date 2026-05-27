# Slide 15: 컨텍스트 옵션

**Part 1: claude 명령 기본**

## Code Blocks

### context

```bash
# 1. --cwd : 작업 디렉토리 변경
$ claude -p "이 프로젝트 분석" --cwd /path/to/project
# 임시로 다른 디렉토리에서 실행
# 현재 셸의 cwd는 변경되지 않음

# 2. --system-prompt : 시스템 프롬프트 추가
$ claude -p "이 코드 검토해 줘" \
    --system-prompt "당신은 보안 전문가입니다. \
                     OWASP Top 10 관점에서 검토."

# 또는 파일에서 로드
$ claude -p "..." \
    --system-prompt "$(cat prompts/security-reviewer.md)"

# 3. --resume : 마지막 세션 이어가기
$ claude -p "그 다음 단계는?"  # 새 세션
$ claude --resume               # 마지막 대화로 복귀
$ claude --resume -p "그 다음"  # 마지막 + Headless

# 4. --continue : 특정 세션 이어가기
$ claude --continue ses_abc123  # session_id로 복귀
# Headless에서 다단계 작업에 유용

# 5. 세션 ID 확인
$ claude -p "..." --output-format json | jq -r '.session_id'

# 6. 다단계 자동화 패턴
$ STEP1=$(claude -p "코드 분석" --output-format json)
$ SES=$(echo "$STEP1" | jq -r '.session_id')
$ STEP2=$(claude --continue "$SES" -p "이제 수정안 제시")
```

## Speaker Notes

컨텍스트 옵션을 살펴봅니다.
첫째, --cwd는 작업 디렉토리를 변경합니다.
임시로 다른 디렉토리에서 실행하는 효과입니다.
현재 셸의 cwd는 변경되지 않습니다.
둘째, --system-prompt는 시스템 프롬프트를 추가합니다.
역할이나 관점을 강하게 지정할 수 있습니다.
파일에서 로드하는 패턴도 권장됩니다.
셋째, --resume은 마지막 세션을 이어가기 합니다.
이전 대화 컨텍스트를 자동으로 복원합니다.
새 프롬프트를 추가로 줄 수도 있습니다.
넷째, --continue는 특정 세션 ID로 이어가기입니다.
여러 세션을 명시적으로 관리할 때 유용합니다.
Headless에서 다단계 작업에 핵심입니다.
다섯째, 세션 ID는 JSON 출력에서 추출 가능합니다.
여섯째, 다단계 자동화 패턴이 가능합니다.
첫 단계의 session_id를 받아 두 번째 단계에서 --continue로 이어가면 한 작업을 여러 명령으로 분할할 수 있습니다.
