import logging
import datetime
from lesson28_pytest.Pages.enter_autoam import EntryAuto
from lesson28_pytest.Helpers.general_helpers import Helper
from lesson28_pytest import config


 
# def test_info_search(driver):
#     logging.info("Start_time: %s", datetime.datetime.now())   
#     helper_obj = Helper(driver)
#     helper_obj.go_to_page(config.url)
    

#     entry_obj = EntryAuto(driver)
#     entry_obj.enter_to_autoam()
#     logging.info(f"The search and assertion are done successfully")
#     logging.info("End_time: %s", datetime.datetime.now())
    
def test_valid():
    assert 1==1

def test_invalid():
    assert 1==2

   
   
    
   
  


    
    
 