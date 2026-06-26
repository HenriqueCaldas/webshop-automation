from time import sleep
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


class TestLogin:

    def test_validar_cliente_logado(self, open_browser):
        user_name = "room3@gmail.com"
        password = "Senh@room3"
        driver = open_browser
        home_page = HomePage(driver)
        home_page.click_btn_login()
        login_page = LoginPage(driver)
        login_page.efetuar_login(user_name, password)
        nome_conta = login_page.capturar_nome_conta_logada()
        assert nome_conta == user_name, f"Erro: O nome da conta deveria ser {nome_conta}"
