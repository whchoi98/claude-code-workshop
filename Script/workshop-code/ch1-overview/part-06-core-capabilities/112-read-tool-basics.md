# Slide 112: Read tool basics

**Part 6: CORE CAPABILITIES**

## Code Blocks

### Read tool

```bash
# Read 도구 - Claude가 자동으로 호출
Read(file_path: "src/services/payment.js")

# 줄 범위 지정 (큰 파일)
Read(file_path: "src/app.js", offset: 100, limit: 50)
# → 100번째 줄부터 50줄 읽기

# 기본 동작
- 절대 경로 권장 (상대 경로도 지원)
- 자동 줄 번호 표시 (cat -n 형식)
- 큰 파일: 기본 2,000줄까지 읽음 (offset/limit로 조정)
- 빈 파일/존재하지 않는 파일: 명시적 오류 반환

# 사용 시점
- 파일 수정 전 반드시 Read로 현재 내용 확인 (필수)
- Grep으로 찾은 위치를 정확히 읽을 때
- README/설정 파일/스택 트레이스 파일 분석 시
```

## Speaker Notes

Read 도구는 가장 기본적이고 가장 자주 사용되는 도구입니다.
절대 경로로 파일 경로를 받으며, 자동으로 cat -n 형식의 줄 번호를 표시해 줍니다.
큰 파일은 기본 2000줄까지 읽고, offset과 limit으로 범위를 지정할 수 있습니다.
가장 중요한 규칙은 파일 수정 전 반드시 Read로 현재 내용을 확인해야 한다는 점입니다.
Edit 도구는 Read 없이 호출되면 오류를 반환합니다.
안전 장치로, Claude가 가정에 기반해 잘못된 수정을 가하는 것을 방지합니다.
사용 시점은 Grep으로 찾은 위치 확인, 설정 파일 분석, 스택 트레이스 파일 분석 등입니다.
