import logging
import os
from selenium import webdriver
import pytest
from lesson28_pytest import config



@pytest.fixture()
def driver():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        logging.info("The driver is initialized")
        driver.maximize_window()
        yield driver
        driver.quit()
    except Exception as error:
        raise Exception(error)
    

def pytest_configure():
    logging.basicConfig(
                    level=logging.INFO,
                    filename=os.path.join(os.path.join(os.path.dirname(__file__), config.log_file_name)),
                    filemode='a',
                    encoding='utf-8'
                    )