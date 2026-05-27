# Slide 125: Troubleshooting: Hooks not firing

**Part 8: INTEGRATION & TROUBLESHOOTING**

## Code Blocks

### hooks debug

```bash
# 증상: PostToolUse Hook이 실행되지 않음

# 진단 절차

# 1. settings 로딩 확인
$ claude doctor
# Hooks 섹션에 등록된 hook이 표시되는가?

# 2. matcher 패턴 검증
> /permissions   # 이 명령은 권한 확인이지만
# 등록된 hooks는 doctor 출력으로 확인

# 3. 수동 실행 테스트
$ echo '{
  "session_id": "test",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/tmp/test.js",
    "content": "..."
  }
}' | /opt/claude/hooks/auto-lint.sh

# exit code 확인
$ echo $?
0   # 정상 (0이어야 함)

# 4. --debug 모드로 실시간 추적
$ claude --debug
> [Write 도구 사용]
# stderr에 다음이 표시되어야:
# [hook] PostToolUse matched
# [hook] Running /opt/claude/hooks/auto-lint.sh
# [hook] Exit code: 0

# 5. 일반 원인
- matcher가 너무 좁음 (Write 대신 Edit 호출 등)
- 스크립트 실행 권한 없음 (chmod +x)
- 스크립트 절대 경로가 아님
- timeout이 너무 짧음
- jq 같은 의존성 미설치
```

## Speaker Notes

Hooks가 실행되지 않을 때의 진단 절차입니다.
PostToolUse Hook이 실행되지 않는 증상입니다.
1단계 settings 로딩을 확인합니다.
claude doctor의 Hooks 섹션에 등록된 hook이 표시되는지 봅니다.
2단계 matcher 패턴을 검증합니다.
등록된 hooks를 doctor 출력으로 확인합니다.
3단계 수동 실행 테스트입니다.
JSON을 echo로 만들어 파이프로 스크립트에 전달합니다.
exit code가 0인지 확인합니다.
4단계 --debug 모드로 실시간 추적입니다.
claude --debug 실행 후 도구를 사용하면 stderr에 hook 매칭과 실행 로그가 표시됩니다.
PostToolUse matched, Running, Exit code 0 같은 메시지가 보여야 정상입니다.
5단계 일반 원인입니다.
matcher가 너무 좁아 매칭 안 됨, 스크립트 실행 권한 없음, 절대 경로가 아님, timeout 너무 짧음, jq 같은 의존성 미설치 같은 원인들이 있습니다.
체크리스트처럼 하나씩 확인하면 대부분 문제가 해결됩니다.
