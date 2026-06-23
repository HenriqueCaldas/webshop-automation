import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url_webshop = "https://demowebshop.tricentis.com/"

@pytest.fixture
def open_browser():
    options_chrome = Options()
    options_chrome.add_argument("--incognito")
    driver = webdriver.Chrome(options=options_chrome)
    driver.maximize_window()
    driver.get(url_webshop)
    yield driver
    driver.quit()

