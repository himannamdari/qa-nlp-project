from transformers import pipeline

# Load pre-trained QA model
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
