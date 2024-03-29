import functools

from .constant import loading_time, ad_time, short_ad_time
from .drivers.driver import WebDriver, ElementEnum


# Css selector of elements
class GamerElement(ElementEnum):
    none = None
    login_page = "https://user.gamer.com.tw/login.php"
    main_page = "https://www.gamer.com.tw/"
    username = "input[name='userid']"
    password = "input[name='password']"
    login_button = "a#btn-login"
    sign_in_button = "a#signin-btn"
    get_coin_button = "button.popup-dailybox__btn:not([disabled])"
    start_ad_button = "button[type='submit']"
    ad_iframe = "iframe[id*='videorewarded']"
    close_button1 = "img[src*='close-circle']"
    close_button2 = "div.close_button"
    resume_button = "div[class*='rewardDialogueWrapper']:not([style*='display']) div.rewardResumebutton"
    mute_button = "img[src*='volume_on']"
    lottery_button = "a[class*='c-accent-o']"
    lottery_confirm_radio = "input#agree-confirm"
    lottery_confirm_button = "a[class*='c-primary']"
    submit_button = "button[type='submit']"


class GamerScript:
    config = {}
    browser: WebDriver = None
    cookies: list = None
    is_authenticated = False
    login_page = "https://user.gamer.com.tw/login.php"
    main_page = "https://www.gamer.com.tw/"

    def __init__(self, browser: WebDriver, gamer_config: dict, cookies=None):
        self.browser = browser
        self.config = gamer_config
        self.cookies = cookies
        self.browser.open_browser()

    def login(self):
        self.browser.go_to_page(self.login_page)

        if self.cookies:
            self.browser.load_cookies(self.cookies)
        else:
            self.browser.write_text_into(GamerElement.username, self.config.get("username"))
            self.browser.write_text_into(GamerElement.password, self.config.get("password"))
            self.browser.click(GamerElement.login_button)
        self.is_authenticated = True

    def login_required(func):
        @functools.wraps(func)
        def wrap(self, *args, **kwargs):
            if not self.is_authenticated:
                self.login()
            return func(self, *args, **kwargs)
        return wrap

    @login_required
    def get_coin(self):
        self.browser.go_to_page(self.main_page)
        self.browser.click(GamerElement.sign_in_button)
        if self.browser.try_click(GamerElement.get_coin_button):
            self._watch_ad()

    def _watch_ad(self):
        self.browser.wait(loading_time)
        self.browser.click(GamerElement.start_ad_button)
        self.browser.wait(loading_time)
        self.browser.switch_to_frame(GamerElement.ad_iframe)
        if self.browser.try_click(GamerElement.resume_button):  # for short ad
            self.browser.try_click(GamerElement.mute_button)
            self.browser.wait(short_ad_time)
        else:  # for normal ad
            self.browser.wait(ad_time)
        self.browser.try_click(GamerElement.close_button1)
        self.browser.try_click(GamerElement.close_button2)
        self.browser.switch_to_frame(GamerElement.none)
        self.browser.wait(loading_time)

    @login_required
    def get_lottery(self, lottery_page):
        self.browser.go_to_page(lottery_page)
        if self.browser.try_click(GamerElement.lottery_button):
            self._watch_ad()
            self.browser.click(GamerElement.lottery_confirm_radio)
            self.browser.click(GamerElement.lottery_confirm_button)
            self.browser.click(GamerElement.submit_button)

    def get_lotteries(self):
        lottery_num = self.config.get("lottery_num", 10)
        lottery_pages = self.config.get("lottery_page", [])
        for lottery_page in lottery_pages:
            for num in range(lottery_num):
                self.get_lottery(lottery_page)
