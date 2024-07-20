import pytest
from pages.LoginPage import LoginPage
from utils.browser import get_driver
from config.config import config
from utils.logger import logger
from config.credentials import credentials

@pytest.fixture
def setup():
    driver = get_driver()
    driver.get(config.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def login(setup):
    driver = setup
    login = LoginPage(driver)
    login.enter_mail_id(credentials.LOGIN_USERNAME)
    login.enter_password(credentials.LOGIN_PASSWORD)
    login.clicking_element()

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    logger.info("Starting the tests")

@pytest.hookimpl(trylast=True)
def pytest_unconfigure(config):
    logger.info("End of tests")

