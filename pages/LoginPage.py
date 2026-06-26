from selenium.webdriver.common.by import By

from utils.waits import esperar_elemento


class LoginPage:
    campoEmail = (By.ID, "Email")
    campoSenha = (By.ID, "Password")
    btn_logIn = (By.CSS_SELECTOR, ".button-1.login-button")
    account_locator = (By.CSS_SELECTOR, ".account")

    def __init__(self, driver):
        self.driver = driver

    def efetuar_login(self, username, password):
        self.driver.find_element(*self.campoEmail).send_keys(username)
        self.driver.find_element(*self.campoSenha).send_keys(password)
        self.driver.find_element(*self.btn_logIn).click()

    def capturar_nome_conta_logada(self):
        elemento = esperar_elemento(self.driver, self.account_locator)
        return elemento.text