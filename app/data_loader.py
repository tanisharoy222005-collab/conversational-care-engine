import csv

from app.config import HEALTH_GUIDELINES_FILE

def load_health_guidelines():

```
guidelines = {}

try:
    with open(
        HEALTH_GUIDELINES_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            condition = row["condition"].lower()

            recommendation = row["recommendation"]

            if condition not in guidelines:
                guidelines[condition] = []

            guidelines[condition].append(
                recommendation
            )

except Exception:
    pass

return guidelines
```
