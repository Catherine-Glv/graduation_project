import time
import allure

from locators.transaction_page_locators import TransactionPageLocators

@allure.feature("Проверка таблицы в Transactions")
class TestTransactions:
    @allure.story('Проверка наличия транзакций в таблице')
    def test_transaction_count(self, customer_account_page, transaction_page, login):
        with (allure.step('Взнос депозита и вывод')):
            customer_account_page.make_deposit("50")
            customer_account_page.make_withdrawl("20")
            time.sleep(5)

        with (allure.step('Переход на страницу с транзакциями')):
            customer_account_page.click_transaction_button()
            time.sleep(5)
            assert transaction_page.element_is_visible(locator=TransactionPageLocators.TRANSACTION_TABLE), (f'Переход '
                                                                                                    f'не осуществлен')
        with allure.step('Проверка транзакций в списке'):
            transaction_count = transaction_page.get_transaction_count()
            assert transaction_count == 2, 'Имеются транзакции'

    @allure.feature("Проверка пустой таблицы в Transactions")
    class TestTransactions:
        @allure.story('Проверка наличия транзакций в таблице')
        def test_transaction_count(self, customer_account_page, transaction_page, login):
            with ((allure.step('Переход на страницу с транзакциями'))):
                customer_account_page.click_transaction_button()
                time.sleep(5)
                assert transaction_page.element_is_visible(locator=TransactionPageLocators.TRANSACTION_TABLE),(f'Переход'
                                                                                                               f' не '
                                                                                                               f'осуществлен')
            with allure.step('Проверка транзакций в списке'):
                transaction_count = transaction_page.get_transaction_count()
                assert transaction_count > 0, 'Список транзакций пуст'

    @allure.story('Проверка очистки списка транзакций')
    def test_reset_transactions(self, customer_account_page, transaction_page, login):
        with (allure.step('Взнос депозита и вывод')):
            customer_account_page.make_deposit("50")
            customer_account_page.make_withdrawl("20")
            time.sleep(5)

        with allure.step('Переход на страницу с транзакциями'):
            customer_account_page.click_transaction_button()

        with allure.step('Очистка списка транзакций'):
            customer_account_page.reload_page()
            transaction_page.click_reset()
            transaction_count = transaction_page.get_transaction_count()
            assert transaction_count == 0, f"Список транзакций не очистился, кол-во транзакций: {transaction_count}"