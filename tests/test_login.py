import pytest

from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username,password,success",
    [
        ("standard_user", "secret_sauce", True),
        ("locked_out_user", "secret_sauce", False),
        ("", "secret_sauce", False),
        ("standard_user", "", False),
        ("", "", False),
        ("wrong", "wrong", False),
    ],
)
def test_login(driver, username, password, success):
    page = LoginPage(driver)

    page.open()

    page.login(username, password)

    if success:
        assert "inventory" in driver.current_url
    else:
        assert "inventory" not in driver.current_url
