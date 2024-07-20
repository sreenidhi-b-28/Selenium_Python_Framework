from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class ProductPage(BasePage):

    cart_icon_field = (By.CLASS_NAME,"shopping_cart_link")
    checkout_field = (By.ID, "checkout")

    def __init__(self,driver):
        super().__init__(driver)
    def select_product(self, product_name):
        product_field = (By.XPATH, f"//button[contains(@name,'{product_name}')]")
        self.click_element(*product_field)

    def click_on_cart(self):
        self.click_element(*self.cart_icon_field)
    def checkout(self):
        self.click_element(*self.checkout_field)



