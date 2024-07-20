from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.config import config
def get_driver():
    browser = config.BROWSER
    if browser == "chrome":
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-features=ReadingList")
        options.add_argument("--disable-infobars")
        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.popups": 0
        }
        options.add_experimental_option("prefs", prefs)
        return webdriver.Chrome(options=options)
    elif browser == "firefox":
        return webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser {browser}")