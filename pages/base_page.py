from playwright.sync_api import Page
from utils.config import BASE_URL

class BasePage:
    def __init__(self, page:Page):
        self.page = page

    def navigate(self, path=""):
        self.page.goto(BASE_URL+path)