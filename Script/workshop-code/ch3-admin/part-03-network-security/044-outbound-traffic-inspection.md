# Slide 44: Outbound traffic inspection

**Part 3: NETWORK & SECURITY**

## Code Blocks

### Egress Monitor

```bash
# 시나리오: 사내에서 AI API 트래픽을 검사하려는 요건

# 1. 검사 가능한 정보
+ 도메인 (api.anthropic.com 등)
+ 트래픽 양 (사용량 모니터링)
+ 시간대 패턴
- 요청 본문 (TLS 암호화로 불가)

# 2. 본문 검사가 필요한 경우 (드물지만)
- TLS Intercept 프록시 사용 (사내 CA로 재서명)
- 단점: 무결성, 성능, 신뢰 이슈
- 권장: 본문 검사 대신 클라이언트 측 로깅 우선

# 3. 클라이언트 측 로깅 패턴
# OpenTelemetry exporter (Part 5에서 상세)
# - 토큰 수, 모델, 도구 호출 로깅
# - 본문은 hash만 저장
# - 사내 SIEM으로 전송

# 4. Data Loss Prevention (DLP)
- 민감 데이터 (PII, 비밀번호) 입력 감지
- Hooks와 결합해 PreToolUse 단계에서 차단
- 사내 DLP 도구 (Symantec, Forcepoint 등) 연동
```

## Speaker Notes

아웃바운드 트래픽 검사 방법을 살펴봅니다.
사내에서 AI API 트래픽을 검사하려는 요건이 있을 때 적용합니다.
1단계 검사 가능한 정보를 정확히 이해해야 합니다.
도메인, 트래픽 양, 시간대 패턴은 검사 가능합니다.
요청 본문은 TLS 암호화로 검사가 불가능합니다.
2단계 본문 검사가 정말 필요한 경우 TLS Intercept 프록시를 사용할 수 있습니다.
사내 CA로 재서명하는 방식이지만 무결성, 성능, 신뢰 이슈가 있습니다.
권장 방식은 본문 검사 대신 클라이언트 측 로깅을 우선하는 것입니다.
3단계 클라이언트 측 로깅 패턴입니다.
OpenTelemetry exporter를 활용해 토큰 수, 모델, 도구 호출을 로깅합니다.
본문은 해시만 저장하고 사내 SIEM으로 전송합니다.
Part 5에서 상세히 다룹니다.
4단계 Data Loss Prevention 통합입니다.
PII나 비밀번호 같은 민감 데이터 입력을 감지합니다.
Hooks와 결합해 PreToolUse 단계에서 차단할 수 있습니다.
