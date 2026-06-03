from pathlib import Path

BASE_DIR = Path(**file**).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

HEALTH_GUIDELINES_FILE = DATA_DIR / "health_guidelines.csv"
SYMPTOM_DESCRIPTION_FILE = DATA_DIR / "symptom_Description.csv"
SYMPTOM_PRECAUTION_FILE = DATA_DIR / "symptom_precaution.csv"
SYMPTOM_SEVERITY_FILE = DATA_DIR / "Symptom-severity.csv"
DATASET_FILE = DATA_DIR / "dataset.csv"
