# 추측 단어를 정답이랑 비교해서 자리별로 correct / present / absent 반환


def check_guess(answer: str, guess: str) -> list[str]:
    result = ["absent"] * 5
    remaining = list(answer)  # 아직 안 쓴 정답 글자들

    # 1. 자리까지 맞는 글자 먼저 처리
    for i in range(5):
        if guess[i] == answer[i]:
            result[i] = "correct"
            remaining.remove(guess[i])

    # 2. 나머지 중에 정답에 남아있는 글자면 present
    # (같은 글자가 여러 번 나오면 정답에 있는 개수만큼만 present로 표시됨)
    for i in range(5):
        if result[i] == "correct":
            continue
        if guess[i] in remaining:
            result[i] = "present"
            remaining.remove(guess[i])

    return result
