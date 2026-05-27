# Slide 113: Lab 1 / Internal mirror

**Part 9: RECAP & 3 LABS**

## Code Blocks

### Lab 1 steps

```bash
# 1. Verdaccio 설치 (Lab VM에서)
$ npm install -g verdaccio
$ verdaccio --listen 4873 &

# 2. config 수정 (~/.config/verdaccio/config.yaml)
packages:
  '@anthropic-ai/*':
    access: $all
    publish: $authenticated
    proxy: npmjs
  '**':
    proxy: npmjs

# 3. 클라이언트 npm registry 설정
$ npm config set registry http://localhost:4873

# 4. Claude Code 설치 (미러 경유)
$ npm install -g @anthropic-ai/claude-code

# 5. 검증
$ claude --version
$ ls -la \
  ~/.config/verdaccio/storage/@anthropic-ai/claude-code/
# 캐싱 확인
```

## Speaker Notes

Lab 1은 사내 npm 미러 구축 실습입니다.
약 30분 소요됩니다.
5단계로 진행됩니다.
1단계 Verdaccio를 npm으로 글로벌 설치하고 4873 포트로 백그라운드 실행합니다.
2단계 config.yaml에서 @anthropic-ai 네임스페이스의 프록시 설정을 추가합니다.
access를 모두에게 허용하고 publish는 인증된 사용자만 가능하게 합니다.
proxy를 npmjs로 설정해 외부 npm을 캐싱합니다.
3단계 클라이언트 npm registry를 사내 미러로 변경합니다.
localhost:4873을 가리키도록 npm config를 설정합니다.
4단계 Claude Code를 미러 경유로 설치합니다.
첫 설치 시 외부 npm에서 자동 캐싱됩니다.
5단계 검증입니다.
claude --version으로 설치 확인하고 Verdaccio storage 디렉토리에 캐싱된 파일이 있는지 확인합니다.
이후로는 오프라인 환경에서도 동일 버전 설치가 가능합니다.
