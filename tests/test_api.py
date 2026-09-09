from fastapi.testclient import TestClient

import wordle.router as router
from main import app

router.ANSWER = "crane"  # 테스트에서는 정답 고정
client = TestClient(app)


def test_rules():
    res = client.get("/wordle/rules")
    assert res.json() == {"word_length": 5, "max_attempts": 6}


def test_answer():
    res = client.get("/wordle/answer")
    assert res.json()["answer"] == "crane"


def test_guess():
    res = client.post("/wordle/guess", json={"word": "crate", "attempt": 1})
    assert res.status_code == 200
    assert res.json()["result"] == ["correct", "correct", "correct", "absent", "correct"]
    assert res.json()["attempts_left"] == 5


def test_guess_correct():
    res = client.post("/wordle/guess", json={"word": "crane", "attempt": 2})
    assert res.json()["is_correct"] is True


def test_too_many_attempts():
    res = client.post("/wordle/guess", json={"word": "crate", "attempt": 7})
    assert res.status_code == 400


def test_wrong_length():
    res = client.post("/wordle/guess", json={"word": "cat", "attempt": 1})
    assert res.status_code == 422
