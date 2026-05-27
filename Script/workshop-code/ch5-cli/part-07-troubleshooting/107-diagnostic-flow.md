# Slide 107: 진단 흐름

**Part 7: 디버깅과 트러블슈팅**

## Code Blocks

### diagnostic flow

```bash
# 1단계: 종합 진단
$ claude doctor
# 모든 영역(인증, 네트워크, MCP)을 한 번에 체크

# 2단계: 상세 디버그 모드
$ claude --debug -p "..." 2> /tmp/claude-debug.log
# stderr에 모든 내부 동작 기록

# 3단계: 로그 분석
$ grep -i error /tmp/claude-debug.log
$ tail -100 /tmp/claude-debug.log

# 4단계: 직접 검증
$ curl -v https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{"model":"...", "max_tokens":10, "messages":[{"role":"user","content":"hi"}]}'

# 5단계: 에스컬레이션
# - 사내 Slack #claude-help
# - Anthropic Support (https://support.anthropic.com)
# - GitHub Issues (anthropics/claude-code)
```

## Speaker Notes

진단 흐름은 5단계입니다.
1단계 claude doctor로 종합 진단합니다.
인증, 네트워크, MCP 모든 영역을 한 번에 체크해 빠른 개요를 얻습니다.
2단계 --debug 모드로 상세 디버그를 실행합니다.
stderr 출력을 파일로 저장해 분석에 활용합니다.
3단계 로그 분석입니다.
grep으로 에러 키워드를 찾고 tail로 최근 로그를 봅니다.
4단계 직접 검증입니다.
curl로 API를 직접 호출해 Claude Code 외부 문제인지 확인합니다.
API 키, 모델 ID, 헤더가 정확한지 검증합니다.
5단계 에스컬레이션입니다.
자체 해결이 어려우면 사내 Slack의 claude-help 채널, Anthropic Support, GitHub Issues 순서로 에스컬레이션합니다.
로그 파일과 doctor 출력을 함께 첨부하면 빠른 해결이 가능합니다.
