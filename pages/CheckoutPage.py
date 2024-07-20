from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CheckoutPage(BasePage):

    first_name_field = (By.NAME, "firstName")
    last_name_field = (By.NAME, "lastName")
    postal_code_field = (By.ID, "postal-code")
    continue_field = (By.ID, "continue")
    finish_field = (By.ID, "finish")
    card_field = (By.XPATH, "//div[@class='summary_value_label']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, first_name_text):
        self.send_keys(first_name_text, *self.first_name_field)

    def enter_last_name(self, last_name_text):
        self.send_keys(last_name_text, *self.last_name_field)

    def enter_postal_code(self, postal_code_text):
        self.send_keys(postal_code_text,*self.postal_code_field)

    def continue_button(self):
        self.click_element(*self.continue_field)

    def finish_button(self):
        self.click_element(*self.finish_field)

