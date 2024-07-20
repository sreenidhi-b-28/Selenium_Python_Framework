import time
from pages.ProductPage import ProductPage
from pages.CheckoutPage import CheckoutPage
from data_loaders.product_data import product_data
from utils.logger import logger
from config.checkout import *


class TestCart:

    def test_add_items_to_cart(self, setup, login):
        driver = setup
        login
        product_page = ProductPage(driver)
        checkout_page = CheckoutPage(driver)
        for product in product_data:
            logger.info(f"Adding {product} to the cart")
            product_page.select_product(product_name=product.lower())
        logger.info("Click on cart icon")
        product_page.click_on_cart()
        logger.info("Checkout")
        product_page.checkout()
        time.sleep(2)
        checkout_page.enter_first_name(FIRST_NAME)
        checkout_page.enter_last_name(LAST_NAME)
        checkout_page.enter_postal_code(POSTAL_CODE)
        time.sleep(2)
        logger.info("Click on continue button")
        checkout_page.continue_button()
        time.sleep(2)
        logger.info("Finish Shopping")
        checkout_page.finish_button()
        time.sleep(4)








