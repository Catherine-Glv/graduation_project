import allure
import pytest
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from locators.account_page_locators import *
from locators.login_page_locators import *

@allure.feature('account_page')
class TestAccountPage:
    @allure.story('Тест выбора номера аккаунта')
    def test_account_selection(self, login_page_pl, account_page_pl):
        """
        Сценарий: Выбор номера аккаунта
        Шаги авторизации:
        1. Нажать кнопку Customer Login.
        2. Кликнуть по селекту и выбрать в селекте одно из значений для входа.
        3. Кликнуть на кнопку Login.
        Шаги после авторизации:
        1. Проверить, что селект для Account number отображается.
        2. Кликнуть по селекту и проверить, что отображается 3 позиции для выбора.
        3. Кликнуть по одному из вариантов в селекте.
        4. Проверить, что отображается выбранное значение в селекте.
        """
        # Шаги авторизации
        login_page_pl.click_customer_login()
        login_page_pl.select_user()
        login_page_pl.click_login()
        print("Авторизация выполнена")

        # Шаг 1: Проверить, что селект для Account number отображается
        assert account_page_pl.is_visible(SELECT_ACCOUNT_NUMBER_LOCATOR), (
            "Ожидаемый результат: Селект для Account number отображается. "
            "Фактический результат: Селект не отобразился."
        )
        print("Шаг 1: Селект для Account number отображается.")

        # Шаг 2: Кликнуть по селекту и проверить, что отображается 3 позиции для выбора
        account_page_pl.click(SELECT_ACCOUNT_NUMBER_LOCATOR)
        options = account_page_pl.locator(SELECT_ACCOUNT_NUMBER_LOCATOR).locator("option")
        assert options.count() == 3, (
            f"Ожидаемый результат: В селекте 3 позиции для выбора. "
            f"Фактический результат: В селекте {options.count()} позиций."
        )
        print("Шаг 2: В селекте отображается 3 позиции для выбора.")

        # Шаг 3: Кликнуть по одному из вариантов в селекте
        account_page_pl.select_account()
        print("Шаг 3: Выбран аккаунт с номером 1008.")

        # Шаг 4: Проверить, что отображается выбранное значение в селекте
        selected_option = account_page_pl.get_text(SELECT_OPTION_NUMBER_LOCATOR)
        assert selected_option == "1008", (
            f"Ожидаемый результат: Выбранный аккаунт: 1008. "
            f"Фактический результат: Выбранный аккаунт: {selected_option}."
        )
        print("Шаг 4: В селекте отображается выбранное значение: 1008.")

    @allure.story('Тест разлогина из аккаунта')
    def test_logout(self, account_page_pl):
        """
        Сценарий: Разлогин из аккаунта
        Шаги:
        1. Нажать кнопку Logout.
        2. Проверить, что осуществлен переход на страницу авторизации.
        """
        # Шаг 1: Нажать кнопку Logout
        account_page_pl.click_logout()
        print("Шаг 1: Нажата кнопка Logout.")

        # Шаг 2: Проверить, что осуществлен переход на страницу авторизации
        expected_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer"
        account_page_pl.check_url(expected_url)
        print(
            f"Шаг 2: Ожидаемый результат: Переход на страницу {expected_url}. "
            f"Фактический результат: Переход на страницу {account_page_pl.url}."
        )

    @allure.story('Тест выхода по кнопке Home')
    def test_home_button(self, login_page_pl, account_page_pl):
        """
        Сценарий: Выход на авторизацию по кнопке Home
        Шаги авторизации:
        1. Нажать кнопку Customer Login.
        2. Кликнуть по селекту и выбрать в селекте одно из значений для входа.
        3. Кликнуть на кнопку Login.
        Шаги после авторизации:
        1. Нажать кнопку Home.
        2. Проверить, что осуществлен переход на страницу авторизации.
        """
        # Шаги авторизации
        login_page_pl.click_customer_login()
        login_page_pl.select_user()
        login_page_pl.click_login()
        print("Авторизация выполнена")

        # Шаг 1: Нажать кнопку Home
        account_page_pl.click_home()
        print("Шаг 1: Нажата кнопка Home.")

        # Шаг 2: Проверить, что осуществлен переход на страницу авторизации
        login_page_pl.check_url()
        print("Шаг 2: Переход на страницу авторизации выполнен.")

    @allure.story('Тест отображения кнопок на странице аккаунта')
    def test_buttons_visibility(self, login_page_pl, account_page_pl):
        """
        Сценарий: Отображение кнопок на странице аккаунта
        Шаги авторизации:
        1. Нажать кнопку Customer Login.
        2. Кликнуть по селекту и выбрать в селекте одно из значений для входа.
        3. Кликнуть на кнопку Login.
        Шаги после авторизации:
        1. Проверить отображение кнопок Transactions, Deposit, Withdrawl.
        2. Проверить отображение кнопок Home и Logout.
        """
        # Шаги авторизации
        login_page_pl.click_customer_login()
        login_page_pl.select_user()
        login_page_pl.click_login()
        print("Авторизация выполнена: выбран пользователь Harry Potter.")

        # Шаг 1: Проверить отображение кнопок Transactions, Deposit, Withdrawl
        assert account_page_pl.is_visible(BUTTON_TRANSACTIONS_LOCATOR), (
            "Ожидаемый результат: Кнопка Transactions отображается. "
            "Фактический результат: Кнопка Transactions не отобразилась."
        )
        assert account_page_pl.is_visible(BUTTON_DEPOSIT_LOCATOR), (
            "Ожидаемый результат: Кнопка Deposit отображается. "
            "Фактический результат: Кнопка Deposit не отобразилась."
        )
        assert account_page_pl.is_visible(BUTTON_WITHDRAWL_LOCATOR), (
            "Ожидаемый результат: Кнопка Withdrawl отображается. "
            "Фактический результат: Кнопка Withdrawl не отобразилась."
        )
        print("Шаг 1: Кнопки Transactions, Deposit, Withdrawl отображаются.")

        # Шаг 2: Проверить отображение кнопок Home и Logout
        assert account_page_pl.is_visible(BUTTON_HOME_LOCATOR), (
            "Ожидаемый результат: Кнопка Home отображается. "
            "Фактический результат: Кнопка Home не отобразилась."
        )
        assert account_page_pl.is_visible(BUTTON_LOGOUT_LOCATOR), (
            "Ожидаемый результат: Кнопка Logout отображается. "
            "Фактический результат: Кнопка Logout не отобразилась."
        )
        print("Шаг 2: Кнопки Home и Logout отображаются.")
