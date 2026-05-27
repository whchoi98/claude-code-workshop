# Slide 113: 자주 묻는 질문

**Part 7: 디버깅과 트러블슈팅**

## Code Blocks

### FAQ

```
Q1. -p와 --print의 차이는?
A.  동일합니다. -p는 단축형, 둘 다 Headless 모드 활성화.

Q2. 응답을 파일로 저장하면 한국어가 깨져요.
A.  locale 문제. export LANG=ko_KR.UTF-8 또는
    LC_ALL=en_US.UTF-8 후 재시도.

Q3. JSON 응답에서 result가 잘려요.
A.  --max-tokens 기본 4096 한계. --max-tokens 8000 등으로 늘림.
    또는 응답이 진짜 그 길이로 끝났는지 stop_reason 확인.

Q4. 같은 프롬프트인데 매번 다른 결과가 나옵니다.
A.  Claude는 stochastic. 동일 응답이 필요하면 --temperature 0.
    실제로는 거의 같지만 약간 다를 수 있음.

Q5. 도구 호출 결과가 컨텍스트에 안 보여요.
A.  --debug로 tool_result 이벤트 확인.
    너무 큰 결과는 자동 trimming. 작은 부분만 요청.

Q6. CI에서 claude가 매번 새로 설치되어 느립니다.
A.  GitHub Actions cache 또는 사내 도커 이미지 베이크.
    한 번 빌드 후 재사용.

Q7. Windows에서 동작하나요?
A.  Windows 10/11에서 WSL2 권장. PowerShell도 가능하지만
    pipe 사용 시 인코딩 차이로 종종 문제.

Q8. 비용을 미리 알 수 있나요?
A.  --output-format json의 usage 필드에 토큰 수 포함.
    모델별 단가와 곱해 호출별 비용 계산. 또는 Anthropic Console.
```

## Speaker Notes

CLI 관련 자주 묻는 질문 8가지입니다.
첫째, -p와 --print의 차이는 없습니다.
동일한 옵션의 단축형과 긴 형식입니다.
둘째, 한국어 깨짐은 locale 문제입니다.
LANG 환경변수를 UTF-8로 설정합니다.
셋째, result가 잘리는 경우는 --max-tokens 한계입니다.
4096이 기본이고 8000 등으로 늘릴 수 있습니다.
넷째, 같은 프롬프트의 다른 결과는 모델의 stochastic 특성입니다.
--temperature 0으로 일관성을 높일 수 있지만 완전히 같지는 않을 수 있습니다.
다섯째, 도구 호출 결과가 안 보이는 경우는 --debug로 tool_result 이벤트를 확인합니다.
너무 큰 결과는 자동 trimming되니 작은 부분만 요청합니다.
여섯째, CI 설치 속도는 cache나 도커 이미지로 개선합니다.
일곱째, Windows는 WSL2가 권장됩니다.
PowerShell도 가능하지만 인코딩 문제가 종종 있습니다.
여덟째, 비용은 JSON 응답의 usage 필드와 모델 단가를 곱해 계산합니다.
Anthropic Console에서도 사용량을 확인할 수 있습니다.
