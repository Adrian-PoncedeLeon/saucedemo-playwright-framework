from pages.base_page import BasePage
from pages.cart_page import CartPage

class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.title = self.page.locator("[data-test=\"title\"]")
        self.products = self.page.locator(".inventory_item")
        self.cart = self.page.locator("[data-test='shopping-cart-link']")

    def find_product(self, product_name):
        for i in range(self.products.count()):
            product = self.products.nth(i).locator(".inventory_item_name").inner_text()
            if product == product_name:
                return self.products.nth(i)

    def is_loaded(self):
        return self.title.is_visible()
    
    def add_to_cart(self, product_name):
        product = self.find_product(product_name)
        if product:
            product.locator(".btn_inventory").click()
        return self
    
    def add_button_text_changed(self, product_name):
        product = self.find_product(product_name)
        if not product:
            return False
        return (product.locator("button").inner_text() == "Remove")
    
    def go_to_cart(self):
        self.cart.click()
        return CartPage(self.page)
        


