def summarize_history(history):

```
if not history:
    return "No previous conversations."

recent_messages = history[-5:]

return " | ".join(recent_messages)
```
