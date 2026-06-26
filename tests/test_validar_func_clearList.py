from pages.CompareProductsPage import CompareProductsPage
from pages.PDPPage import PDPPage
from pages.HomePage import HomePage


class TestClearList:

    def test_verificar_func_clear_list(self, open_browser):
        driver = open_browser
        home_page = HomePage(driver)
        home_page.click_link_computers()
        home_page.click_link_notebooks()
        home_page.click_product_notebook()

        pdp_page = PDPPage(driver)
        pdp_page.click_add_to_compare_list()
        compare_products_page = CompareProductsPage(driver)
        compare_products_page.click_clear_list()
        msg_catch = compare_products_page.capturar_mensagem_no_items()
        assert not compare_products_page.is_clear_list_visible()
        assert msg_catch == "You have no items to compare."
