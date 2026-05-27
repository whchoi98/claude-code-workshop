# Slide 95: Lib upgrade scenario

**Part 8: PATTERN 5 / MIGRATION BOT**

## Code Blocks

### axios upgrade

```bash
# 사용자 요청
"axios를 v0.27에서 v1.6으로 업그레이드하고 변경 사항을 모두 적용해 줘"

# migration-bot의 작업
1. package.json 업데이트: axios ^1.6.0
2. Grep "import axios" → 23개 파일 식별
3. 변경 패턴 인식:
   - axios.create(config) → axios.create(config) (변화 없음)
   - response.data.error 처리 변경
   - timeout 옵션 동작 변화

4. 시범 5개 파일 변경 → npm test 통과
5. 사용자 검토용 git diff 출력
6. 동의 → 나머지 18개 파일 변경
7. 최종 npm test 전체 통과 → 보고

# 결과 보고
"23개 파일 변경 완료. 모든 테스트 통과.
 PR 생성 권장: feat/upgrade-axios-v1"
```

## Speaker Notes

시나리오 1은 라이브러리 업그레이드입니다.
saxios를 v0.27에서 v1.6으로 업그레이드하는 시나리오입니다.
migration-bot의 작업을 단계별로 봅니다.
1단계 package.json을 업데이트해 axios 버전을 ^1.6.0으로 변경합니다.
2단계 Grep으로 import axios 패턴을 검색해 23개 파일을 식별합니다.
3단계 변경 패턴을 인식합니다.
axios.create는 변화가 없지만 response.data.error 처리 방식과 timeout 옵션 동작이 변했음을 파악합니다.
4단계 시범으로 5개 파일을 먼저 변경하고 npm test로 통과를 확인합니다.
5단계 사용자 검토용으로 git diff를 출력합니다.
6단계 사용자 동의 후 나머지 18개 파일을 변경합니다.
7단계 최종 npm test 전체 통과를 확인하고 보고합니다.
결과는 23개 파일 변경 완료와 PR 생성 권장 메시지입니다.
