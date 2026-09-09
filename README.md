# Wordle API

KHUDA AI Engineering 1주차 과제. FastAPI로 만든 Wordle 서버.

## 실행

```bash
uv sync
uv run uvicorn main:app --app-dir src --reload
```

http://127.0.0.1:8000/docs 에서 확인 가능

## 엔드포인트

- `GET /wordle/rules` : 단어 길이(5), 최대 시도 횟수(6)
- `POST /wordle/guess` : 단어 추측
- `GET /wordle/answer` : 정답 확인

### /guess 예시

```bash
curl -X POST localhost:8000/wordle/guess -H "content-type: application/json" -d '{"word":"slate","attempt":1}'
```

```json
{"word":"slate","result":["absent","correct","absent","absent","absent"],"is_correct":false,"attempts_left":5}
```

- correct: 글자랑 자리 다 맞음
- present: 글자는 있는데 자리가 다름
- absent: 없는 글자

attempt가 6 넘으면 400, 5글자 영어 아니면 422

## 무상태

서버가 시도 횟수를 저장하면 무상태 원칙에 어긋나서, 클라이언트가 요청할 때마다 `attempt`를 같이 보내는 식으로 함.
서버는 그 값만 보고 6 넘었는지 판단.

## 테스트

```bash
uv run pytest
```
