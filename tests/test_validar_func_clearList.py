from pages.CompareProductsPage import CompareProductsPage
from pages.PDPPage import PDPPage
from pages.HomePage import HomePage


class TestClearList:

    def test_Verificar_func_ClearList_cliente_logado(self, open_browser):
        driver = open_browser
        home_page = HomePage(driver)
        home_page.clicarLinkComputers()
        home_page.clicarLinkNotebooks()
        home_page.clicarProdutroNotebook()

        pdp_page = PDPPage(driver)
        pdp_page.clickAddToCompareList()
        compare_products_page = CompareProductsPage(driver)
        compare_products_page.clickClearList()
        msg_catch = compare_products_page.capturarMensagemNoItems()
        assert not compare_products_page.is_clear_list_visible()
        assert msg_catch == "You have no items to compare."
