# Slide 8: Internal mirror setup

**Part 1: DEPLOYMENT STRATEGY**

## Code Blocks

### Verdaccio

```bash
# 1. Verdaccio 사내 미러 구축 (간단한 옵션)
$ npm install -g verdaccio
$ verdaccio --listen 4873

# 2. config.yaml에서 anthropic 패키지 캐싱
storage: ./storage
packages:
  '@anthropic-ai/*':
    access: $authenticated
    publish: $authenticated
    proxy: npmjs    # 첫 요청 시 외부에서 캐싱
  '**':
    access: $authenticated
    publish: $authenticated
    proxy: npmjs

# 3. 사내 PC에 npm 레지스트리 설정 (GPO/Ansible로 일괄)
$ npm config set registry https://npm.internal.company.com

# 4. 설치 시 사내 미러에서 가져옴
$ npm install -g @anthropic-ai/claude-code

# 5. 보안 효과
- 외부 npm 직접 접근 불필요
- 사내 미러에서 보안 스캔 후 제공
- 버전 회수(yank) 시 즉시 차단 가능
```

## Speaker Notes

사내 npm 미러 운영 방법을 살펴봅니다.
외부 의존성을 차단하고 통제하는 핵심 패턴입니다.
1단계 Verdaccio를 사내에 설치합니다.
npm으로 글로벌 설치 후 4873 포트로 실행합니다.
2단계 config.yaml에서 anthropic 패키지를 캐싱하도록 설정합니다.
@anthropic-ai 네임스페이스의 패키지는 인증된 사용자만 접근하도록 합니다.
첫 요청 시 외부 npm에서 자동으로 캐싱됩니다.
3단계 사내 PC들의 npm registry를 사내 미러로 설정합니다.
GPO나 Ansible로 일괄 배포합니다.
4단계 사내 미러에서 Claude Code를 설치합니다.
5단계 보안 효과를 봅니다.
외부 npm 직접 접근이 불필요하고 사내 미러에서 보안 스캔 후 제공할 수 있습니다.
버전 회수가 발생하면 즉시 차단도 가능합니다.
