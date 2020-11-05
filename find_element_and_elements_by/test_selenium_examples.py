from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import time, sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPage, ProductPage, AdminPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


def test_element_by_class_name_selector(parametrize_browser):
    bro = parametrize_browser
    bro.find_element_by_class_name(MainPage.promoblock).click()
    bro.find_element_by_class_name("breadcrumb")
    bro.find_element_by_class_name("input-group-btn")
    bro.find_element_by_class_name("input-group")


def test_element_by_xpath(browser):
    browser.find_element_by_xpath("//div[@class='swiper-viewport']").click()
    browser.find_element_by_xpath("//*[@class='breadcrumb']")
    browser.find_element_by_xpath("//button[@data-original-title='Add to Wish List']").click()
    browser.find_element_by_xpath("//div[contains(@class, 'alert-success')]")


def test_element_by_id(browser):
    wait = WebDriverWait(browser, 10)
    browser.find_element(By.ID, "slideshow0").click()
    browser.find_element(By.CLASS_NAME, "breadcrumb")
    el = wait.until(EC.element_to_be_clickable((By.ID, ProductPage.button_cart)))
    el.click()
    browser.get_screenshot_as_file("screenshot-1.png")
    el = wait.until(EC.element_to_be_clickable((By.ID, ProductPage.cart)))
    el.click()
    browser.get_screenshot_as_file("screenshot-2.png")
    el = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
    el.click()
    browser.get_screenshot_as_file("screenshot-3.png")


def test_element_by_link_text(browser):
    desktops_link = browser.find_element_by_link_text(MainPage.desktop)
    ActionChains(browser).move_to_element(desktops_link).pause(2).perform()
    browser.find_element_by_link_text("Show All Desktops").click()
    browser.find_element_by_partial_link_text("Product Compare")

    components_link = browser.find_element_by_link_text(MainPage.components)
    ActionChains(browser).move_to_element(components_link).pause(2).perform()
    browser.find_element_by_link_text("Monitors (2)").click()

    laptops_link = browser.find_element_by_link_text(MainPage.laptops)
    ActionChains(browser).move_to_element(laptops_link).pause(2).perform()

    tablets_link = browser.find_element_by_link_text(MainPage.tablets).click()

    software_link = browser.find_element_by_link_text(MainPage.software).click()

    phones_link = browser.find_element_by_link_text(MainPage.phones).click()

    cameras_link = browser.find_element_by_link_text(MainPage.cameras).click()

    mp3_link = browser.find_element_by_link_text(MainPage.mp3).click()


def test_search_input(browser):
    input_search = browser.find_element_by_name(MainPage.search_input)
    input_search.send_keys("iMac")
    input_search.send_keys(Keys.RETURN)


def test_footer(browser):
    about_link = browser.find_element_by_link_text(MainPage.about_us).click()
    del_link = browser.find_element_by_link_text(MainPage.del_info).click()
    privacy_link = browser.find_element_by_link_text(MainPage.privacy_pol).click()
    terms_link = browser.find_element_by_link_text(MainPage.terms).click()


def test_product_page(browser):
    input_search = browser.find_element_by_name(MainPage.search_input)
    input_search.send_keys("iPhone")  # find Iphone in our shop
    input_search.send_keys(Keys.RETURN)
    iphone_link = browser.find_element_by_link_text("iPhone").click()  # click iPhone
    browser.find_element_by_xpath(ProductPage.pic_iphone).click()


def test_admin_login_page(browser):
    browser.get("https://demo.opencart.com/admin/")
    input_login = browser.find_element_by_id(AdminPage.input_login)
    input_login.clear()
    input_login.send_keys("admin")
    input_pass = browser.find_element_by_id(AdminPage.input_pass)
    input_pass.clear()
    input_pass.send_keys("1234")
    input_pass.send_keys(Keys.RETURN)

# def test_elements_by_css_selector(browser):
#     navbar_items = browser.find_elements(MainPage.nav_links)
#     for item in navbar_items:
#         ActionChains(browser).move_to_element(item).pause(0.5).perform()


# def test_element_by_class_name_selector(parametrize_browser):
#     parametrize_browser.find_element_by_class_name("swiper-viewport").click()
#     parametrize_browser.find_element_by_class_name("breadcrumb")
