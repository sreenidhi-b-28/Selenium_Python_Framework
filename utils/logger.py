import logging

def setup_logger():
    logger = logging.getLogger("Selenium POM tests")
    logger.setLevel(logging.DEBUG)

    #handler = logging.FileHandler("Selenium_Test.log")
    handler = logging.FileHandler(filename='../reports/Selenium_Test.log')
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return  logger

logger = setup_logger()