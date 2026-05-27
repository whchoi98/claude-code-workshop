# Slide 68: OTel configuration

**Part 5: MONITORING & COST CONTROL**

## Code Blocks

### OTel config

```bash
# managed-settings.json에 telemetry 섹션 추가
{
  "telemetry": {
    "enabled": true,
    "endpoint": "https://otel-collector.company.com:4318",
    "headers": {
      "Authorization": "Bearer ${OTEL_TOKEN}"
    },
    "exporters": ["traces", "metrics", "logs"],
    "sampling": {
      "traces": 1.0,
      "metrics": "always"
    },
    "attributes": {
      "service.name": "claude-code",
      "deployment.environment": "production",
      "company.region": "kr"
    }
  }
}

# 효과
- 모든 Claude Code 인스턴스가 사내 OTel Collector로 전송
- 사용자가 비활성화할 수 없음 (managed 강제)
- 표준 OTLP 프로토콜로 호환성 보장
- 사내 SIEM/APM과 자동 통합
```

## Speaker Notes

OpenTelemetry 설정 방법입니다.
managed-settings.json에 telemetry 섹션을 추가해 강제합니다.
enabled를 true로 설정하고 endpoint에 사내 OTel Collector URL을 지정합니다.
4318 포트가 OTLP HTTP 표준 포트입니다.
headers에 Authorization Bearer 토큰으로 인증 정보를 전달합니다.
exporters에 traces, metrics, logs 세 가지를 모두 활성화합니다.
sampling으로 샘플링 비율을 조정합니다.
traces는 1.0으로 100퍼센트, metrics는 always로 항상 수집합니다.
attributes에 service.name, deployment.environment, company.region 같은 메타데이터를 추가합니다.
나중에 필터링과 그루핑에 사용됩니다.
효과는 명확합니다.
모든 Claude Code 인스턴스가 사내 OTel Collector로 전송됩니다.
사용자가 비활성화할 수 없는 강제 설정입니다.
