# This img is not working either - below is the error msg. seems like the indexing of elements may be out of range in this "selenium/standalone-chrome image"
# ======================================================================
# ERROR: test_search_israel_in_bing_and_wikipedia (test_selenium_search_countries.SeleniumTest1)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/qa-app/test/test_selenium_search_countries.py", line 74, in test_search_israel_in_bing_and_wikipedia
#     bing_wiki_result.click()
#   File "/usr/local/lib/python3.6/dist-packages/selenium/webdriver/remote/webelement.py", line 80, in click
#     self._execute(Command.CLICK_ELEMENT)
#   File "/usr/local/lib/python3.6/dist-packages/selenium/webdriver/remote/webelement.py", line 633, in _execute
#     return self._parent.execute(command, params)
#   File "/usr/local/lib/python3.6/dist-packages/selenium/webdriver/remote/webdriver.py", line 321, in execute
#     self.error_handler.check_response(response)
#   File "/usr/local/lib/python3.6/dist-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
#     raise exception_class(message, screen, stacktrace)
# selenium.common.exceptions.WebDriverException: Message: unknown error: session deleted because of page crash
# from unknown error: cannot determine loading status
# from tab crashed
#   (Session info: headless chrome=85.0.4183.83)


# ======================================================================
# ERROR: test_search_panama_in_bing_and_wikipedia (test_selenium_search_countries.SeleniumTest1)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/qa-app/test/test_selenium_search_countries.py", line 49, in test_search_panama_in_bing_and_wikipedia
#     wiki_header = driver.find_elements_by_tag_name("h1")[0].text
# IndexError: list index out of range

# ----------------------------------------------------------------------
# Ran 3 tests in 21.974s

# FAILED (errors=2)

FROM selenium/standalone-chrome:latest
USER root
WORKDIR /qa-app
COPY requirements.txt .
COPY test test
RUN apt-get update \
    && apt-get install -y python3 \
    && apt-get install -y python3-pip \
    && pip3 install -r requirements.txt
CMD ["python3", "-m", "unittest", "discover", "-s", "test"]