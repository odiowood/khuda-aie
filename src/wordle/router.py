from fastapi import APIRouter, HTTPException

from .logic import check_guess
from .schemas import (
    MAX_ATTEMPTS,
    WORD_LENGTH,
    AnswerResponse,
    GuessRequest,
    GuessResponse,
    RulesResponse,
)
from .words import pick_answer

wordle_router = APIRouter(prefix="/wordle", tags=["wordle"])

# 서버 켤 때 한번 정답 뽑기
ANSWER = pick_answer()


@wordle_router.get("/rules")
def get_rules() -> RulesResponse:
    """단어 길이랑 최대 시도 횟수를 알려준다."""
    return RulesResponse(word_length=WORD_LENGTH, max_attempts=MAX_ATTEMPTS)


@wordle_router.get("/answer")
def get_answer() -> AnswerResponse:
    """정답 확인용"""
    return AnswerResponse(answer=ANSWER)


@wordle_router.post("/guess")
def post_guess(guess: GuessRequest) -> GuessResponse:
    """단어 추측 (attempt가 6 넘으면 400)"""
    # 무상태: 서버는 몇 번 시도했는지 기억 안한다. 요청에 들어있는 attempt만 확인한다.
    if guess.attempt > MAX_ATTEMPTS:
        raise HTTPException(status_code=400, detail="시도 횟수 6번 초과! GAME OVER")

    result = check_guess(ANSWER, guess.word)

    return GuessResponse(
        word=guess.word,
        result=result,
        is_correct=(guess.word == ANSWER),
        attempts_left=MAX_ATTEMPTS - guess.attempt,
    )
