import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from .driver import WebDriver, ElementEnum


class SeleniumDriver(WebDriver):
    driver = None

    def __init__(self):
        super().__init__()

    def open_browser(self):
        self.driver = webdriver.Chrome()

    def close_browser(self):
        self.driver.quit()

    def go_to_page(self, page_url: str):
        self.driver.get(page_url)

    def find_element(self, el: ElementEnum):
        return self.driver.find_element(By.CSS_SELECTOR, el.value)

    def write_text_into(self, el: ElementEnum, text):
        self.find_element(el).send_keys(text)

    def click(self, el: ElementEnum):
        self.find_element(el).click()

    def get_cookies(self):
        return self.driver.get_cookies()

    def load_cookies(self, cookies):
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def wait(self, seconds):
        time.sleep(seconds)

    def switch_to(self, el: ElementEnum):
        if el.value:
            self.driver.switch_to.frame(self.find_element(el))
        else:
            self.driver.switch_to.default_content()

    def try_click(self, el: ElementEnum) -> bool:
        try:
            self.click(el)
            return True
        except Exception as ex:
            print(ex)
            print(f"fail to click {el.value}")
            return False
