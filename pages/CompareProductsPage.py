from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class CompareProductsPage:

    btnClearList =(By.CSS_SELECTOR, ".clear-list")
    msg_no_items = (By.CSS_SELECTOR, ".page-body")
    btn_clear_list = (By.CSS_SELECTOR, "input[value='Clear list']")

    def __init__(self, driver):
        self.driver = driver


    def click_clear_list(self):
        self.driver.find_element(*self.btnClearList).click()

    def capturar_mensagem_no_items(self):
        return self.driver.find_element(*self.msg_no_items).text

    def is_clear_list_visible(self):
        try:
            self.driver.find_element(*self.btnClearList)
            return True
        except NoSuchElementException:
            return False