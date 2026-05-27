# Chapter 6: Agent SDK

SDK 통합과 운영

코드 블록 슬라이드: 112개

[← 워크샵 메인](../README.md)

## 파트 목록

## Part 1: SDK 기본
Slides 6-20 (15 slides)

  - [Slide 7: Python 설치와 첫 호출](./part-01-sdk-basics/007-python-install-first-call.md)
  - [Slide 8: TypeScript 설치와 첫 호출](./part-01-sdk-basics/008-typescript-install-first-call.md)
  - [Slide 9: 비동기 클라이언트 (Python)](./part-01-sdk-basics/009-async-client-python.md)
  - [Slide 10: 비동기 클라이언트 (TypeScript)](./part-01-sdk-basics/010-async-client-typescript.md)
  - [Slide 11: 클라이언트 구조 깊이 이해](./part-01-sdk-basics/011-client-structure-deep-understanding.md)
  - [Slide 12: 인증 옵션](./part-01-sdk-basics/012-auth.md)
  - [Slide 13: 모델 선택](./part-01-sdk-basics/013-model-selection.md)
  - [Slide 14: 환경별 클라이언트 설정](./part-01-sdk-basics/014-env-client-config.md)
  - [Slide 15: 에러 처리 기본](./part-01-sdk-basics/015-error-handling-basics.md)
  - [Slide 16: TypeScript 에러 처리](./part-01-sdk-basics/016-typescript-error-handling.md)
  - [Slide 17: 첫 SDK 앱 예시](./part-01-sdk-basics/017-first-sdk-example.md)
  - [Slide 18: 첫 SDK 앱 TypeScript](./part-01-sdk-basics/018-first-sdk-typescript.md)

## Part 2: MESSAGES API 심화
Slides 21-40 (20 slides)

  - [Slide 22: 메시지 형식과 role](./part-02-messages-api-deepdive/022-message-format-role.md)
  - [Slide 23: 시스템 프롬프트](./part-02-messages-api-deepdive/023-system-prompt.md)
  - [Slide 24: 멀티턴 대화 기본](./part-02-messages-api-deepdive/024-multi-turn-conversation-basics.md)
  - [Slide 25: 대화 상태 보관](./part-02-messages-api-deepdive/025-conversation-state-storage.md)
  - [Slide 26: max_tokens와 stop_reason](./part-02-messages-api-deepdive/026-max-tokens-stop-reason.md)
  - [Slide 27: temperature와 top_p](./part-02-messages-api-deepdive/027-temperature-top-p.md)
  - [Slide 28: stop_sequences](./part-02-messages-api-deepdive/028-stop-sequences.md)
  - [Slide 29: 메시지 메타데이터](./part-02-messages-api-deepdive/029-message.md)
  - [Slide 30: 토큰 측정](./part-02-messages-api-deepdive/030-token-measure.md)
  - [Slide 31: Prompt Caching 기본](./part-02-messages-api-deepdive/031-prompt-caching-basics.md)
  - [Slide 32: Prompt Caching 심화](./part-02-messages-api-deepdive/032-prompt-caching-deepdive.md)
  - [Slide 33: 컨텍스트 윈도우 관리](./part-02-messages-api-deepdive/033-management.md)
  - [Slide 34: 멀티 메시지 구조](./part-02-messages-api-deepdive/034-multi-message-structure.md)
  - [Slide 35: 이미지 메시지 (Vision)](./part-02-messages-api-deepdive/035-message-vision.md)
  - [Slide 36: PDF 입력](./part-02-messages-api-deepdive/036-pdf-input.md)
  - [Slide 37: 메시지 검증](./part-02-messages-api-deepdive/037-message-validation.md)
  - [Slide 38: 대화 저장과 로드](./part-02-messages-api-deepdive/038-conversation.md)
  - [Slide 39: 비용 최적화 종합](./part-02-messages-api-deepdive/039-cost-summary.md)

