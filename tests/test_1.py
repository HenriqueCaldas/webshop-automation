from time import sleep
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


class TestLogin:

    def test_login(self, open_browser):
        driver = open_browser
        home_page = HomePage(driver)
        home_page.clicarBtnLogIn()
        login_page = LoginPage(driver)
        login_page.efetuar_login()
        sleep(3)