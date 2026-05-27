# Slide 17: 첫 SDK 앱 예시

**Part 1: SDK 기본**

## Code Blocks

### first app

```python
#!/usr/bin/env python3
# pr_analyzer.py - PR 분석 CLI
import argparse
import subprocess
import sys
from anthropic import Anthropic, APIError

def get_pr_diff(pr_num: int) -> str:
    """gh CLI로 PR diff 가져옴"""
    result = subprocess.run(
        ["gh", "pr", "diff", str(pr_num)],
        capture_output=True, text=True, check=True,
    )
    return result.stdout

def analyze(pr_num: int) -> str:
    """Claude로 PR 분석"""
    diff = get_pr_diff(pr_num)

    client = Anthropic()
    try:
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=2000,
            system="당신은 시니어 코드 리뷰어입니다.",
            messages=[{
                "role": "user",
                "content": f"""다음 PR을 리뷰해 주세요:

{diff}

다음 관점으로:
1. 코드 품질
2. 보안
3. 테스트
"""
            }],
        )
        return message.content[0].text
    except APIError as e:
        print(f"Claude API 에러: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pr_num", type=int)
    args = parser.parse_args()

    review = analyze(args.pr_num)
    print(review)

if __name__ == "__main__":
    main()

# 사용
# $ python pr_analyzer.py 1234
```

## Speaker Notes

첫 SDK 앱 예시 PR 분석 CLI 도구입니다.
argparse로 CLI 인터페이스를 만듭니다.
get_pr_diff 함수는 gh CLI를 subprocess로 호출해 PR diff를 가져옵니다.
check=True로 실패 시 예외를 발생시킵니다.
analyze 함수에서 Claude를 호출합니다.
Anthropic 인스턴스를 만들고 messages.create로 호출합니다.
system 인자로 시니어 코드 리뷰어 역할을 부여합니다.
user 메시지에 f-string으로 diff를 포함해 동적으로 프롬프트를 구성합니다.
3가지 관점을 명시합니다.
APIError를 catch해서 stderr로 에러를 출력하고 exit 1로 종료합니다.
main 함수에서 argparse로 pr_num을 받고 analyze를 호출합니다.
결과를 print로 stdout에 출력합니다.
실행은 python pr_analyzer.py 1234처럼 PR 번호만 전달하면 됩니다.
실용적이고 즉시 활용 가능한 첫 SDK 앱입니다.
