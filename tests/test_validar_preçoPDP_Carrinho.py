from asyncio import sleep

from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.PDPPage import PDPPage


class TestPrecoPDPCart:

    def test_validar_preco_PDP_mesmo_Cart(self, open_browser):
        driver = open_browser
        home_page = HomePage(driver)
        home_page.clicarLinkComputers()
        home_page.clicarLinkNotebooks()
        home_page.clicarProdutroNotebook()

        pdp_page = PDPPage(driver)
        valorProdutoPDP = pdp_page.capturarValorDoProduto()
        pdp_page.clickAddToCart()
        pdp_page.clickIrParaCart()

        cart_page = CartPage(driver)
        cartValorUnitarioList = cart_page.capturarValorUnitarioDaList()
        cartValorSubtotalList = cart_page.capturarvalorSubtotalList()
        cartValorSubtotalResumo = cart_page.capturarValorSubtotalResumo()
        cartValorTotalResumo = cart_page.capturarValorTotalResumo()

        assert valorProdutoPDP == cartValorUnitarioList == cartValorSubtotalList == cartValorSubtotalResumo == cartValorTotalResumo, \
            f"Valores divergentes: PDP={valorProdutoPDP}, Unitário={cartValorUnitarioList}, Subtotal={cartValorSubtotalList}, Resumo={cartValorSubtotalResumo}, Total={cartValorTotalResumo}"




