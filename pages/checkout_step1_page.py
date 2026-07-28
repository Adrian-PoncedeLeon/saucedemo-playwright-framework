from pages.base_page import BasePage
from pages.checkout_step2_page import CheckoutPage2

class CheckoutPage1(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.title = self.page.locator("[data-test=\"title\"]")
        self.first_name = self.page.locator("#first-name")
        self.last_name = self.page.locator("#last-name")
        self.zip = self.page.locator("#postal-code")

    def is_loaded(self):
        return self.title.inner_text() == "Checkout: Your Information"
    
    def fill_information(self, first_name, last_name, zip):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.zip.fill(zip)
        return self
    
    def click_continue_button(self):
        self.page.locator(".submit-button").click()
        return CheckoutPage2(self.page) 