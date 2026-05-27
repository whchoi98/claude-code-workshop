# Slide 123: 비용 통제 마지막 점검

**Part 8: RECAP & 4 LABS**

## Code Blocks

### cost helper

```bash
# 비용 계산 헬퍼 함수 (.bashrc에 추가)
claude_cost() {
  jq -r '.usage as $u | .model as $m |
    if ($m | startswith("claude-haiku")) then
      ($u.input_tokens * 1 + $u.output_tokens * 5) / 1e6
    elif ($m | startswith("claude-sonnet")) then
      ($u.input_tokens * 3 + $u.output_tokens * 15) / 1e6
    elif ($m | startswith("claude-opus")) then
      ($u.input_tokens * 15 + $u.output_tokens * 75) / 1e6
    else 0 end'
}
# 사용: claude -p "..." --output-format json | claude_cost
# 결과: 0.0023 (약 $0.0023)
```

## Speaker Notes

비용 통제 마지막 점검입니다.
실수 회피 체크리스트 4가지입니다.
첫째, 모델 선택입니다.
단순 작업은 Haiku, 복잡한 분석만 Sonnet, 핵심만 Opus를 사용합니다.
10배에서 75배 단가 차이를 이해하고 적절히 선택하시기 바랍니다.
둘째, 컨텍스트 최소화입니다.
grep, awk, jq로 사전 필터링해서 필요한 부분만 입력합니다.
전체 파일을 그대로 입력하면 토큰이 폭증합니다.
셋째, 한도 설정입니다.
--max-turns 10-20, --max-tokens 4000-8000을 명시합니다.
폭주를 방지합니다.
넷째, 모니터링입니다.
usage 토큰을 로깅하고 일일과 월간 한도 알람을 설정합니다.
비용을 지속 추적합니다.
claude_cost 헬퍼 함수를 .bashrc에 추가하면 매 호출마다 비용을 즉시 확인할 수 있습니다.
Haiku, Sonnet, Opus 단가를 모델 prefix로 자동 인식합니다.
사용은 claude 명령에 파이프로 연결만 하면 됩니다.
습관화하면 비용 의식이 자연스럽게 정착됩니다.
