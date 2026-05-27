# Slide 116: Team library

**Part 7: CUSTOM SLASH COMMANDS**

## Code Blocks

### team library

```bash
# 1. 팀 표준 명령 저장소 구조
.claude/commands/
├── review-pr.md          # PR 리뷰
├── deploy.md             # 배포
├── debug-error.md        # 디버깅
├── sprint-summary.md     # 스프린트 요약
├── translate-doc.md      # 번역
├── new-feature.md        # 기능 추가 워크플로
├── postmortem.md         # 장애 회고
├── security-audit.md     # 보안 감사
└── README.md             # 명령 가이드

# 2. Git에 커밋
$ git add .claude/commands/
$ git commit -m "feat: standard team commands"
$ git push

# 3. 팀원은 clone 후 자동 사용 가능
$ git clone git@github.com:company/repo.git
$ cd repo
$ claude
> /            # 사용 가능한 명령 목록 자동 표시

# 4. 명령 가이드 README.md 권장
# Team Slash Commands

이 저장소는 사내 표준 슬래시 명령을 포함합니다.

## 사용 가능한 명령
- /review-pr <num>      - PR 종합 리뷰
- /deploy <env>         - 표준 배포 절차
- /debug-error <msg>    - 에러 분석
- /sprint-summary <date> - 스프린트 요약
- /translate-doc <file> <lang> - 문서 번역

## 새 명령 추가
.claude/commands/<name>.md 형식으로 작성하고 PR 제출
```

## Speaker Notes

팀 명령 라이브러리 구축 방법입니다.
팀 표준 명령 저장소 구조를 봅니다.
.claude/commands 디렉토리에 review-pr, deploy, debug-error, sprint-summary, translate-doc, new-feature, postmortem, security-audit 같은 명령들을 둡니다.
README.md도 함께 두어 명령 가이드를 제공합니다.
Git에 커밋해 공유합니다.
표준 git add, commit, push 절차를 사용합니다.
팀원은 clone 후 즉시 모든 명령을 사용할 수 있습니다.
claude 실행 후 슬래시만 입력하면 사용 가능한 명령 목록이 자동 표시됩니다.
README 가이드 작성을 권장합니다.
사용 가능한 모든 명령을 인자 형식과 함께 나열합니다.
새 명령 추가 방법도 안내합니다.
.claude/commands에 새 .md 파일을 작성하고 PR로 제출하는 패턴입니다.
팀 단위 자산화가 슬래시 명령의 가장 강력한 활용입니다.
