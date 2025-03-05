from playwright.sync_api import Page

from Other.locators.login_page_locators import *
from Other.pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, page: Page, url: str):
        super().__init__(page, url)

    def click_customer_login(self):
        self.click(SELECT_LOGIN_LOCATOR)

    def select_user(self):
        self.select_option(SELECT_LOGIN_OPTION_3_LOCATOR)

    def click_login(self):
        self.click(BUTTON_LOGIN_LOCATOR)

    def is_login_button_visible(self):
        return self.is_visible(BUTTON_LOGIN_WITH_OPTION_LOCATOR)
