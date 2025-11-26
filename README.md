# Python Executor

HTTP API 및 SSH를 통해 Python 코드를 실행하는 서비스

## 접속 정보
- SSH: root / python123
- API: 5000 포트

## API 엔드포인트
- GET / : 서비스 정보
- POST /execute : Python 코드 실행
- GET /info : Python 환경 정보

## 사용 예시
```bash
# SSH 접속
ssh root@host -p {ssh_port}

# API 코드 실행
curl -X POST http://host:port/execute \
  -H "Content-Type: application/json" \
  -d '{"code": "print(1+1)"}'
```
