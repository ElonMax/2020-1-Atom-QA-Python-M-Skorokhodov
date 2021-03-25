from selenium.common.exceptions import TimeoutException

from ui.locators.basic_locators import StartPageLocators
from ui.pages.base_page import BasePage


class ValidException(Exception):
    pass


class StartPage(BasePage):
    locators = StartPageLocators()

    def autorization(self, user, password):
        self.click(self.locators.USERNAME, 2)
        self.entering(self.locators.USERNAME, user, 2)
        self.click(self.locators.PASSWORD, 2)
        self.entering(self.locators.PASSWORD, password, 2)
        self.click(self.locators.LOGIN_BUTTON, 2)

    def check_valid_start_page(self):
        try:
            self.find(self.locators.USERNAME, 2)
            self.find(self.locators.PASSWORD, 2)
        except TimeoutException:
            raise ValidException('Валидация не пройдена')

    def go_to_registration_page(self):
        self.click(self.locators.REGISTER_BUTTON, 5)
