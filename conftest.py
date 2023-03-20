from datetime import datetime

import pytest

from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def browser(browser_name):
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y%H:%M:%S")

    selenoid_options = {"enableVNC": True,
                        "enableVideo": False,
                        "videoCodec": "mpeg4",
                        "videoName": dt_string + ".mp4",
                        "enableLog": False}
    if browser_name == "chrome":
        browser_options = webdriver.ChromeOptions()
        browser_options.add_argument('--ignore-ssl-errors=yes')
        browser_options.add_argument('--ignore-certificate-errors')
        browser_options.set_capability("selenoid:options", selenoid_options)
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=browser_options
        )

    elif browser_name == "firefox":
        browser_options = webdriver.FirefoxOptions()
        browser_options.set_capability("selenoid:options", selenoid_options)
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=browser_options
        )
    elif browser_name == "local":
        driver = webdriver.Chrome()
    else:
        raise ValueError("Invalid browser name")

    yield driver

    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="append",
        default=[],
        help="list of browser to pass to test functions",
    )


def pytest_generate_tests(metafunc):
    if "browser_name" in metafunc.fixturenames:
        metafunc.parametrize("browser_name", metafunc.config.getoption("browser_name"))
