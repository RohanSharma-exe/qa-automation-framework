from pathlib import Path

BASE_URL = "https://www.saucedemo.com/"

TIMEOUT = 10

HEADLESS = False

ROOT = Path(__file__).resolve().parent.parent
SCREENSHOT_DIR = ROOT / "screenshots"
LOG_DIR = ROOT / "logs"
