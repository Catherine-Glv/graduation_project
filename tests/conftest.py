import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.transaction_page import TransactionPage

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture(scope="function")
def login_page(page):
    LoginPage(page).open_page()
    return LoginPage(page)

@pytest.fixture(scope="function")
def customer_account_page(page):
    return AccountPage(page)

@pytest.fixture(scope="function")
def transaction_page(page):
    return TransactionPage(page)

@pytest.fixture(scope="function")
def login(login_page):
    login_page.click_customer_login_button()
    login_page.select_customer(customer_name='Ron Weasly')
    login_page.click_login_button()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)
