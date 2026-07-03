from pages.base_page import BasePage

class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.title = self.page.locator("[data-test=\"title\"]")
        self.products = self.page.locator(".cart_item")
    
    def is_loaded(self):
        return (self.title.inner_text() == "Your Cart")

    def find_product(self, product_name):
        for i in range(self.products.count()):
            product = self.products.nth(i).locator(".inventory_item_name").inner_text()
            if product == product_name:
                return self.products.nth(i)
            
    def product_exists(self, product_name):
        if not self.find_product(product_name):
            return False
        else:
            return True