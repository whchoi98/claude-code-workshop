# Slide 101: Deployment to Kubernetes

**Part 6: MCP 사내 서버 구축**

## Code Blocks

### k8s yaml

```bash
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: company-mcp-server
  namespace: platform
spec:
  replicas: 3
  selector:
    matchLabels: { app: company-mcp }
  template:
    metadata:
      labels: { app: company-mcp }
    spec:
      containers:
      - name: mcp
        image: registry.company.com/mcp/company-mcp:1.0.0
        ports: [{ containerPort: 8080 }]
        env:
        - name: JWT_SECRET
          valueFrom: { secretKeyRef: { name: mcp-secrets, key: jwt }}
        - name: HR_TOKEN
          valueFrom: { secretKeyRef: { name: mcp-secrets, key: hr }}
        resources:
          requests: { memory: "128Mi", cpu: "100m" }
          limits:   { memory: "512Mi", cpu: "500m" }
        livenessProbe:
          httpGet: { path: /health, port: 8080 }
          periodSeconds: 30
---
apiVersion: v1
kind: Service
metadata:
  name: company-mcp
  namespace: platform
spec:
  selector: { app: company-mcp }
  ports:
  - port: 443
    targetPort: 8080
  type: ClusterIP
---
# Ingress로 외부 노출
# 사용자: https://mcp.company.com/sse 접근
```

## Speaker Notes

Kubernetes 배포 매니페스트입니다.
Deployment 리소스에 3 replicas로 고가용성을 확보합니다.
image는 사내 레지스트리의 빌드한 이미지를 가리킵니다.
환경변수로 JWT_SECRET과 HR_TOKEN을 secretKeyRef로 주입합니다.
사내 Secrets에서 토큰을 가져오므로 매니페스트에 평문이 없습니다.
resources로 memory와 cpu의 requests와 limits를 명시합니다.
128Mi 시작, 512Mi 제한으로 가벼운 서비스에 적절한 크기입니다.
livenessProbe로 /health 경로를 30초마다 체크합니다.
실패 시 컨테이너가 자동 재시작됩니다.
Service 리소스로 클러스터 내부에서 접근 가능하게 합니다.
ClusterIP 타입으로 443 포트를 8080으로 매핑합니다.
Ingress 리소스를 추가하면 외부 노출도 가능합니다.
사용자는 https://mcp.company.com/sse 같은 URL로 접근합니다.
Kubernetes의 모든 기능 자동 복구, 롤링 업데이트, 스케일링을 활용할 수 있습니다.
