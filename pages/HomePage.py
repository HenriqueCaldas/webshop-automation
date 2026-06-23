from selenium.webdriver.common.by import By


class HomePage:

    btnLogIn =(By.CSS_SELECTOR, ".ico-login")
    itemComputer = (By.LINK_TEXT, "Computers")


    def __init__(self, driver):
        self.driver = driver

    def clicarBtnLogIn(self):
        self.driver.find_element(*self.btnLogIn).click()

    def clicarLinkComputers(self):
        self.driver.find_element(*self.itemComputer).click()

    def clicarLinkNotebooks(self):
        self.driver.find_element(By.LINK_TEXT, "Notebooks").click()

    def clicarProdutroNotebook(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/141-inch-laptop"]').click()



