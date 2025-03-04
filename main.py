from fastapi import FastAPI
from model.qa_model import qa_pipeline

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Question Answering API!"}

@app.post("/answer/")
def answer_question(question: str, context: str):
    answer = qa_pipeline(question=question, context=context)
    return {"question": question, "context": context, "answer": answer["answer"]}
