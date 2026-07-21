from pages.login_page import LoginPage


def test_valid_login(driver):
    page = LoginPage(driver)

    page.open()

    page.login(
        "standard_user",
        "secret_sauce",
    )

    assert "inventory" in driver.current_url


def test_invalid_login(driver):
    page = LoginPage(driver)

    page.open()

    page.login(
        "locked_out_user",
        "wrong_password",
    )

    assert "Username and password do not match" in page.error_message()