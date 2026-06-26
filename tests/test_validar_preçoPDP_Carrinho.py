import logging
from time import sleep

from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.PDPPage import PDPPage


class TestPrecoPDPCart:

    def test_check_preco_pdp_same_cart(self, open_browser):
        driver = open_browser
        home_page = HomePage(driver)
        home_page.click_link_computers()
        home_page.click_link_notebooks()
        home_page.click_product_notebook()

        pdp_page = PDPPage(driver)
        valor_product_pdp = pdp_page.capturar_valor_do_produto()
        logging.info(f"Valor capturado na PDP: {valor_product_pdp}")
        pdp_page.click_add_to_cart()
        pdp_page.click_ir_para_cart()

        cart_page = CartPage(driver)
        cart_valor_unit_list = cart_page.capturar_valor_unitario_da_lista()
        logging.info(f"Valor capturado no carrinho: {cart_valor_unit_list}")
        cart_valor_subtotal_list = cart_page.capturar_valor_subtotal_list()
        cart_valor_subtotal_resumo = cart_page.capturar_valor_subtotal_resumo()
        cart_valor_total_resumo = cart_page.capturar_valor_total_resumo()

        assert valor_product_pdp == cart_valor_unit_list, f"Erro: PDP={valor_product_pdp} diferente do Unitário={cart_valor_unit_list}"
        assert cart_valor_unit_list == cart_valor_subtotal_list, f"Erro: Unitário={cart_valor_unit_list} diferente do Subtotal={cart_valor_subtotal_list}"
        assert cart_valor_subtotal_list == cart_valor_subtotal_resumo, f"Erro: Subtotal={cart_valor_subtotal_list} diferente do Resumo={cart_valor_subtotal_resumo}"
        assert cart_valor_subtotal_resumo == cart_valor_total_resumo, f"Erro: Resumo={cart_valor_subtotal_resumo} diferente do Total={cart_valor_total_resumo}"


    def test_check_preco_quantidade_add_mesmo_produto_cart(self, open_browser):
        driver = open_browser
        home_page = HomePage(driver)
        home_page.click_link_computers()
        home_page.click_link_notebooks()
        home_page.click_product_notebook()

        pdp_page = PDPPage(driver)
        valor_product_pdp = pdp_page.capturar_valor_do_produto()
        pdp_page.click_add_to_cart()
        sleep(3)
        pdp_page.click_add_to_cart()
        pdp_page.click_ir_para_cart()

        cart_page = CartPage(driver)
        cart_valor_unit_list = cart_page.capturar_valor_unitario_da_lista()
        logging.info(f"Valor capturado no carrinho: {cart_valor_unit_list}")
        cart_valor_subtotal_list = cart_page.capturar_valor_subtotal_list()
        cart_valor_subtotal_resumo = cart_page.capturar_valor_subtotal_resumo()
        cart_valor_total_resumo = cart_page.capturar_valor_total_resumo()
        cart_value_quantidade = cart_page.capturar_quantidade_produto()

        assert valor_product_pdp == cart_valor_unit_list, f"Erro: PDP={valor_product_pdp} diferente do Unitário={cart_valor_unit_list}"
        assert cart_valor_subtotal_list == cart_valor_subtotal_resumo, f"Erro: Subtotal={cart_valor_subtotal_list} diferente do Resumo={cart_valor_subtotal_resumo}"
        assert cart_valor_subtotal_resumo == cart_valor_total_resumo, f"Erro: Resumo={cart_valor_subtotal_resumo} diferente do Total={cart_valor_total_resumo}"
        assert cart_value_quantidade == 2, f"Erro: A quantidade está incorreta: esperado 2, obtido {cart_value_quantidade}"

