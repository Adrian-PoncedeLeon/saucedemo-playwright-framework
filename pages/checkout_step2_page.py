from pages.base_page import BasePage
from pages.checkout_step3_page import CheckoutPage3

class CheckoutPage2(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.title = self.page.locator("[data-test=\"title\"]")

    def is_loaded(self):
        return self.title.inner_text() == "Checkout: Overview"
    
    def click_finish_button(self):
        self.page.locator("button#finish").click()
        return CheckoutPage3(self.page) 