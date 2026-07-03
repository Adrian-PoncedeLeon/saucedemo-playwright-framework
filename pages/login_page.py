from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.inventory_page import InventoryPage

class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_field = page.locator('[data-test="username"]')
        self.password_field = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')

    def login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
        return InventoryPage(self.page)