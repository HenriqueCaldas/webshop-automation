from selenium.webdriver.common.by import By

class LoginPage:
    campoEmail = (By.ID, "Email")
    campoSenha = (By.ID, "Password")
    btn_logIn = (By.CSS_SELECTOR, ".button-1.login-button")

    def __init__(self, driver):
        self.driver = driver

    def efetuar_login(self, username="room3@gmail.com", password="Senh@room3"):
        self.driver.find_element(*self.campoEmail).send_keys(username)
        self.driver.find_element(*self.campoSenha).send_keys(password)
        self.driver.find_element(*self.btn_logIn).click()
