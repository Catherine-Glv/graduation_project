import allure


@allure.feature("Проверка авторизации")
class TestLoginPage:
    @allure.story('Проверка успешного входа')
    def test_successful_login(self, login_page, customer_account_page):
        with allure.step('Выбор пользователя'):
            login_page.click_customer_login_button()
            assert login_page.select_customer(customer_name='Ron Weasly')

        with allure.step('Проверка входа под выбранным пользователем'):
            login_page.click_login_button()
            expected_customer_name = 'Ron Weasly'
            actual_customer_name = customer_account_page.get_customer_name()
            assert expected_customer_name == actual_customer_name, (f'Имя пользователя на странице не соответствует '
                                                                    f'выбранному. Имя пользователя выбрано:'
                                                                    f' {actual_customer_name}')
            print("Проверка входа")

    @allure.story('Проверка перехода по клику кнопки Home')
    def test_move_to_home(self, login_page, customer_account_page, login):
        with allure.step('Клик по кнопке Home и проверка редиректа на страницу для входа'):
            login_page.click_home_button()
            expected_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
            actual_url = login_page.get_current_url()
            assert expected_url == actual_url, f"Редирект произошел на страницу {actual_url}"
            print("Клик по кнопке Home")

    @allure.story('Проверка выхода из аккаунта')
    def test_successful_logout(self, login_page, customer_account_page):
        login_page.login(customer_name='Harry Potter')
        print("Авторизация под пользователем Harry Potter")

        with allure.step('Разлогин из аккаунта'):
            customer_account_page.logout()
            current_location = login_page.get_current_url()
            expected_location = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'
            assert current_location == expected_location, (f'Разлогин не произошел. '
                                                           f'Фактическая страница расположения: {current_location}')
