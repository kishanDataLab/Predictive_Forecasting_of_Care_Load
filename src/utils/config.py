from pathlib import Path


# --------------------------------------------------
# PROJECT PATH
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]


# --------------------------------------------------
# DATA DIRECTORIES
# --------------------------------------------------

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"


# --------------------------------------------------
# PROJECT DIRECTORIES
# --------------------------------------------------

IMAGE_DIR = PROJECT_ROOT / "images"

RESULTS_DIR = PROJECT_ROOT / "results"

MODELS_DIR = PROJECT_ROOT / "models"

REPORTS_DIR = PROJECT_ROOT / "reports"


# --------------------------------------------------
# FORECASTING SETTINGS
# --------------------------------------------------

TARGET_COLUMN = "Children in HHS Care"

FORECAST_HORIZON = 12

RANDOM_STATE = 42