# Slide 39: 비용 최적화 종합

**Part 2: MESSAGES API 심화**

## Code Blocks

### cost tracker

```python
# 비용 모니터링 헬퍼
class CostTracker:
    RATES = {
        "haiku":  {"in": 1.0,  "out": 5.0,  "cache_in": 1.25,  "cache_read": 0.10},
        "sonnet": {"in": 3.0,  "out": 15.0, "cache_in": 3.75,  "cache_read": 0.30},
        "opus":   {"in": 15.0, "out": 75.0, "cache_in": 18.75, "cache_read": 1.50},
    }

    def calc(self, response):
        u = response.usage
        rate = next((v for k,v in self.RATES.items() if k in response.model), None)
        return (u.input_tokens * rate["in"]
                + u.output_tokens * rate["out"]
                + u.cache_creation_input_tokens * rate["cache_in"]
                + u.cache_read_input_tokens * rate["cache_read"]) / 1e6
```

## Speaker Notes

비용 최적화 종합 5가지 핵심 전략입니다.
첫째, 모델 적합입니다.
분류는 Haiku로 10배 절감, 일반은 Sonnet, 핵심만 Opus를 사용합니다.
Opus는 Haiku의 15배 단가이므로 핵심 결정에만 사용하시기 바랍니다.
둘째, Prompt Caching입니다.
시스템 프롬프트를 5분 캐시하면 반복 호출 시 90 퍼센트 절감 효과가 있습니다.
셋째, max_tokens 최적화입니다.
필요한 만큼만 명시합니다.
짧은 응답에 8000은 낭비이고 1024로도 충분합니다.
넷째, 입력 최소화입니다.
count_tokens로 사전 확인하고 RAG로 관련 부분만 선택합니다.
CostTracker 클래스 예시를 봅니다.
RATES에 모델별 단가를 정의합니다.
in, out, cache_in, cache_read 4가지 단가를 모두 관리합니다.
calc 메서드에서 응답의 usage를 받아 종합 비용을 계산합니다.
response.model로 모델을 식별하고 적절한 단가를 적용합니다.
이 클래스를 모든 호출에 사용하면 정확한 비용 추적이 가능합니다.
