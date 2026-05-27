# Chapter 5: CLI Reference

CLI 명령어와 자동화

코드 블록 슬라이드: 86개

[← 워크샵 메인](../README.md)

## 파트 목록

## Part 1: claude 명령 기본
Slides 6-20 (15 slides)

  - [Slide 7: Command structure](./part-01-claude-cli-basics/007-command-structure.md)
  - [Slide 8: --help system](./part-01-claude-cli-basics/008-help-system.md)
  - [Slide 10: 동작 모드 옵션](./part-01-claude-cli-basics/010-slide.md)
  - [Slide 11: 출력 형식 옵션](./part-01-claude-cli-basics/011-output-format.md)
  - [Slide 12: JSON 출력 파싱 (jq)](./part-01-claude-cli-basics/012-json-output-jq.md)
  - [Slide 13: 권한 옵션](./part-01-claude-cli-basics/013-permission.md)
  - [Slide 14: 모델 옵션](./part-01-claude-cli-basics/014-model.md)
  - [Slide 15: 컨텍스트 옵션](./part-01-claude-cli-basics/015-context.md)
  - [Slide 16: 디버깅 옵션](./part-01-claude-cli-basics/016-debug.md)
  - [Slide 19: 명령 조합 패턴](./part-01-claude-cli-basics/019-command.md)

## Part 2: HEADLESS 모드 심화
Slides 21-35 (15 slides)

  - [Slide 22: Headless 입력 방식 6종](./part-02-headless-mode-deepdive/022-headless-input-6.md)
  - [Slide 23: Exit code 활용](./part-02-headless-mode-deepdive/023-exit-code-usage.md)
  - [Slide 24: 자동화 1 / PR 리뷰](./part-02-headless-mode-deepdive/024-automation-1-pr.md)
  - [Slide 25: 자동화 2 / 로그 분석](./part-02-headless-mode-deepdive/025-automation-2-log.md)
  - [Slide 26: 자동화 3 / 문서 생성](./part-02-headless-mode-deepdive/026-automation-3-docs.md)
  - [Slide 27: 자동화 4 / 번역](./part-02-headless-mode-deepdive/027-automation-4.md)
  - [Slide 28: 자동화 5 / 검증](./part-02-headless-mode-deepdive/028-automation-5-validation.md)
  - [Slide 29: 큰 입력 처리](./part-02-headless-mode-deepdive/029-input-handling.md)
  - [Slide 30: 세션 재사용](./part-02-headless-mode-deepdive/030-session-reuse.md)
  - [Slide 31: 에러 처리와 재시도](./part-02-headless-mode-deepdive/031-error-handling-retry.md)
  - [Slide 32: 로깅과 관측성](./part-02-headless-mode-deepdive/032-log-claude.md)
  - [Slide 33: 완성 스크립트 예시](./part-02-headless-mode-deepdive/033-complete-example.md)

## Part 3: 출력 형식과 파싱 심화
Slides 36-50 (15 slides)

  - [Slide 37: JSON 응답 스키마 전체](./part-03-output-format-deepdive/037-json-response-key-overall.md)
  - [Slide 38: stream-json 이벤트 타입 전체](./part-03-output-format-deepdive/038-stream-json-event-type-overall.md)
  - [Slide 40: jq 고급 패턴 (filter)](./part-03-output-format-deepdive/040-jq-filter.md)
  - [Slide 41: jq 고급 (집계)](./part-03-output-format-deepdive/041-aggregation.md)
  - [Slide 42: JSON → CSV 변환](./part-03-output-format-deepdive/042-json-csv.md)
  - [Slide 43: Markdown → HTML 변환](./part-03-output-format-deepdive/043-markdown-html.md)
  - [Slide 44: 다중 호출 집계](./part-03-output-format-deepdive/044-call.md)
  - [Slide 45: 토큰 사용량과 비용 추적](./part-03-output-format-deepdive/045-token-use-cost-tracking.md)
  - [Slide 46: 출력 파일 분할](./part-03-output-format-deepdive/046-output-file.md)
  - [Slide 47: 실시간 진행 표시](./part-03-output-format-deepdive/047-realtime-progress.md)
  - [Slide 48: HTML 대시보드 생성](./part-03-output-format-deepdive/048-html.md)

## Part 4: CI/CD 통합
Slides 51-70 (20 slides)

  - [Slide 52: CI 통합 기본 패턴](./part-04-ci-cd-integration/052-ci-integration-basics.md)
  - [Slide 53: GitHub Actions / 인증](./part-04-ci-cd-integration/053-github-actions-auth.md)
  - [Slide 54: GitHub Actions / 기본 워크플로](./part-04-ci-cd-integration/054-github-actions-basics.md)
  - [Slide 55: GitHub Actions / Matrix 빌드](./part-04-ci-cd-integration/055-github-actions-matrix.md)
  - [Slide 56: GitHub Actions / Reusable Workflow](./part-04-ci-cd-integration/056-github-actions-reusable-workflow.md)
  - [Slide 57: GitLab CI / 기본 설정](./part-04-ci-cd-integration/057-gitlab-ci-basics-config.md)
  - [Slide 58: GitLab CI 고급 패턴](./part-04-ci-cd-integration/058-gitlab-ci.md)
  - [Slide 59: Jenkins / Jenkinsfile 기본](./part-04-ci-cd-integration/059-jenkins-jenkinsfile-basics.md)
  - [Slide 60: Jenkins / Parallel](./part-04-ci-cd-integration/060-jenkins-parallel.md)
  - [Slide 61: Jenkins / Credentials](./part-04-ci-cd-integration/061-jenkins-credentials.md)
  - [Slide 63: 비용 통제](./part-04-ci-cd-integration/063-cost-control.md)
  - [Slide 64: CI 보안 검증](./part-04-ci-cd-integration/064-ci-security-validation.md)
  - [Slide 66: 모니터링과 알람](./part-04-ci-cd-integration/066-monitoring.md)
  - [Slide 67: PR 자동 처리 완성 예시](./part-04-ci-cd-integration/067-pr-handling-complete-example.md)
  - [Slide 68: 다른 CI 시스템 한눈에](./part-04-ci-cd-integration/068-ci-system.md)

