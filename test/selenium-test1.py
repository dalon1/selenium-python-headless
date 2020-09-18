import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumTest1(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome("/Users/AloniD/Develop/selenium-python-headless/chrome-drivers/mac/chromedriver")

    def test_open_bing_search(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.bing.com/")
        time.sleep(2)
        driver.close()

    def test_search_panama_in_bing(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.bing.com/")
        time.sleep(2)
        elem = driver.find_element_by_id("sb_form_q")
        elem.send_keys("panama")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        #driver.set_page_load_timeout(10)
        driver.close()

    def test_search_israel_in_bing(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.bing.com/")
        time.sleep(2)
        elem = driver.find_element_by_id("sb_form_q")
        elem.send_keys("israel")
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        #driver.set_page_load_timeout(10)
        driver.close()

if __name__ == '__main__':
    unittest.main()