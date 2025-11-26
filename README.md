# Python Executor

HTTP API를 통해 Python 코드를 실행하는 서비스

## 엔드포인트
- GET / : 서비스 정보
- POST /execute : Python 코드 실행
- GET /info : Python 환경 정보

## 사용 예시
```bash
curl -X POST http://host:port/execute \
  -H "Content-Type: application/json" \
  -d '{"code": "print(1+1)"}'
```