## Part 3: TOOL USE
Slides 41-60 (20 slides)

  - [Slide 42: Tool Use 개념](./part-03-tool-use/042-tool-use-concept.md)
  - [Slide 43: 도구 정의 상세](./part-03-tool-use/043-tool-definition.md)
  - [Slide 44: 호출 사이클 구현](./part-03-tool-use/044-call-cycle.md)
  - [Slide 45: tool_use와 tool_result 형식](./part-03-tool-use/045-tool-use-tool-result-format.md)
  - [Slide 46: 멀티 도구 호출](./part-03-tool-use/046-multi-tool-call.md)
  - [Slide 47: tool_choice 제어](./part-03-tool-use/047-tool-choice.md)
  - [Slide 48: 실전 예시 / DB 검색 봇](./part-03-tool-use/048-practical-example-db-search.md)
  - [Slide 49: 실전 예시 / API 클라이언트](./part-03-tool-use/049-practical-example-api-client.md)
  - [Slide 50: 실전 / 파일 시스템 도구](./part-03-tool-use/050-practical-file-system-tool.md)
  - [Slide 51: 도구 응답 캐싱](./part-03-tool-use/051-tool-response-caching.md)
  - [Slide 52: 동적 도구 정의](./part-03-tool-use/052-tool-definition.md)
  - [Slide 53: 에이전트 패턴](./part-03-tool-use/053-agent.md)
  - [Slide 54: 도구 에러 처리](./part-03-tool-use/054-tool-error-handling.md)
  - [Slide 55: 도구 호출 검증](./part-03-tool-use/055-tool-call-validation.md)
  - [Slide 56: 도구 호출 로깅](./part-03-tool-use/056-tool-call.md)
  - [Slide 57: 도구 테스트](./part-03-tool-use/057-tool-test.md)
  - [Slide 59: 도구 정의 종합 예시](./part-03-tool-use/059-tool-definition-summary-example.md)

## Part 4: STREAMING
Slides 61-80 (20 slides)

  - [Slide 62: 스트리밍 기본](./part-04-streaming/062-basics.md)
  - [Slide 63: 스트림 이벤트 타입](./part-04-streaming/063-event-type.md)
  - [Slide 64: 도구 호출 스트리밍](./part-04-streaming/064-tool-call.md)
  - [Slide 65: FastAPI SSE 서버](./part-04-streaming/065-fastapi-sse-server.md)
  - [Slide 66: React SSE 클라이언트](./part-04-streaming/066-react-sse-client.md)
  - [Slide 67: 스트림 중단](./part-04-streaming/067-cancellation.md)
  - [Slide 68: 청크 후처리](./part-04-streaming/068-handling.md)
  - [Slide 69: WebSocket 통합](./part-04-streaming/069-websocket-integration.md)
  - [Slide 70: 스트림과 도구 결합](./part-04-streaming/070-tool.md)
  - [Slide 71: 백프레셔](./part-04-streaming/071-backpressure.md)
  - [Slide 72: 스트림 에러 처리](./part-04-streaming/072-error-handling.md)
  - [Slide 73: 스트림 디버깅](./part-04-streaming/073-debugging.md)
  - [Slide 75: 스트림 캐싱](./part-04-streaming/075-caching.md)
  - [Slide 76: 실시간 음성 통합](./part-04-streaming/076-realtime-voice-integration.md)
  - [Slide 79: 완성 예시 / 스트리밍 챗봇](./part-04-streaming/079-complete-example-chatbot.md)

## Part 5: MCP SDK 통합
Slides 81-100 (20 slides)

  - [Slide 82: MCP 복습](./part-05-mcp-integration/082-comparison.md)
  - [Slide 83: mcp_servers 매개변수](./part-05-mcp-integration/083-mcp-servers.md)
  - [Slide 84: MCP 도구 흐름](./part-05-mcp-integration/084-mcp-tool.md)
  - [Slide 85: 응답 처리](./part-05-mcp-integration/085-response-handling.md)
  - [Slide 86: 사내 MCP 서버 연결](./part-05-mcp-integration/086-mcp-server.md)
  - [Slide 87: MCP 도구 권한 통제](./part-05-mcp-integration/087-mcp-tool-permission-control.md)
  - [Slide 88: MCP 서버 디버깅](./part-05-mcp-integration/088-mcp-server.md)
  - [Slide 89: 실전 / GitHub 통합](./part-05-mcp-integration/089-practical-github-integration.md)
  - [Slide 90: 실전 / Slack 통합](./part-05-mcp-integration/090-practical-slack-integration.md)
  - [Slide 91: 실전 / Database MCP](./part-05-mcp-integration/091-practical-database-mcp.md)
  - [Slide 92: MCP + Streaming](./part-05-mcp-integration/092-mcp-streaming.md)
  - [Slide 93: MCP 비용 추적](./part-05-mcp-integration/093-mcp-cost-tracking.md)
  - [Slide 94: MCP 캐싱 결합](./part-05-mcp-integration/094-mcp-caching.md)
  - [Slide 98: 완성 예시 / 통합 비서](./part-05-mcp-integration/098-complete-example-integration.md)

