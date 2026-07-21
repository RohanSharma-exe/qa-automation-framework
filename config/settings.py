from pathlib import Path
import os

BASE_URL = "https://www.saucedemo.com/"

TIMEOUT = 10

HEADLESS = os.getenv("HEADLESS", "True").lower() == "true"

ROOT = Path(__file__).resolve().parent.parent
SCREENSHOT_DIR = ROOT / "screenshots"
LOG_DIR = ROOT / "logs"
