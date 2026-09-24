from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class QuestionRequest(BaseModel):
    question: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/questions")
def ask_question(data: QuestionRequest):
    return {
        "question": "O que é RAG?"
    }