# Slide 74: OAuth: 사용량 모니터링

**Part 4: AUTHENTICATION**

## Code Blocks

### usage

```bash
# 1. 현재 세션 사용량 확인
$ /cost
Session usage
  Input tokens:    45,231
  Output tokens:   12,845
  Tool calls:      87
  Subagent calls:  3
  Cache reads:     8,910

Daily plan usage (Claude Max)
  Used:        2,341 / 10,000 messages (23%)
  Resets:      in 3h 27m

# 2. 누적 사용 내역 (Anthropic 콘솔)
# https://console.anthropic.com/settings/usage

# 3. 한도 경고
> [WARN] You've used 85% of your Pro window.
>        Consider /clear or switching to API key.
```

## Speaker Notes

Pro와 Max 사용자에게 가장 중요한 것은 사용량 모니터링입니다.
/cost 슬래시 명령을 실행하면 현재 세션의 입력/출력 토큰, 도구 호출 횟수, Subagent 호출, 캐시 읽기까지 상세히 표시됩니다.
일일 플랜 사용량과 리셋까지 남은 시간도 함께 표시되어 자신의 사용 패턴을 즉시 파악할 수 있습니다.
누적 사용 내역은 console.anthropic.com의 settings/usage 대시보드에서 그래프와 함께 확인할 수 있습니다.
한도의 85%에 도달하면 경고가 표시되고, /clear로 컨텍스트를 비우거나 API Key 모드로 전환하는 것을 권장합니다.
