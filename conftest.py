import pytest
from datetime import datetime

from utils.driver_factory import get_driver
from config.settings import SCREENSHOT_DIR


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            SCREENSHOT_DIR.mkdir(exist_ok=True)

            filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"

            driver.save_screenshot(str(SCREENSHOT_DIR / filename))
