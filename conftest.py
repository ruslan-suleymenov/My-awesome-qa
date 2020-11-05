import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="https://demo.opencart.com/", help="choose your URL")


@pytest.fixture
def browser(request):
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        driver = webdriver.Chrome(executable_path="/Users/Nigma/Applications/chromedriver")
    elif browser_param == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception(f"{request.param} is not supported!")
    driver.implicitly_wait(20)
    request.addfinalizer(driver.close)
    driver.get(request.config.getoption("--url"))
    return driver


@pytest.fixture(params=["chrome", "safari"])
def parametrize_browser(request):
    browser_param = request.param
    if browser_param == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser_param == "safari":
        driver = webdriver.Safari()
        driver.maximize_window()
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(20)
    request.addfinalizer(driver.quit)
    driver.get(request.config.getoption("--url"))

    return driver
