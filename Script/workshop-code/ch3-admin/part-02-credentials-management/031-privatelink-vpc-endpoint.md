# Slide 31: PrivateLink/VPC Endpoint

**Part 2: CREDENTIALS MANAGEMENT**

## Code Blocks

### VPC Endpoint

```bash
# 시나리오: 모든 트래픽이 인터넷 거치지 않고 AWS 사설망 내에서

# 1. VPC Endpoint 생성 (Bedrock용)
# AWS Console 또는 CloudFormation

Resources:
  BedrockVPCEndpoint:
    Type: AWS::EC2::VPCEndpoint
    Properties:
      VpcId: !Ref MyVPC
      ServiceName: com.amazonaws.ap-northeast-2.bedrock-runtime
      VpcEndpointType: Interface
      SubnetIds:
        - !Ref PrivateSubnet1
        - !Ref PrivateSubnet2
      SecurityGroupIds:
        - !Ref BedrockEndpointSG
      PrivateDnsEnabled: true

# 2. DNS Resolution
# bedrock-runtime.ap-northeast-2.amazonaws.com
# → VPC 내부 IP로 자동 해석 (인터넷 우회)

# 3. 효과
- API 트래픽이 인터넷 거치지 않음
- 사내 네트워크 내에서만 통신
- 사내 보안 정책 컴플라이언스 만족
- VPC Flow Logs로 트래픽 감사
```

## Speaker Notes

PrivateLink와 VPC Endpoint 설정을 살펴봅니다.
모든 API 트래픽이 인터넷을 거치지 않고 AWS 사설망 내에서만 흐르도록 하는 설정입니다.
1단계 VPC Endpoint를 생성합니다.
Bedrock용 Interface 타입 엔드포인트입니다.
CloudFormation 예시처럼 ServiceName에 bedrock-runtime을 지정하고 사설 서브넷에 배치합니다.
보안 그룹으로 접근을 통제하고 PrivateDnsEnabled를 true로 설정합니다.
2단계 DNS Resolution입니다.
bedrock-runtime.ap-northeast-2.amazonaws.com 같은 도메인이 VPC 내부 IP로 자동 해석됩니다.
Claude Code는 별도 설정 변경 없이 자동으로 사설망 경로를 사용합니다.
3단계 효과는 명확합니다.
API 트래픽이 인터넷을 거치지 않습니다.
사내 네트워크 내에서만 통신하므로 사내 보안 정책 컴플라이언스를 만족합니다.
VPC Flow Logs로 트래픽 감사도 가능합니다.
