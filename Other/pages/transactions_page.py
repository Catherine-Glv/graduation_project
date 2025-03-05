from playwright.sync_api import Page

from Other.locators.table_transactions_locators import *
from Other.pages.base_page import BasePage

class TransactionsPage(BasePage):

    def __init__(self, page: Page, url: str):
        super().__init__(page, url)

    def click_reset(self):
        self.click(BUTTON_RESET_LOCATOR)

    def click_back(self):
        self.click(BUTTON_BACK_LOCATOR)

    def is_transaction_table_visible(self):
        return self.is_visible(TABLE_TRANSACTIONS_LOCATOR)
