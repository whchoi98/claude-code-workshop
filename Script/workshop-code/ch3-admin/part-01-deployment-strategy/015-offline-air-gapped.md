# Slide 15: Offline air-gapped

**Part 1: DEPLOYMENT STRATEGY**

## Code Blocks

### Air-gapped

```bash
# 시나리오: 보안 정책상 인터넷 차단된 사내망

# 1. 외부 망에서 패키지 수집 (이동 가능 미디어)
$ npm pack @anthropic-ai/claude-code
# claude-code-1.5.0.tgz 생성
$ docker save anthropic/claude-code:1.5.0 -o claude.tar
# tar 파일로 패키지화

# 2. 사내 미러 서버로 이전 (오프라인 매체)
USB 또는 보안 데이터 이전 채널 사용

# 3. 사내 미러에 등록
# Verdaccio
$ npm publish claude-code-1.5.0.tgz --registry https://internal-npm

# Docker
$ docker load -i claude.tar
$ docker tag anthropic/claude-code:1.5.0 registry.internal/claude:1.5.0
$ docker push registry.internal/claude:1.5.0

# 4. 사내 사용자는 사내 미러에서만 설치
# 외부 접근 없이 완전한 오프라인 동작

# 5. 단, Anthropic API 호출은 별도 게이트웨이 필요
# Bedrock VPC Endpoint 또는 PrivateLink 활용
```

## Speaker Notes

오프라인 또는 에어갭 환경의 배포 방법입니다.
보안 정책상 인터넷이 차단된 사내망에서의 배포입니다.
1단계 외부 망에서 패키지를 수집합니다.
npm pack 명령으로 .tgz 파일을 만들고 docker save 명령으로 tar 파일을 만듭니다.
2단계 USB 같은 보안 데이터 이전 채널을 통해 사내 미러 서버로 이전합니다.
3단계 사내 미러에 등록합니다.
Verdaccio에 npm publish를 하고 Docker는 docker load 후 사내 레지스트리에 push합니다.
4단계 사내 사용자는 사내 미러에서만 설치합니다.
외부 접근 없이 완전한 오프라인 동작이 가능합니다.
5단계 다만 Anthropic API 호출은 별도 게이트웨이가 필요합니다.
AWS Bedrock의 VPC Endpoint나 PrivateLink를 활용해 사내망 내에서 API에 접근합니다.
완전한 air-gapped 환경에서는 추가 아키텍처 설계가 필요합니다.
