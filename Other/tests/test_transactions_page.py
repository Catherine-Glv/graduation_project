import allure
import pytest
from Other.locators.table_transactions_locators import *

@allure.feature('transactions_page')
class TestTransactionsPage:
    @allure.story('Тест отображения таблицы транзакций')
    def test_transactions_table(self, page, login_page_pl, account_page_pl, transactions_page_pl):
        """
        Сценарий: Отображение таблицы транзакций
        Шаги авторизации:
        1. Нажать кнопку Customer Login.
        2. Кликнуть по селекту и выбрать в селекте одно из значений для входа.
        3. Кликнуть на кнопку Login.
        Шаги после авторизации:
        1. Нажать на кнопку Transactions на странице аккаунта.
        2. Проверить переход на страницу с таблицей транзакций.
        3. Проверить отображение таблицы.
        4. Проверить отображение строк с транзакциями в таблице.
        5. Нажать кнопку Reset.
        6. Проверить, что строки из таблицы очистились.
        7. Нажать на кнопку Back.
        8. Проверить, что вернулись на страницу аккаунта.
        """
        # Шаги авторизации
        login_page_pl.click_customer_login()
        login_page_pl.select_user("Ron Weasly")
        login_page_pl.click_login()
        print("Авторизация выполнена")

        # Шаг 1: Нажать на кнопку Transactions на странице аккаунта
        account_page_pl.click_transactions()
        print("Шаг 1: Нажата кнопка Transactions.")

        # Шаг 2: Проверить переход на страницу с таблицей транзакций
        transactions_page_pl.check_url()
        print("Шаг 2: Переход на страницу с таблицей транзакций выполнен.")

        # Шаг 3: Проверить отображение таблицы
        assert transactions_page_pl.is_transaction_table_visible(), (
            "Ожидаемый результат: Таблица транзакций отображается. "
            "Фактический результат: Таблица транзакций не отобразилась."
        )
        print("Шаг 3: Таблица транзакций отображается.")

        # Шаг 4: Проверить отображение строк с транзакциями в таблице
        transactions_page_pl.wait_for_element(TABLE_ROWS_LOCATOR)
        rows = transactions_page_pl.locator(TABLE_ROWS_LOCATOR).count()
        assert rows > 0, (
            f"Ожидаемый результат: Таблица содержит хотя бы одну строку. "
            f"Фактический результат: Таблица содержит {rows} строк."
        )
        print(f"Шаг 4: В таблице отображается {rows} строк транзакций.")

        # Шаг 5: Нажать кнопку Reset
        transactions_page_pl.click_reset()
        print("Шаг 5: Нажата кнопка Reset.")

        # Шаг 6: Проверить, что строки из таблицы очистились
        rows_after_reset = transactions_page_pl.locator(TABLE_ROWS_LOCATOR).count()
        assert rows_after_reset == 0, (
            f"Ожидаемый результат: Таблица очищена (0 строк). "
            f"Фактический результат: Таблица содержит {rows_after_reset} строк."
        )
        print("Шаг 6: Таблица очищена, строки транзакций отсутствуют.")

        # Шаг 7: Нажать на кнопку Back
        transactions_page_pl.click_back()
        print("Шаг 7: Нажата кнопка Back.")

        # Шаг 8: Проверить, что вернулись на страницу аккаунта
        account_page_pl.check_url()
        print("Шаг 2: Переход на страницу аккаунта выполнен.")
