# Slide 125: WebSearch

**Part 6: CORE CAPABILITIES**

## Code Blocks

### WebSearch

```bash
# WebSearch 도구
WebSearch(query: "React 19 useTransition 변경점")

# 활용 예시
User: 최신 Stripe API의 metered billing 변경사항 알려 주세요.
Claude: [WebSearch("Stripe metered billing 2026 changes")]
        → 검색 결과 요약 + 관련 URL 제시
        [WebFetch("https://stripe.com/docs/...")]
        → 페이지 상세 분석

# 사용 시점
- 라이브러리 최신 버전 변경사항
- 보안 취약점 정보 (CVE)
- 베스트 프랙티스 최신 동향
- API/SDK 공식 문서 참조

# 권장 패턴
- WebSearch로 URL 식별
- 그 후 WebFetch로 정밀 분석
- 결과를 코드에 반영하기 전 사용자에게 확인
```

## Speaker Notes

WebSearch 도구는 코드베이스 외부의 정보를 검색하는 도구입니다.
query에 자연어 검색어를 지정하면 검색 결과 요약과 관련 URL을 반환합니다.
활용 시점은 라이브러리 최신 버전 변경사항, 보안 취약점 CVE 정보, 베스트 프랙티스 동향, API와 SDK 공식 문서 참조 같은 상황입니다.
권장 패턴은 WebSearch로 URL을 식별한 다음 WebFetch로 정밀 분석하는 두 단계 흐름입니다.
검색 결과를 코드에 반영하기 전에는 사용자에게 한 번 확인을 받는 것이 좋습니다.
