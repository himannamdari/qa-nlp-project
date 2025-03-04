# Question Answering NLP API

This project is a simple Question Answering API built with FastAPI and Hugging Face Transformers.

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the API: `uvicorn app.main:app --reload`

## Usage

Send a POST request to `/answer/` with `question` and `context` parameters.

Example:
```json
{
    "question": "What is the capital of France?",
    "context": "France's capital is Paris."
}
```
Response:
```json
{
    "question": "What is the capital of France?",
    "context": "France's capital is Paris.",
    "answer": "Paris"
}
```
