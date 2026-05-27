# Slide 99: Docker packaging

**Part 6: MCP 사내 서버 구축**

## Code Blocks

### Dockerfile

```bash
# Dockerfile
FROM node:20-alpine AS builder
WORKDIR /app

# 의존성 설치 (캐시 최적화)
COPY package*.json ./
RUN npm ci --only=production

# 빌드
COPY tsconfig.json ./
COPY src ./src
RUN npm install -D typescript && npx tsc

# 런타임 이미지
FROM node:20-alpine
WORKDIR /app

# 비root 사용자
RUN addgroup -S mcp && adduser -S mcp -G mcp

COPY --from=builder --chown=mcp:mcp /app/node_modules ./node_modules
COPY --from=builder --chown=mcp:mcp /app/dist ./dist
COPY --from=builder --chown=mcp:mcp /app/package.json ./

USER mcp

# 헬스체크
HEALTHCHECK --interval=30s --timeout=3s \
  CMD node -e "process.exit(0)" || exit 1

# 메타데이터
LABEL maintainer="platform@company.com"
LABEL version="1.0.0"

ENTRYPOINT ["node", "dist/index.js"]

# 빌드
# $ docker build -t registry.company.com/mcp/company-mcp:1.0.0 .
# 푸시
# $ docker push registry.company.com/mcp/company-mcp:1.0.0
```

## Speaker Notes

Docker로 컨테이너 패키징하는 방법입니다.
Multi-stage Dockerfile을 사용합니다.
빌더 단계에서 의존성 설치와 TypeScript 컴파일을 합니다.
package*.json을 먼저 복사해 npm ci로 production 의존성만 설치합니다.
캐시 최적화로 코드 변경 시 의존성 재설치가 불필요합니다.
빌드 단계에서 tsconfig와 src를 복사하고 tsc로 컴파일합니다.
런타임 이미지는 깨끗한 node:20-alpine을 베이스로 시작합니다.
비root 사용자 mcp를 생성합니다.
보안상 컨테이너 내부에서 root로 실행하지 않는 것이 권장됩니다.
빌더에서 node_modules와 dist를 복사하면서 chown으로 mcp 소유로 변경합니다.
USER mcp로 비root 사용자로 전환합니다.
HEALTHCHECK를 정의해 컨테이너 헬스 모니터링을 활성화합니다.
LABEL로 maintainer와 version을 명시합니다.
ENTRYPOINT는 node와 dist/index.js입니다.
빌드 후 사내 컨테이너 레지스트리에 푸시하면 모든 사용자가 동일한 버전을 받을 수 있습니다.
