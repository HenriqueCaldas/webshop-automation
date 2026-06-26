from selenium.webdriver.common.by import By

from utils.waits import esperar_elemento

class CartPage:
    """
    Page Object da tela de carrinho.
    Contém métodos para capturar valores do carrinho e interagir com a página.
    """

    valor_unit_list_locator = (By.CSS_SELECTOR, ".product-unit-price")
    valor_subtotal_list_locator = (By.CSS_SELECTOR, ".product-subtotal")
    valor_subtotal_resumo_locator = (By.CSS_SELECTOR, ".product-price")
    valor_total_resumo_locator = (By.CSS_SELECTOR, ".product-price.order-total")
    qty_imput_locator = (By.CSS_SELECTOR, ".qty-input")

    def __init__(self, driver):
        self.driver = driver

    def capturar_valor_unitario_da_lista(self):
        elemento = esperar_elemento(self.driver, self.valor_unit_list_locator)
        return elemento.text


    def capturar_valor_subtotal_list(self):
        elemento = esperar_elemento(self.driver, self.valor_subtotal_list_locator)
        return elemento.text

    def capturar_valor_subtotal_resumo(self):
        elemento = esperar_elemento(self.driver, self.valor_subtotal_list_locator)
        return elemento.text


    def capturar_valor_total_resumo(self):
        elemento = esperar_elemento(self.driver, self.valor_total_resumo_locator)
        return elemento.text

    def capturar_quantidade_produto(self):
        elemento = esperar_elemento(self.driver, self.qty_imput_locator)
        valor = int(elemento.get_attribute("value"))
        return valor