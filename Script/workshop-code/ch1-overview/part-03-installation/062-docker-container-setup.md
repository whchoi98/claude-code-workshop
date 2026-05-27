# Slide 62: Docker Container Setup

**Part 3: INSTALLATION**

## Code Blocks

### Docker

```bash
# 1. 공식 이미지 풀
docker pull anthropic/claude-code:latest

# 2. 단일 명령 실행 (헤드리스)
docker run --rm -it \
  -v $(pwd):/workspace \
  -e ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY" \
  anthropic/claude-code:latest \
  -p "package.json에서 outdated 패키지를 알려 주세요"

# 3. 대화형 세션
docker run --rm -it \
  -v $(pwd):/workspace \
  -v $HOME/.claude:/root/.claude \
  -e ANTHROPIC_API_KEY \
  anthropic/claude-code:latest

# 4. docker-compose.yml 활용
docker compose up claude-code
```

## Speaker Notes

Docker 환경에서의 사용입니다.
Anthropic이 anthropic/claude-code 공식 이미지를 제공합니다.
1단계 docker pull로 이미지를 받습니다.
2단계 헤드리스 한 번 실행 시에는 현재 디렉토리를 /workspace로 마운트하고 ANTHROPIC_API_KEY를 환경변수로 주입한 후 -p 플래그로 프롬프트를 전달합니다.
--rm 플래그는 컨테이너 종료 후 자동 정리, -it는 인터랙티브 터미널을 의미합니다.
3단계 대화형 세션을 원할 경우 $HOME/.claude 디렉토리도 마운트해 세션과 설정이 호스트에 영구 저장되도록 합니다.
4단계 docker-compose.yml로 정의하면 docker compose up 명령으로 반복 실행이 편해집니다.
컨테이너 방식은 CI/CD나 격리가 중요한 환경에서 가장 안정적입니다.
