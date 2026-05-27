# Slide 49: Hook debugging

**Part 3: HOOKS 4가지 시점**

## Code Blocks

### debug

```bash
# 1. --debug 모드로 hook 동작 추적
$ claude --debug
# stderr에 hook 실행 로그 출력
# 어느 hook이 어떤 입력을 받았는지, 어떤 결과를 냈는지

# 2. 수동 테스트 (Hook 스크립트 직접 실행)
$ echo '{
  "session_id": "test",
  "tool_name": "Bash",
  "tool_input": { "command": "rm -rf /tmp/test" }
}' | /opt/claude/hooks/dlp-check.sh

# 결과 확인
$ echo $?  # exit code
1
$ # stderr에 '{"action":"block","reason":"위험 명령"}' 출력

# 3. timeout 디버깅
# managed-settings에 timeout 충분히 설정
{
  "hooks": {
    "PreToolUse": [{
      "hooks": [{ 
        "type": "command",
        "command": "...",
        "timeout": 10000   # 10초로 늘려서 디버깅
      }]
    }]
  }
}

# 4. 로그 추가 (스크립트 내부)
echo "DEBUG: input=$INPUT" >> /tmp/claude-hook.log
echo "DEBUG: tool=$TOOL"  >> /tmp/claude-hook.log

# 5. 일반 실수
- exit code 잘못: exit 1을 0으로 (차단이 안 됨)
- stderr 누락: JSON을 stdout으로 (Claude가 못 받음)
- jq 미설치: 명령 실행 실패
```

## Speaker Notes

Hook 디버깅 방법을 정리합니다.
첫째, --debug 모드로 hook 동작을 추적합니다.
claude --debug로 실행하면 stderr에 hook 실행 로그가 출력됩니다.
어느 hook이 어떤 입력을 받았는지, 어떤 결과를 냈는지 모두 볼 수 있습니다.
둘째, 수동 테스트입니다.
Hook 스크립트를 직접 실행해 검증할 수 있습니다.
echo로 JSON을 만들어 파이프로 전달하고 exit code와 stderr 출력을 확인합니다.
셋째, timeout 디버깅입니다.
스크립트가 timeout에 걸리는지 확인하려면 timeout을 10초 정도로 늘려서 테스트합니다.
넷째, 로그 추가입니다.
스크립트 내부에 echo로 디버그 로그를 /tmp 파일에 기록합니다.
다섯째, 일반 실수입니다.
exit code 잘못 사용은 가장 흔한 실수입니다.
exit 1을 0으로 잘못 적으면 차단이 안 됩니다.
stderr 누락도 흔합니다.
JSON을 stdout으로 보내면 Claude가 못 받습니다.
jq 미설치 시 명령 실행 자체가 실패합니다.
