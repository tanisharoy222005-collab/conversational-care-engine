def generate_response(message, history):

```
text = message.lower()

if "diabetes" in text:
    return (
        "For diabetes management, monitor blood sugar levels, "
        "maintain a balanced diet, and exercise regularly."
    )

if "thyroid" in text:
    return (
        "Regular medication, proper nutrition, and routine "
        "checkups are important for thyroid management."
    )

if "obesity" in text:
    return (
        "A healthy diet and consistent physical activity "
        "can support long-term weight management."
    )

return (
    "Can you tell me more about your symptoms or health goals?"
)
```
