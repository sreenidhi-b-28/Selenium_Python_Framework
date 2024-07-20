from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    def find_element(self, *locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, *locator):
        element = self.find_element(*locator)
        element.click()

    def send_keys(self, text, *locator):
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(text)


