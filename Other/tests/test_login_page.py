import allure
import pytest
from playwright.sync_api import Page
from Other.locators.login_page_locators import *

@allure.feature('login_page')
class TestLoginPage:
    @allure.story('Тест успешной авторизации')
    def test_successful_login(self, page, login_page_pl, account_page_pl):
        """
        Сценарий: Успешный вход
        Шаги:
        1. Проверить, что кнопка Customer Login отображается.
        2. Нажать кнопку Customer Login.
        3. Проверить, что отображается селект.
        4. Проверить, что в селекте 5 позиций выбора.
        5. Выбрать в селекте одно из значений для входа.
        6. Проверить, что кнопка Login отображается.
        7. Кликнуть на кнопку Login.
        8. Проверить, что произошел переход на страницу аккаунта.
        """
        # login_page_pl.open_url("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

        # Шаг 1: Проверить, что кнопка Customer Login отображается
        # button = page.BUTTON_LOGIN_LOCATOR
        assert login_page_pl.is_visible(BUTTON_LOGIN_LOCATOR), (
            "Ожидаемый результат: Кнопка Customer Login отображается. "
            "Фактический результат: Кнопка Customer Login не отобразилась."
        )

        # Шаг 2: Нажать кнопку Customer Login
        login_page_pl.click_customer_login()
        print("Шаг 2: Нажата кнопка Customer Login.")

        # Шаг 3: Проверить, что отображается селект
        assert login_page_pl.is_visible(SELECT_LOGIN_ALL_OPTIONS_LOCATOR), (
            "Ожидаемый результат: Селект отображается. "
            "Фактический результат: Селект не отобразился."
        )

        # Шаг 4: Проверить, что в селекте 5 позиций выбора
        options = login_page_pl.locator(SELECT_LOGIN_ALL_OPTIONS_LOCATOR).locator("option")
        assert options.count() == 5, (
            f"Ожидаемый результат: В селекте 5 позиций выбора. "
            f"Фактический результат: В селекте {options.count()} позиций."
        )

        # Шаг 5: Выбрать в селекте третий вариант
        login_page_pl.select_user("Ron Weasly")
        print("Шаг 5: Выбран третий вариант в селекте.")

        # Шаг 6: Проверить, что кнопка Login отображается
        assert login_page_pl.is_visible(BUTTON_LOGIN_WITH_OPTION_LOCATOR), (
            "Ожидаемый результат: Кнопка Login отображается. "
            "Фактический результат: Кнопка Login не отобразилась."
        )

        # Шаг 7: Кликнуть на кнопку Login
        login_page_pl.click_login()
        print("Шаг 7: Нажата кнопка Login.")

        # Шаг 8: Проверить, что произошел переход на страницу аккаунта
        account_page_pl.check_url()
        print("Шаг 2: Переход на страницу аккаунта выполнен.")
