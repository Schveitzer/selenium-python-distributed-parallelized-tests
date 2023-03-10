import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestPythonOrgSearch:

    @pytest.fixture(params=["chrome", "firefox"], scope="session", autouse=True)
    def browser(self, request):
        if request.param == "chrome":
            self.browser_options = webdriver.ChromeOptions()
            self.driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                options=self.browser_options
            )
        elif request.param == "firefox":
            self.browser_options = webdriver.FirefoxOptions()
            self.driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                options=self.browser_options
            )
        elif request.param == "edge":
            self.browser_options = webdriver.EdgeOptions()
            self.driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                options=self.browser_options
            )
        else:
            raise ValueError("Invalid browser name")

        yield self.driver

    def test_search_in_python_org(self, browser):
        browser.get("https://github.com")
        assert "GitHub" in browser.title
        elem = browser.find_element(By.NAME, "q")
        elem.send_keys("dzitkowskik")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in browser.page_source

    def tearDown(self, browser):
        browser.close()
