from app.data_loader import load_health_guidelines

GUIDELINES = load_health_guidelines()

def generate_response(message, history):

```
text = message.lower()

for condition in GUIDELINES:

    if condition in text:

        recommendations = GUIDELINES[condition]

        return (
            f"{condition.title()} Advice: "
            f"{recommendations[0]}"
        )

if "diet" in text:
    return (
        "Maintaining a balanced diet and regular physical "
        "activity is beneficial for overall health."
    )

if "exercise" in text:
    return (
        "Aim for at least 30 minutes of moderate physical "
        "activity most days of the week."
    )

return (
    "I understand. Could you provide more information "
    "about your condition or symptoms?"
)
```
