from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_home():

```
response = client.get("/")

assert response.status_code == 200

assert response.json()["status"] == "running"
```

def test_chat():

```
response = client.post(
    "/chat",
    json={
        "user_id": "user123",
        "message": "I have diabetes"
    }
)

assert response.status_code == 200

data = response.json()

assert "reply" in data

assert data["history_length"] >= 1
```
