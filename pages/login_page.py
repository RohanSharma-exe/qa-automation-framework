from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from config.settings import BASE_URL


class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "h3")

    def open(self):
        self.driver.get(BASE_URL)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN)

    def error_message(self):
        return self.get_text(self.ERROR)