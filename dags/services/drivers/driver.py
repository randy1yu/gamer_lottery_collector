from abc import abstractmethod
from enum import Enum


class ElementEnum(Enum):
    pass


class WebDriver:
    driver = None

    def __init__(self):
        pass

    @abstractmethod
    def open_browser(self):
        raise NotImplementedError()

    @abstractmethod
    def close_browser(self):
        raise NotImplementedError()

    @abstractmethod
    def go_to_page(self, url: str):
        raise NotImplementedError()

    @abstractmethod
    def find_element(self, el: ElementEnum):
        raise NotImplementedError()

    @abstractmethod
    def write_text_into(self, el: ElementEnum, value):
        raise NotImplementedError()

    @abstractmethod
    def click(self, el: ElementEnum):
        raise NotImplementedError()

    @abstractmethod
    def get_cookies(self):
        raise NotImplementedError()

    @abstractmethod
    def load_cookies(self, cookies):
        raise NotImplementedError()

    @abstractmethod
    def wait(self, seconds):
        raise NotImplementedError()

    @abstractmethod
    def switch_to_frame(self, el: ElementEnum):
        raise NotImplementedError()

    @abstractmethod
    def try_click(self, el: ElementEnum):
        raise NotImplementedError()

