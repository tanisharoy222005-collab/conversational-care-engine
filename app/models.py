from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
user_id: str = Field(
...,
description="Unique identifier for the user"
)

```
message: str = Field(
    ...,
    min_length=1,
    max_length=1000,
    description="User message"
)
```

class ChatResponse(BaseModel):
reply: str

```
summary: str

history_length: int
```

class HealthStatusResponse(BaseModel):
status: str
version: str
