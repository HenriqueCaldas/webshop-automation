from selenium.webdriver.common.by import By


class CartPage:

    valorUnitarioList = (By.CSS_SELECTOR, ".product-unit-price")
    valorSubtotalList = (By.CSS_SELECTOR, ".product-subtotal")
    valorSubtotalResumo = (By.CSS_SELECTOR, ".product-price")
    valorTotalResumo = (By.CSS_SELECTOR, ".product-price.order-total")

    def __init__(self, driver):
        self.driver = driver

    def capturarValorUnitarioDaList(self):
        return self.driver.find_element(*self.valorUnitarioList).text

    def capturarvalorSubtotalList(self):
        return self.driver.find_element(*self.valorSubtotalList).text

    def capturarValorSubtotalResumo(self):
        return self.driver.find_element(*self.valorSubtotalResumo).text

    def capturarValorTotalResumo(self):
        return self.driver.find_element(*self.valorTotalResumo).text
