from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = url

    # def open_url(self):
    #     self.page.goto(self.url)

    def open_url(self, url: str):
        self.page.goto(url)
        # self.page.wait_for_load_state("networkidle")

    def check_url(self):
        assert self.page.url == self.url, (
            f"Ожидаемый URL: {self.url}, Фактический URL: {self.page.url}"
        )

    def click(self, locator: str):
        element = self.page.wait_for_selector(selector=locator)
        element.click()

    def input_text(self, locator: str, text: str):
        element = self.page.wait_for_selector(selector=locator)
        element.fill(value=text)

    def get_text(self, locator: str) -> str:
        element = self.page.wait_for_selector(selector=locator)
        return element.inner_text()

    # def is_visible(self, locator: str) -> bool:
    #     button = self.page.locator(locator)
    #     is_visible = button.is_visible(timeout=5)
    #     if is_visible:
    #         return True
    #     else:
    #         raise Exception('Элемент не отобразился на странице')

    def is_visible(self, locator: str, timeout: int = 10) -> bool:
        button = self.page.locator(selector=locator)
        is_visible = button.is_visible(timeout=timeout * 1000)  # timeout в миллисекундах
        if is_visible:
            return True
        else:
            raise Exception(f'Элемент с локатором "{locator}" не отобразился на странице')

    def is_clickable(self, locator: str) -> bool:
        is_element = self.page.is_enabled(selector=locator)
        if is_element:
            return True
        else:
            raise Exception('Элемент не кликабельный')

    def select_option(self, select_locator: str, option_locator: str):
        select = self.page.locator(selector=select_locator)
        select.click()
        option = self.page.locator(selector=option_locator)
        option.wait_for(state="visible")
        option.click()

    def wait_for_element(self, locator: str, timeout: int = 5000):
        self.page.wait_for_selector(selector=locator, timeout=timeout)

    def check_url(self, expected_url: str):
        assert self.page.url == expected_url, f"Ожидаемый URL: {expected_url}, Фактический URL: {self.page.url}"

    def take_screenshot(self, name: str):
        self.page.screenshot(path=f"screenshots/{name}.png", full_page=True)

    # def is_not_active_field(self, locator: str) -> bool:
    #     is_element = self.page.is_disabled(selector=locator)
    #     if is_element:
    #         return True
    #     else:
    #         raise Exception('Поле активное')