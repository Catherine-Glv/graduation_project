from playwright.sync_api import Page

from Other.locators.account_page_locators import *
from Other.pages.base_page import BasePage


class AccountPage(BasePage):

    def __init__(self, page: Page, url: str):
        super().__init__(page, url)

    def select_account(self):
        self.select_option(select_locator=SELECT_ACCOUNT_NUMBER_LOCATOR, option_locator=SELECT_OPTION_NUMBER_LOCATOR)

    def click_transactions(self):
        self.click(BUTTON_TRANSACTIONS_LOCATOR)

    def click_deposit(self):
        self.click(BUTTON_DEPOSIT_LOCATOR)

    def click_withdrawl(self):
        self.click(BUTTON_WITHDRAWL_LOCATOR)

    def input_deposit_amount(self, amount: str):
        self.input_text(INPUT_DEPOSIT_WITHDRAWL_LOCATOR)

    def input_withdrawl_amount(self, amount: str):
        self.input_text(INPUT_DEPOSIT_WITHDRAWL_LOCATOR)

    def click_logout(self):
        self.click(BUTTON_LOGOUT_LOCATOR)

    def click_home(self):
        self.click(BUTTON_HOME_LOCATOR)
