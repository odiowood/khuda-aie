from pydantic import BaseModel, Field, field_validator

WORD_LENGTH = 5
MAX_ATTEMPTS = 6


class GuessRequest(BaseModel):
    word: str
    attempt: int = Field(ge=1)  # 몇 번째 시도인지. 서버가 안 세니까 클라이언트가 보내줌

    @field_validator("word")
    @classmethod
    def check_word(cls, word: str):
        word = word.lower()
        if len(word) != WORD_LENGTH:
            raise ValueError(f"{WORD_LENGTH}글자 단어만 가능합니다")
        if not word.isalpha():
            raise ValueError("영어 알파벳만 입력하세요")
        return word


class GuessResponse(BaseModel):
    word: str
    result: list[str]  # ["correct", "present", "absent", ...]
    is_correct: bool
    attempts_left: int


class AnswerResponse(BaseModel):
    answer: str


class RulesResponse(BaseModel):
    word_length: int
    max_attempts: int
