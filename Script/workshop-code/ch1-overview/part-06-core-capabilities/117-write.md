# Slide 117: Write

**Part 6: CORE CAPABILITIES**

## Code Blocks

### Write tool

```python
# Write 도구
Write(
  file_path: "src/lib/logger.ts",
  content: `import pino from 'pino';

export const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  redact: ['password', 'token', 'apiKey'],
});

export type Logger = typeof logger;`
)

# 주요 규칙
- file_path는 존재하지 않아야 함 (있으면 Edit 사용)
- 부모 디렉토리는 자동 생성됨
- 줄 끝 개행 자동 처리
- 파일 권한은 기본 644 (실행파일은 chmod 별도)

# Write vs Edit
- Write: 새 파일 생성 전용
- Edit: 기존 파일 수정 (Read 후 사용)
```

## Speaker Notes

Write 도구는 신규 파일을 생성합니다.
file_path와 content를 지정하면 해당 경로에 파일이 만들어집니다.
주요 규칙은 file_path가 존재하지 않아야 한다는 점인데, 이미 있는 파일을 덮어쓰려고 하면 오류가 발생하며 대신 Edit을 사용해야 합니다.
부모 디렉토리는 자동으로 생성되므로 mkdir -p를 별도로 실행할 필요가 없습니다.
줄 끝 개행 처리는 자동으로 됩니다.
파일 권한은 기본 644이며, 실행 파일이 필요한 경우 Bash 도구로 chmod를 별도 실행합니다.
Write와 Edit의 구분은 명확합니다.
신규 파일은 Write, 기존 파일 수정은 Read 후 Edit이라는 규칙을 기억하시기 바랍니다.
