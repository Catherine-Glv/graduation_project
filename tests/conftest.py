from playwright.sync_api import sync_playwright, Page


from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.transactions_page import TransactionsPage
import pytest
import allure

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope='function')
def page(browser):
    page = browser.new_page()
    page.goto(url='https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
    page.wait_for_load_state("networkidle")
    assert "XYZ Bank" in page.title()
    yield page
    page.close()


@pytest.fixture()
def login_page_pl(page):
    login_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    return LoginPage(page, login_url)


@pytest.fixture()
def account_page_pl(page):
    account_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account"
    return AccountPage(page, account_url)

@pytest.fixture()
def transactions_page_pl(page):
    transactions_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx"
    return TransactionsPage(page, transactions_url)
