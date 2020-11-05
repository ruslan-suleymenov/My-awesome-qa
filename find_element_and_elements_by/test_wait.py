import pytest
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# capabilities = webdriver.DesiredCapabilities.CHROME.copy()
# capabilities['timeouts'] = {'implicit': 3000, 'pageLoad': 3000, 'script': 30000}
# capabilities['loggingPrefs'] = {'browser': 'ALL', 'client': 'ALL', 'driver': 'ALL',
#                                 'performance': 'ALL', 'server': 'ALL'}
# # profile = webdriver.ChromeProfile()
# # profile.set_preference('app.update.auto', False)
# # profile.set_preference('app.update.enabled', False)
# # profile.accept_untrusted_certs = True


def test_wait():
    wd = webdriver.Chrome(executable_path="/Users/Nigma/Applications/chromedriver")
    wd.implicitly_wait(10)
    wd.get("https://pagination.js.org/")
    wd.find_element_by_css_selector('#demo1 > div.data-container > ul > li:nth-child(1)').click()
    wd.quit()
