from selenium.webdriver.common.by import By
from lesson28_pytest.Helpers.general_helpers import Helper
from lesson28_pytest.TestData.data import search_text


class EntryAuto(Helper):
    
    search_field = (By.XPATH, '//div[@class="search-master"]//input[@id="searchInp"]')
    btn_search_click = (By.XPATH, '//i[@id="submit_search"]')
    search_result = (By.XPATH, '//div[@class="card"]')

    def enter_to_autoam(self):
        self.find_and_send_keys(self.search_field, search_text)  
        self.find_and_click(self.btn_search_click)
        result_count = self.element_count(self.search_result)
        return result_count
      



    
        


        