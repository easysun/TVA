from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="TVA Time Authority Backend",
    description="API service to validate submitted historical versions using AI",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # adjust for production
    allow_methods=["*"],
    allow_headers=["*"],
)

class HistorySubmission(BaseModel):
    content: str
    version: str

@app.post("/validate")
async def validate(submission: HistorySubmission):
    if not openai.api_key:
        raise HTTPException(status_code=500, detail="OpenAI API key not configured")
    prompt = (
        f"Validate the accuracy and authenticity of the following historical version:\n"
        f"Version: {submission.version}\n"
        f"Content: {submission.content}\n"
    )
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.0,
    )
    return {"validation": response.choices[0].text.strip()}