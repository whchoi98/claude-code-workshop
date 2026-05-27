# Slide 50: 실전 / 파일 시스템 도구

**Part 3: TOOL USE**

## Code Blocks

### fs tools

```python
from pathlib import Path

# 안전을 위해 허용 디렉토리 제한
ALLOWED_DIRS = [Path("/workspace"), Path("/tmp")]

def is_safe_path(path_str: str) -> Path | None:
    p = Path(path_str).resolve()
    for allowed in ALLOWED_DIRS:
        if str(p).startswith(str(allowed.resolve())):
            return p
    return None

TOOLS = [
    {
        "name": "read_file",
        "description": "파일 읽기. 허용 디렉토리만.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "max_bytes": {"type": "integer", "default": 100_000},
            },
            "required": ["path"],
        },
    },
    {
        "name": "write_file",
        "description": "파일 쓰기. 허용 디렉토리만.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "content": {"type": "string"},
            },
            "required": ["path", "content"],
        },
    },
    {
        "name": "list_files",
        "description": "디렉토리 목록",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "pattern": {"type": "string", "description": "glob pattern"},
            },
            "required": ["path"],
        },
    },
]

def read_file(path: str, max_bytes: int = 100_000) -> str:
    p = is_safe_path(path)
    if not p: return "Error: Path not allowed"
    if not p.is_file(): return "Error: Not a file"
    data = p.read_bytes()[:max_bytes]
    return data.decode("utf-8", errors="replace")

def write_file(path: str, content: str) -> str:
    p = is_safe_path(path)
    if not p: return "Error: Path not allowed"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)
    return f"Wrote {len(content)} chars to {p}"

def list_files(path: str, pattern: str = "*") -> list:
    p = is_safe_path(path)
    if not p: return ["Error: Path not allowed"]
    return [str(f.relative_to(p)) for f in p.rglob(pattern)][:100]
```

## Speaker Notes

실전 예시 파일 시스템 도구입니다.
안전이 가장 중요합니다.
ALLOWED_DIRS로 허용 디렉토리를 명시 화이트리스트로 제한합니다.
is_safe_path 함수에서 모든 경로를 resolve해서 허용 디렉토리 내부인지 검증합니다.
도구 3개를 정의합니다.
read_file은 path와 max_bytes를 받아 파일을 읽습니다.
write_file은 path와 content를 받아 파일을 씁니다.
list_files는 path와 pattern을 받아 파일 목록을 반환합니다.
read_file 구현은 안전 경로 검증 후 max_bytes만큼만 읽습니다.
토큰 폭증을 방지하는 안전망입니다.
UTF-8 디코딩 시 에러는 replace로 처리합니다.
write_file은 부모 디렉토리를 자동 생성하고 쓰기를 수행합니다.
list_files는 rglob으로 패턴 매칭하고 최대 100개로 제한합니다.
이 도구들로 Claude가 워크스페이스에서 파일을 안전하게 다룰 수 있습니다.
위험한 경로 접근은 자동 차단됩니다.
실제 프로덕션에서는 Docker나 chroot 같은 추가 격리가 권장됩니다.
