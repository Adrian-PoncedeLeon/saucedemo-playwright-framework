from pages.base_page import BasePage

class CartPage(BasePage):
    
    def is_loaded(self):
        return (self.page.locator("data-test:'title'").inner_text() == "Your Cart")