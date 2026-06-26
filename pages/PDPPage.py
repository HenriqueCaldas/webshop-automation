from selenium.webdriver.common.by import By


class PDPPage:

    btnAddToCompareList = (By.CSS_SELECTOR, ".button-2.add-to-compare-list-button")
    btnAddToCart = (By.ID, "add-to-cart-button-31")
    valorProduto = (By.CSS_SELECTOR, ".price-value-31")
    msg_no_items = (By.CSS_SELECTOR, ".page-body")
    btnIrPraCart = (By.CSS_SELECTOR, ".cart-label")

    def __init__(self, driver):
        self.driver = driver

    def click_add_to_compare_list(self):
        self.driver.find_element(*self.btnAddToCompareList).click()

    def click_add_to_cart(self):
        self.driver.find_element(*self.btnAddToCart).click()

    def capturar_valor_do_produto(self):
        return self.driver.find_element(*self.valorProduto).text

    def click_ir_para_cart(self):
        self.driver.find_element(*self.btnIrPraCart).click()
