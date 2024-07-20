from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.BasePage import BasePage

class LoginPage(BasePage):

    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    submit_field = (By.ID, "login-button")
    is_login_success_field = (By.XPATH, '//span[text()="Products"]')

    def __init__(self, driver):
        super().__init__(driver)

    def enter_mail_id(self, email_text):
        self.send_keys(email_text, *self.username_field)

    def enter_password(self, password_text):
        self.send_keys(password_text, *self.password_field)

    def clicking_element(self):
        self.click_element(*self.submit_field)

    def is_login_successful(self):
        return "https://www.saucedemo.com/inventory.html"






