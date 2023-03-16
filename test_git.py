from datetime import datetime

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestPythonOrgSearch:

    @pytest.fixture(params=["chrome", "firefox"], scope="session", autouse=True)
    def browser(self, request):
        self.now = datetime.now()
        self.dt_string = self.now.strftime("%d-%m-%Y%H:%M:%S")

        self.selenoid_options = {"enableVNC": True,
                                 "enableVideo": True,
                                 "videoCodec": "mpeg4",
                                 "videoName": self.dt_string + ".mp4",
                                 "enableLog": True}
        if request.param == "chrome":
            self.browser_options = webdriver.ChromeOptions()
            self.browser_options.set_capability("selenoid:options", self.selenoid_options)
            self.driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                options=self.browser_options
            )

        elif request.param == "firefox":
            self.browser_options = webdriver.FirefoxOptions()
            self.browser_options.set_capability("selenoid:options", self.selenoid_options)
            self.driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                options=self.browser_options
            )
        elif request.param == "local":
            self.driver = webdriver.Chrome()
        else:
            raise ValueError("Invalid browser name")

        yield self.driver

        self.driver.quit()

    def test_search_in_python_org(self, browser):
        browser.get("https://github.com")
        assert "GitHub" in browser.title
        elem = browser.find_element(By.NAME, "q")
        elem.send_keys("dzitkowskik")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in browser.page_source


