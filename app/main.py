from fastapi import FastAPI

from app.models import ChatRequest
from app.memory import save_message
from app.memory import get_history
from app.coach import generate_response
from app.summarizer import summarize_history

app = FastAPI(
title="Conversational Care Engine",
version="1.0.0",
description="Multi-turn health coaching backend"
)

@app.get("/")
def home():
return {
"status": "running",
"version": "1.0.0"
}

@app.post("/chat")
def chat(request: ChatRequest):

```
save_message(
    request.user_id,
    request.message
)

history = get_history(
    request.user_id
)

reply = generate_response(
    request.message,
    history
)

summary = summarize_history(
    history
)

return {
    "reply": reply,
    "summary": summary,
    "history_length": len(history)
}
```
