from langchain_community.llms import Ollama
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

llm = Ollama(model="llama3.1")

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define the model for the POST request body
class QuestionModel(BaseModel):
    question: str

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# POST request endpoint
@app.post("/ask")
async def ask_question(body: QuestionModel):
    result = llm.invoke(body.question)
    return {"received_question": result}

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
