# Slide 126: WebFetch

**Part 6: CORE CAPABILITIES**

## Code Blocks

### WebFetch

```bash
# WebFetch 도구
WebFetch(
  url: "https://docs.anthropic.com/claude-code/overview",
  prompt: "Subagents 기능에 대한 핵심 요약과 사용 예시 추출",
)

# 동작
- 페이지 다운로드 + HTML→Markdown 변환
- prompt에 따라 Claude가 의미 추출 (LLM 단계)
- 결과: 구조화된 요약 + 핵심 인용

# 캐시 정책
- 동일 URL 15분간 캐싱 (네트워크 절약)
- prompt가 달라도 캐시 활용
- 강제 갱신 옵션은 별도

# 활용 예시
- 공식 문서에서 특정 섹션 추출
- 변경 로그에서 breaking change 식별
- GitHub PR/Issue 분석
```

## Speaker Notes

WebFetch 도구는 특정 URL을 가져와서 분석하는 도구입니다.
url과 prompt를 함께 지정합니다.
prompt는 Claude에게 페이지에서 무엇을 추출할지 알려주는 지시문입니다.
동작은 세 단계로, 먼저 페이지를 다운로드하고 HTML을 Markdown으로 변환합니다.
다음 prompt 기준으로 Claude가 페이지 내용에서 의미를 추출하는 LLM 단계가 실행됩니다.
결과는 구조화된 요약과 핵심 인용이 반환됩니다.
