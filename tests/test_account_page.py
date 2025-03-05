import allure

@allure.feature("Проверка взноса Deposit")
class TestDeposit:
    @allure.story('Взнос успешен')
    def test_successful_deposit(self, customer_account_page, login):
        with allure.step('Ввод суммы депозита'):
            customer_account_page.make_deposit("100")
            expected_balance = "100"
            actual_balance = customer_account_page.get_balance()
            assert expected_balance == actual_balance, f'Ожидаемый баланс: 100. Актуальный баланс: {actual_balance}'

@allure.feature("Проверка взноса Withdrawl")
class TestWithdrawl:
    @allure.story('Успешный вывод средств')
    def test_successful_withdrawal(self, customer_account_page, login):
        with allure.step('Ввод суммы депозита'):
            customer_account_page.make_deposit("50")

        with allure.step('Ввод суммы вывода'):
            customer_account_page.make_withdrawl("20")
            expected_balance = "30"
            actual_balance = customer_account_page.get_balance()
            assert expected_balance == actual_balance, f'Ожидаемый баланс: 30. Актуальный баланс: {actual_balance}'


@allure.feature("Проверка смены account number")
class TestAccountNumber:
    @allure.story("Успешная смена account_number")
    def test_select_account_number(self, customer_account_page, login):
        with allure.step("Смена account number"):
            expected_account_number = "1008"
            assert customer_account_page.select_account_number(expected_account_number)
            actual_account_number = customer_account_page.get_account_number()
            assert expected_account_number == actual_account_number, f"Выбран неверный account number. " \
                                                                     f"Текущий account number: {actual_account_number}"

    @allure.story("Успешная смена account_number на предыдущий номер")
    def test_change_account_number(self, customer_account_page, login):
        with allure.step("Смена account number на предыдущий"):
            expected_account_number = "1007"
            assert customer_account_page.select_account_number(expected_account_number)
            actual_account_number = customer_account_page.change_account_number()
            assert expected_account_number == actual_account_number, f"Выбранный неверный account number. " \
                                                                     f"Текущий account number: {actual_account_number}"