## Part 6: PRODUCTION 운영
Slides 101-120 (20 slides)

  - [Slide 103: 에러 분류와 대응](./part-06-production/103-error-classify.md)
  - [Slide 104: Retry Python](./part-06-production/104-retry-python.md)
  - [Slide 105: Retry TypeScript](./part-06-production/105-retry-typescript.md)
  - [Slide 106: Rate Limiting 이해](./part-06-production/106-rate-limiting-understanding.md)
  - [Slide 107: Rate Limiter 구현](./part-06-production/107-rate-limiter.md)
  - [Slide 108: Timeout과 Circuit Breaker](./part-06-production/108-timeout-circuit-breaker.md)
  - [Slide 109: 구조화 로깅](./part-06-production/109-structure.md)
  - [Slide 110: 메트릭과 대시보드](./part-06-production/110-metric.md)
  - [Slide 111: 분산 트레이싱](./part-06-production/111-distributed-tracing.md)
  - [Slide 112: 헬스체크와 readiness](./part-06-production/112-health-readiness.md)
  - [Slide 113: 비용 모니터링](./part-06-production/113-cost-monitoring.md)
  - [Slide 114: API key 관리](./part-06-production/114-api-key-management.md)
  - [Slide 115: 입력 검증](./part-06-production/115-input-validation.md)
  - [Slide 116: 단위 테스트](./part-06-production/116-unit-test.md)
  - [Slide 117: 통합 테스트](./part-06-production/117-integration-test.md)
  - [Slide 118: 부하 테스트](./part-06-production/118-load-test.md)
  - [Slide 119: 배포 전략](./part-06-production/119-deploy-strategy.md)

## Part 7: 고급 패턴
Slides 121-135 (15 slides)

  - [Slide 122: 멀티 에이전트 개요](./part-07-advanced-patterns/122-multi-agent.md)
  - [Slide 123: Orchestrator-Worker 패턴](./part-07-advanced-patterns/123-orchestrator-worker.md)
  - [Slide 124: Specialist 분리](./part-07-advanced-patterns/124-specialist.md)
  - [Slide 125: 에이전트 간 통신](./part-07-advanced-patterns/125-agent.md)
  - [Slide 126: 백그라운드 작업](./part-07-advanced-patterns/126-background-task.md)
  - [Slide 127: 큐 기반 비동기 처리](./part-07-advanced-patterns/127-queue-async-handling.md)
  - [Slide 128: 캐싱 전략 종합](./part-07-advanced-patterns/128-caching-strategy-summary.md)
  - [Slide 129: Semantic 캐시](./part-07-advanced-patterns/129-semantic.md)
  - [Slide 130: 비용 최적화 종합](./part-07-advanced-patterns/130-cost-summary.md)
  - [Slide 131: 모델 캐스케이딩](./part-07-advanced-patterns/131-model-cascading.md)
  - [Slide 132: Prompt 압축](./part-07-advanced-patterns/132-prompt-compression.md)
  - [Slide 133: 응답 검증과 자가 비평](./part-07-advanced-patterns/133-response-validation-self-critique.md)
  - [Slide 134: Constitutional AI 패턴](./part-07-advanced-patterns/134-constitutional-ai.md)

## Part 8: RECAP & 4 LABS
Slides 136-150 (15 slides)

  - [Slide 138: Lab 1 / 첫 SDK 호출](./part-08-recap-labs/138-lab-1-first-sdk-call.md)
  - [Slide 139: Lab 2 / Tool Use 봇](./part-08-recap-labs/139-lab-2-tool-use.md)
  - [Slide 140: Lab 3 / Streaming 챗봇](./part-08-recap-labs/140-lab-3-streaming-chatbot.md)
  - [Slide 141: Lab 4 / 프로덕션 운영](./part-08-recap-labs/141-lab-4-operations.md)
  - [Slide 143: 학습 자원](./part-08-recap-labs/143-learning-resources.md)
  - [Slide 144: 비용 통제 마지막 점검](./part-08-recap-labs/144-cost-control-final-check.md)
