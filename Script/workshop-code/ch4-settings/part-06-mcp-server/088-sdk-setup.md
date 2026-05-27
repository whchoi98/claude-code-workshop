# Slide 88: SDK setup

**Part 6: MCP 사내 서버 구축**

## Code Blocks

### setup

```bash
# 1. 새 프로젝트 디렉토리 생성
$ mkdir company-mcp-server
$ cd company-mcp-server
$ npm init -y

# 2. MCP SDK와 의존성 설치
$ npm install @modelcontextprotocol/sdk
$ npm install -D typescript @types/node tsx
$ npm install zod   # 입력 검증용

# 3. tsconfig.json 생성
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "Node16",
    "esModuleInterop": true,
    "strict": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "declaration": true
  },
  "include": ["src/**/*"]
}

# 4. package.json scripts
{
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "dev": "tsx watch src/index.ts"
  },
  "bin": {
    "company-mcp": "./dist/index.js"
  }
}

# 5. 디렉토리 구조
src/
├── index.ts          # 진입점
├── server.ts         # MCP 서버 설정
├── tools/            # 도구 구현
├── resources/        # 리소스 구현
└── auth.ts           # 인증 로직
```

## Speaker Notes

TypeScript SDK 셋업을 살펴봅니다.
1단계 새 프로젝트 디렉토리를 만들고 npm init으로 초기화합니다.
2단계 MCP SDK와 의존성을 설치합니다.
@modelcontextprotocol/sdk가 핵심이고, typescript와 tsx를 dev dependency로 설치합니다.
zod는 입력 런타임 검증에 사용합니다.
3단계 tsconfig.json을 생성합니다.
target을 ES2022로, module과 moduleResolution을 Node16으로 설정합니다.
strict 모드를 활성화해 타입 안전성을 확보합니다.
outDir은 dist, rootDir은 src로 분리합니다.
4단계 package.json의 scripts를 정의합니다.
build로 컴파일, start로 실행, dev로 watch 모드 개발이 가능합니다.
bin 필드에 등록하면 npm install -g 후 명령처럼 실행할 수 있습니다.
5단계 디렉토리 구조를 정리합니다.
index.ts는 진입점, server.ts는 MCP 설정, tools와 resources는 구현, auth.ts는 인증입니다.
