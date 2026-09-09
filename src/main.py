from fastapi import FastAPI

from wordle import wordle_router

app = FastAPI(title="Wordle API")
app.include_router(wordle_router)
