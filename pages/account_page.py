import time

from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):
    def get_customer_name(self) -> str:
        return self.get_element_text(locator=AccountPageLocators.CUSTOMER_NAME)

    def get_account_number(self) -> str:
        return self.get_element_text(locator=AccountPageLocators.ACCOUNT_NUMBER).replace(" ", "")

    def change_account_number(self) -> str:
        return self.get_element_text(locator=AccountPageLocators.ACCOUNT_NUMBER_1007).replace(" ", "")

    def click_transaction_button(self) -> None:
        self.click(locator=AccountPageLocators.TRANSACTIONS_BUTTON)

    def click_deposit_button(self) -> None:
        self.click(locator=AccountPageLocators.DEPOSIT_BUTTON)

    def click_withdrawl_button(self) -> None:
        self.click(locator=AccountPageLocators.WITHDRAWL_BUTTON)

    def click_submit_deposit(self) -> None:
        self.click(locator=AccountPageLocators.SUBMIT_DEPOSIT)

    def enter_deposit_amount(self, amount) -> None:
        self.fill_value(locator=AccountPageLocators.AMOUNT_INPUT, value=amount)

    def logout(self) -> None:
        self.click(locator=AccountPageLocators.LOGOUT_BUTTON)

    def select_account_number(self, account_number: str) -> bool:
        self.click(locator=AccountPageLocators.ACCOUNT_SELECTOR)
        if self.select_element(locator=AccountPageLocators.ACCOUNT_SELECTOR, label=account_number):
            return True
        else:
            return False

    def make_deposit(self, amount: str) -> None:
        self.click_deposit_button()
        self.enter_deposit_amount(amount=amount)
        self.click_submit_deposit()

    def make_withdrawl(self, amount: str) -> None:
        self.click_withdrawl_button()
        time.sleep(1)
        self.enter_deposit_amount(amount=amount)
        time.sleep(1)
        self.click_submit_deposit()

    def get_balance(self) -> str:
        return self.get_element_text(locator=AccountPageLocators.BALANCE)