## Part 5: 자동화 패턴
Slides 71-90 (20 slides)

  - [Slide 73: Pattern 1 / 핵심 스크립트](./part-05-automation/073-pattern-1.md)
  - [Slide 74: Pattern 1 / 결과 처리](./part-05-automation/074-pattern-1-result-handling.md)
  - [Slide 75: Pattern 1 / GitHub Actions 통합](./part-05-automation/075-pattern-1-github-actions-integration.md)
  - [Slide 76: Pattern 2 / 이슈 트리아지 설계](./part-05-automation/076-pattern-2.md)
  - [Slide 77: Pattern 2 / 분류 스크립트](./part-05-automation/077-pattern-2-classify.md)
  - [Slide 78: Pattern 2 / 액션 실행](./part-05-automation/078-pattern-2.md)
  - [Slide 79: Pattern 2 / GitHub Actions 통합](./part-05-automation/079-pattern-2-github-actions-integration.md)
  - [Slide 80: Pattern 3 / 코드 마이그레이션 설계](./part-05-automation/080-pattern-3.md)
  - [Slide 81: Pattern 3 / 변환 스크립트](./part-05-automation/081-pattern-3.md)
  - [Slide 82: Pattern 3 / 실패 분석](./part-05-automation/082-pattern-3.md)
  - [Slide 84: Pattern 4 / 보안 감사 스크립트](./part-05-automation/084-pattern-4-security-audit.md)
  - [Slide 85: Pattern 4 / 정기 실행](./part-05-automation/085-pattern-4.md)
  - [Slide 86: Pattern 5 / 매일 보고서 설계](./part-05-automation/086-pattern-5.md)
  - [Slide 87: Pattern 5 / 보고서 스크립트](./part-05-automation/087-pattern-5.md)
  - [Slide 88: Pattern 5 / 스케줄 등록](./part-05-automation/088-pattern-5.md)

## Part 6: 환경변수와 설정
Slides 91-105 (15 slides)

  - [Slide 92: 인증 환경변수](./part-06-env-config/092-auth-env.md)
  - [Slide 93: AWS Bedrock 환경변수 심화](./part-06-env-config/093-aws-bedrock-env-deepdive.md)
  - [Slide 94: 네트워크 환경변수](./part-06-env-config/094-network-env.md)
  - [Slide 95: 로그와 디버깅 환경변수](./part-06-env-config/095-log-env.md)
  - [Slide 96: 모델 환경변수](./part-06-env-config/096-model-env.md)
  - [Slide 97: MCP 환경변수](./part-06-env-config/097-mcp-env.md)
  - [Slide 98: 디렉토리와 캐시 환경변수](./part-06-env-config/098-dir-env.md)
  - [Slide 99: 환경변수 점검 명령](./part-06-env-config/099-env-check-command.md)
  - [Slide 100: 환경별 설정 패턴](./part-06-env-config/100-env-config.md)
  - [Slide 101: 환경변수 보안](./part-06-env-config/101-env-security.md)
  - [Slide 102: 환경변수 트러블슈팅](./part-06-env-config/102-env-troubleshooting.md)

## Part 7: 디버깅과 트러블슈팅
Slides 106-115 (10 slides)

  - [Slide 107: 진단 흐름](./part-07-troubleshooting/107-diagnostic-flow.md)
  - [Slide 108: 인증 문제 진단](./part-07-troubleshooting/108-auth.md)
  - [Slide 109: 네트워크 문제 진단](./part-07-troubleshooting/109-network-issues.md)
  - [Slide 110: 응답 동작 문제](./part-07-troubleshooting/110-response.md)
  - [Slide 112: 디버그 정보 수집](./part-07-troubleshooting/112-collect-debug.md)
  - [Slide 113: 자주 묻는 질문](./part-07-troubleshooting/113-slide.md)

## Part 8: RECAP & 4 LABS
Slides 116-130 (15 slides)

  - [Slide 118: Lab 1 / 첫 Headless 호출](./part-08-recap-labs/118-lab-1-first-headless-call.md)
  - [Slide 119: Lab 2 / 자동화 스크립트](./part-08-recap-labs/119-lab-2-automation.md)
  - [Slide 120: Lab 3 / CI 통합](./part-08-recap-labs/120-lab-3-ci-integration.md)
  - [Slide 121: Lab 4 / 데이터 파싱](./part-08-recap-labs/121-lab-4.md)
  - [Slide 123: 비용 통제 마지막 점검](./part-08-recap-labs/123-cost-control-final-check.md)
  - [Slide 127: 학습 자원](./part-08-recap-labs/127-learning-resources.md)
