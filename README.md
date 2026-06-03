# Conversational Care Engine

A multi-turn healthcare coaching backend built with FastAPI.

## Features

* Multi-turn conversation memory
* Condition-specific coaching
* Dataset-driven recommendations
* Health guideline lookup
* REST API endpoints
* Conversation summarization

## Datasets Used

Located inside:

data/

Files:

* health_guidelines.csv
* dataset.csv
* Symptom-severity.csv
* symptom_Description.csv
* symptom_precaution.csv

## Tech Stack

* Python
* FastAPI
* Pydantic
* Uvicorn

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

Open:

http://127.0.0.1:8000/docs

## Example Request

POST /chat

```json
{
  "user_id": "user123",
  "message": "I have diabetes"
}
```

## Example Response

```json
{
  "reply": "Diabetes Advice: Monitor blood sugar regularly and follow a balanced diet",
  "summary": "I have diabetes",
  "history_length": 1
}
```

## Future Enhancements

* Redis session storage
* OpenAI integration
* Voice support
* Twilio integration
* Whisper speech-to-text
* Analytics dashboard
