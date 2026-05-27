# Slide 159: /init Command

**Part 8: CLAUDE.md & MEMORY**

## Code Blocks

### /init

```bash
$ cd /path/to/your/project
$ claude
> /init

Claude가 프로젝트를 분석 중...
  ✓ package.json 분석 (TypeScript, React, Vite 감지)
  ✓ tsconfig.json 확인 (strict 모드)
  ✓ scripts 분석 (dev/build/test/lint)
  ✓ 디렉토리 구조 스캔 (src/, tests/, docs/)
  ✓ README.md 분석
  ✓ 주요 코드 패턴 분석 (Functional Components, Hooks)

다음 ./CLAUDE.md 초안을 작성했습니다:

# Project Overview
...

이 내용을 저장하시겠습니까? [Y/n]
```

## Speaker Notes

/init 명령은 CLAUDE.md를 처음 만들 때 유용한 도우미입니다.
프로젝트 디렉토리에서 claude 세션을 시작한 후 /init을 입력하면 Claude가 자동으로 package.json, tsconfig.json, scripts, 디렉토리 구조, README, 주요 코드 패턴까지 분석해 CLAUDE.md 초안을 작성해 줍니다.
빈 상태에서 시작하는 부담을 크게 줄여 주지만, 자동 생성된 내용을 그대로 두지 말고 팀 컨벤션이나 특수 사정을 직접 추가하는 것이 좋습니다.
