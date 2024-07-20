import pytest
from pages.LoginPage import LoginPage
from data_loaders.login_data import login_data
from utils.logger import logger


@pytest.mark.parametrize("username, password", login_data)
class TestLogin:
    def test_login(self, setup, username, password):
        driver = setup
        login = LoginPage(driver)
        login.enter_mail_id(username)
        login.enter_password(password)
        logger.info(f"checking logging info for username={username} and password={password}")
        login.clicking_element()
        assert login.is_login_successful() == driver.current_url





