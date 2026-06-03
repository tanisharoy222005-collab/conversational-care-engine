# Conversational Care Engine

Multi-turn health coaching backend built with FastAPI.

## Features

* Multi-turn conversations
* Session memory
* Diabetes support
* Thyroid support
* Obesity support
* Conversation summarization
* REST API

## Tech Stack

* Python
* FastAPI
* Pydantic
* Uvicorn

## Project Structure

conversational-care-engine/

├── README.md

├── requirements.txt

├── app/

│ ├── main.py

│ ├── models.py

│ ├── memory.py

│ ├── coach.py

│ └── summarizer.py

├── tests/

│ └── test_chat.py

├── docs/

│ └── architecture.md

└── screenshots/

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/conversational-care-engine.git

cd conversational-care-engine

pip install -r requirements.txt
```

## Run Application

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

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
  "reply": "For diabetes management, monitor blood sugar levels, maintain a balanced diet, and exercise regularly.",
  "summary": "I have diabetes",
  "history_length": 1
}
```

## Run Tests

```bash
pytest
```

## Future Roadmap

* Redis
* Twilio
* Whisper
* OpenAI Integration
* Analytics Dashboard

## License

MIT License
