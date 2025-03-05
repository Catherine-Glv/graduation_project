class AccountPageLocators:
    CUSTOMER_NAME = "//span[@class='fontBig ng-binding']"
    LOGOUT_BUTTON = "//button[@class='btn logout']"
    TRANSACTIONS_BUTTON = "//button[@ng-class='btnClass1']"
    DEPOSIT_BUTTON = "//button[@ng-class='btnClass2']"
    WITHDRAWL_BUTTON = "//button[@ng-class='btnClass3']"
    AMOUNT_INPUT = "//input[@type='number']"
    SUBMIT_DEPOSIT = "//button[@class='btn btn-default']"
    MESSAGE = "//span[@ng-show='message']"
    ACCOUNT_SELECTOR = "//select[@id='accountSelect']"
    ACCOUNT_NUMBER = "#accountSelect > option:nth-child(2)"
    ACCOUNT_NUMBER_1007 = "#accountSelect > option:nth-child(1)"
    BALANCE = "//strong[@class='ng-binding'][2]"

