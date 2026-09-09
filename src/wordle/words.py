import random

# DB가 없으니까 그냥 하드코딩
WORDS = [
    "crane", "slate", "audio", "raise", "stone",
    "pilot", "brick", "lemon", "juice", "mango",
    "ghost", "flame", "storm", "cloud", "river",
]


def pick_answer():
    return random.choice(WORDS)
