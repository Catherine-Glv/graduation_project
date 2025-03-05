from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

    def open_page(self, url=URL) -> None:
        self.open_url(url=url)

    def login(self, customer_name: str) -> None:
            self.click_customer_login_button()
            self.select_customer(customer_name=customer_name)
            self.click_login_button()

    def click_customer_login_button(self) -> None:
        self.click(locator=LoginPageLocators.CUSTOMER_LOGIN_BUTTON)

    def click_login_button(self) -> None:
        self.click(locator=LoginPageLocators.LOGIN_BUTTON)

    def click_home_button(self) -> None:
        self.click(locator=LoginPageLocators.HOME_BUTTON)

    def select_customer(self, customer_name: str) -> bool:
        self.click(locator=LoginPageLocators.CUSTOMER_SELECTOR)
        if self.select_element(locator=LoginPageLocators.CUSTOMER_SELECTOR, label=customer_name):
            return True
        else:
            return False
