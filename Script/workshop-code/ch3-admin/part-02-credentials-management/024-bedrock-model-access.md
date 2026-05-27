# Slide 24: Bedrock model access

**Part 2: CREDENTIALS MANAGEMENT**

## Code Blocks

### Model Access

```bash
# 1. AWS Console → Bedrock → Model access
# Anthropic 모델 패밀리 액세스 요청
# - Claude Sonnet 4.5
# - Claude Opus 4.5
# - Claude Haiku 4.5

# 신청 시 입력 항목
- 회사명 / 사용 사례 / 데이터 처리 방식
- 보통 1시간 이내 자동 승인 (일부 모델 별도)

# 2. 리전 선택 (한국 권장)
- ap-northeast-2 (Seoul) - 모델 가용성 확인
- us-east-1 (Virginia) - 가장 빠른 모델 출시
- us-west-2 (Oregon) - 두 번째 빠른 출시

# 3. 액세스 후 확인
$ aws bedrock list-foundation-models \
    --region ap-northeast-2 \
    --by-provider anthropic

# 4. IAM 정책 준비 (다음 슬라이드)
```

## Speaker Notes

Bedrock 모델 액세스 신청 절차입니다.
1단계 AWS Console에서 Bedrock 서비스의 Model access 메뉴로 이동합니다.
Anthropic 모델 패밀리, 즉 Claude Sonnet 4.5, Opus 4.5, Haiku 4.5에 대한 액세스를 요청합니다.
신청 시 회사명, 사용 사례, 데이터 처리 방식을 입력합니다.
보통 1시간 이내 자동 승인되며 일부 모델은 별도 검토가 있을 수 있습니다.
2단계 리전을 선택합니다.
한국은 ap-northeast-2 Seoul 리전에서 모델 가용성을 확인합니다.
us-east-1 Virginia가 가장 빠르게 새 모델이 출시되고 us-west-2 Oregon이 두 번째입니다.
3단계 액세스 후 AWS CLI로 사용 가능한 모델을 확인합니다.
4단계 IAM 정책을 준비합니다.
다음 슬라이드에서 상세히 다룹니다.
