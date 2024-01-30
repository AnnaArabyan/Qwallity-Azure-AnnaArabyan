import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson28_pytest import config

class Helper():

    def __init__(self, browser):
        self.browser = browser

    def go_to_page(self, url):
        self.browser.get(url)
        logging.info(f"The web page {config.url} is opened")
        self.browser.maximize_window()
        self.browser.set_page_load_timeout(20)
     
    def find_elem_ui(self,loc, sec=60):
        try:
            elem = WebDriverWait(self.browser, sec).until(
                EC.visibility_of_element_located(loc))
            return elem
        except Exception as e:
            logging.info("Element is not vissible.", error=True)
            print(e, error=True)

    def find_elem_dom(self, loc, sec=60):
        elem = WebDriverWait(self.browser, sec).until(
            EC.presence_of_element_located(loc))
        return elem

    def find_and_click(self, loc, sec=15):
        elem= WebDriverWait(self.browser, sec).until(EC.element_to_be_clickable(loc))
        elem.click()

    def find_and_send_keys(self, loc, inp_text, sec=20):
        elem = self.find_elem_ui(loc, sec)
        elem.send_keys(inp_text)

    def element_count(self, loc):
        elems = self.browser.find_elements(*loc)
        count = len(elems)
        print(count)
        assert count > 0
        return count

        

     