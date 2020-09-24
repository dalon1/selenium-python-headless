import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumTest1(unittest.TestCase):
    
    def setUp(self):
        browser_options = webdriver.ChromeOptions()
        # enable the argument below to run the test cases as headless using chrome driver
        browser_options.add_argument('headless')
        browser_options.add_argument('no-sandbox')

        # self.driver = webdriver.Chrome("/Users/AloniD/Develop/selenium-python-headless/chrome-drivers/mac/chromedriver", options=browser_options)

        # linux path
        self.driver = webdriver.Chrome("/usr/bin/chromedriver", options=browser_options)

    def test_open_bing_search(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.bing.com/")
        time.sleep(2)
        driver.close()

    def test_search_panama_in_bing_and_wikipedia(self):
        # step #1: Going to bing
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.bing.com/")
        time.sleep(2)

        # step #2: Searching for country
        bing_search = driver.find_element_by_id("sb_form_q")
        bing_search.send_keys("panama wikipedia")
        bing_search.send_keys(Keys.RETURN)
        time.sleep(2)

        # step #3: Iterate through search results - get first item only
        # and go to wiki page
        bing_results = driver.find_element_by_id("b_results")
        bing_wiki_result = bing_results.find_elements_by_tag_name("li")[0]
        bing_wiki_result = bing_wiki_result.find_elements_by_tag_name("a")[0]
        bing_wiki_result.click()
        time.sleep(2)

        # step #4: getting wiki page description
        wiki_header = driver.find_elements_by_tag_name("h1")[0].text
        driver.close()

        # assertions:
        assert wiki_header == "Panama", "This is not the wiki page about Panama. Value received was: %s" % wiki_header

    
    def test_search_israel_in_bing_and_wikipedia(self):
        # step #1: Going to bing
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.bing.com/")
        time.sleep(2)

        # step #2: Searching for country
        bing_search = driver.find_element_by_id("sb_form_q")
        bing_search.send_keys("israel wikipedia")
        bing_search.send_keys(Keys.RETURN)
        time.sleep(2)

        # step #3: Iterate through search results - get first item only
        # and go to wiki page
        bing_results = driver.find_element_by_id("b_results")
        bing_wiki_result = bing_results.find_elements_by_tag_name("li")[0]
        bing_wiki_result = bing_wiki_result.find_elements_by_tag_name("a")[0]
        bing_wiki_result.click()
        time.sleep(2)

        # step #4: getting wiki page description
        wiki_header = driver.find_elements_by_tag_name("h1")[0].text
        driver.close()

        # assertions:
        assert wiki_header == "Israel", "This is not the wiki page about Israel. Value received was: %s" % wiki_header

if __name__ == '__main__':
    unittest.main()
