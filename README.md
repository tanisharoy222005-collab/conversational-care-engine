# Conversational Care Engine

A multi-turn health coaching backend built with FastAPI.

## Overview

The Conversational Care Engine provides condition-specific conversational support for:

* Diabetes
* Thyroid Disorders
* Obesity Management

The system maintains user session history and generates contextual responses based on previous interactions.

## Features

* Multi-turn conversation memory
* Condition-specific coaching responses
* FastAPI REST API
* Session management
* Extensible architecture

## Tech Stack

* Python
* FastAPI
* Pydantic
* Uvicorn

## Project Structure

```text
conversational-care-engine/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── app/
│   ├── main.py
│   ├── memory.py
│   ├── coach.py
│   └── models.py
│
├── tests/
│   └── test_chat.py
│
└── docs/
    └── architecture.md
```

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/conversational-care-engine.git

cd conversational-care-engine

pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Example API Request

POST /chat

```json
{
  "user_id": "user123",
  "message": "I have diabetes"
}
```

Response:

```json
{
  "reply": "Monitor blood sugar levels and maintain a balanced diet.",
  "history_length": 1
}
```

## Future Improvements

* Redis-based session storage
* OpenAI/Gemini integration
* Voice interface
* Authentication and authorization
* Analytics dashboard

## License

MIT License
