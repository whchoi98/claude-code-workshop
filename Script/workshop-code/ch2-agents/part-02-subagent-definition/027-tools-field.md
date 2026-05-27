# Slide 27: tools field

**Part 2: SUBAGENT 정의 방법**

## Code Blocks

### tools patterns

```bash
# 1. 도구 이름만 (해당 도구 전체 허용)
tools: Read, Grep, Glob, Edit, Write

# 2. Bash는 명령 패턴으로 좁히기
tools: Read, Bash(npm test:*), Bash(git diff:*), Bash(git status)

# 3. 패턴 와일드카드
tools: Read(**/*.md), Edit(docs/**)

# 4. 비어 있으면 → 메인의 모든 도구 상속 (지양)
# tools 필드 생략 시 위험

# 5. 빈 문자열 → 도구 없음 (분석 전용 에이전트)
tools: ""
```

## Speaker Notes

tools 필드 작성법을 자세히 다룹니다.
몇 가지 패턴이 있습니다.
첫 번째 방식은 도구 이름만 콤마로 구분하는 것입니다.
해당 도구 전체를 허용합니다.
두 번째 방식은 Bash 같은 강력한 도구를 명령 패턴으로 좁히는 것입니다.
Bash 괄호 안에 허용할 명령 패턴을 명시합니다.
npm test 또는 git diff만 허용한다는 식으로 좁힐 수 있습니다.
세 번째 방식은 패턴 와일드카드입니다.
Read나 Edit에 경로 글롭을 적용해 특정 디렉토리나 파일 확장자에만 접근하도록 제한합니다.
네 번째로 tools 필드를 생략하면 메인의 모든 도구를 상속받습니다.
위험하므로 지양합니다.
다섯 번째로 빈 문자열을 주면 도구를 전혀 사용할 수 없습니다.
분석과 추론만 하는 에이전트에 적합합니다.
