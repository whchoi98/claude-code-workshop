# Slide 109: 세션 관리 --continue

**Part 5: QUICK START**

## Code Blocks

### continue

```bash
# 1. 가장 최근 세션 이어가기
$ claude -c
> [Continuing last session sess_abc123]
> [Loaded 23 messages]

# 또는 긴 형식
$ claude --continue

# 2. 디렉토리별 마지막 세션 자동 인식
$ cd ~/projects/my-app
$ claude -c
> [Continuing last session in this directory]

$ cd ~/projects/api-svc
$ claude -c
> [Continuing last session in this directory]

# 3. --continue와 --resume의 차이
# --continue (-c): 같은 디렉토리의 가장 최근 세션
# --resume (-r):   세션 ID 명시적 지정
```

## Speaker Notes

--continue 옵션은 직전 세션을 빠르게 이어가는 단축 명령입니다.
짧게 -c로도 사용할 수 있습니다.
현재 디렉토리에서 가장 최근에 사용한 세션이 자동으로 재개됩니다.
디렉토리별로 세션이 관리되므로 my-app 디렉토리에서는 my-app의 마지막 세션, api-svc 디렉토리에서는 api-svc의 마지막 세션이 자동으로 식별됩니다.
일상적인 작업 재개에는 -c가 가장 편리합니다.
--continue와 --resume의 차이는 명확합니다.
--continue는 같은 디렉토리의 가장 최근 세션을 자동 식별하고, --resume은 세션 ID를 명시적으로 지정할 때 사용합니다.
다른 디렉토리의 세션으로 전환하려면 --resume이 필요합니다.
