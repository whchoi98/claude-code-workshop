# Slide 18: Cost & latency

**Part 1: SUBAGENTS 개념과 원리**

## Code Blocks

### Cost Calc

```bash
# 단일 에이전트
보안 검사 (Sonnet) → 50K input + 5K output → 약 $0.23, 60초

# Subagent 위임 시 (3개 병렬)
Main (Sonnet)
  ├─ security-scanner (Opus)   50K + 5K → $1.13, 80초
  ├─ docs-writer (Sonnet)      30K + 8K → $0.21, 40초
  └─ test-extender (Sonnet)    40K + 10K → $0.27, 50초

총 비용: $1.61 (vs 단일 $0.23, 약 7배)
총 시간: max(80, 40, 50) = 80초 (병렬, vs 순차 170초)

# 트레이드오프
+ 시간 단축 (170s → 80s, -53%)
+ 작업별 모델 최적화 가능
- 비용 증가 (7배)
- 메인 컨텍스트 보존 가치 별도
```

## Speaker Notes

병렬화의 진짜 비용을 살펴봅니다.
단일 에이전트로 보안 검사만 했을 때를 가정합니다.
50K 입력에 5K 출력으로 약 0.23달러, 60초가 소요됩니다.
Subagent로 3개를 병렬 위임하는 경우를 봅니다.
메인 외에 security-scanner, docs-writer, test-extender 세 개를 동시에 호출합니다.
security-scanner를 Opus로 호출하면 80초에 1.13달러가 듭니다.
나머지 두 개는 Sonnet으로 합쳐 약 0.48달러입니다.
총 비용은 1.61달러로 단일 대비 약 7배입니다.
반면 총 시간은 가장 긴 80초로 끝나며 순차 실행 170초 대비 53퍼센트 단축됩니다.
트레이드오프가 명확합니다.
시간은 절반 가까이 줄지만 비용은 7배가 될 수 있습니다.
Opus가 비용 주범이므로 정말 필요한 작업에만 사용하는 것이 좋습니다.
