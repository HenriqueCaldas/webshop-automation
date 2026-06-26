from selenium.webdriver.common.by import By


class HomePage:
    btnLogIn = (By.CSS_SELECTOR, ".ico-login")
    itemComputer = (By.LINK_TEXT, "Computers")

    def __init__(self, driver):
        self.driver = driver

    def click_btn_login(self):
        self.driver.find_element(*self.btnLogIn).click()

    def click_link_computers(self):
        self.driver.find_element(*self.itemComputer).click()

    def click_link_notebooks(self):
        self.driver.find_element(By.LINK_TEXT, "Notebooks").click()

    def click_product_notebook(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/141-inch-laptop"]').click()
