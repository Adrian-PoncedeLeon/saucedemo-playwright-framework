from pages.base_page import BasePage


class CheckoutPage3(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.title = self.page.locator("[data-test=\"title\"]")

    def is_loaded(self):
        return self.title.inner_text() == "Checkout: Complete!"
    
    def click_back_home_button(self):
        from pages.inventory_page import InventoryPage
        self.page.locator("#back-to-products").click()
        return InventoryPage(self.page) 