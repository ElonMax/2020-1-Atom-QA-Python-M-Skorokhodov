from selenium.common.exceptions import TimeoutException

from ui.locators.basic_locators import RegistrationPageLocators
from ui.pages.base_page import BasePage


class ValidException(Exception):
    pass


class RegistrationPage(BasePage):
    locators = RegistrationPageLocators()

    def check_valid_registration_page(self):
        try:
            self.find(self.locators.REGISTRATION_USERNAME, 2)
            self.find(self.locators.REGISTRATION_PASSWORD, 2)
            self.find(self.locators.REGISTRATION_EMAIL_VALID, 2)
            self.find(self.locators.REGISTRATION_CONFIRM_PASSWORD_VALID, 2)
            self.find(self.locators.TERM_BUTTON, 2)
        except TimeoutException:
            raise ValidException('Валидация не пройдена')

    def do_registration(self, username, email, password, confirm):
        self.click(self.locators.REGISTRATION_USERNAME, 2)
        self.entering(self.locators.REGISTRATION_USERNAME, username, 2)
        self.click(self.locators.REGISTRATION_EMAIL, 2)
        self.entering(self.locators.REGISTRATION_EMAIL, email, 2)
        self.click(self.locators.REGISTRATION_PASSWORD, 2)
        self.entering(self.locators.REGISTRATION_PASSWORD, password, 2)
        self.click(self.locators.REGISTRATION_CONFIRM_PASSWORD, 2)
        self.entering(self.locators.REGISTRATION_CONFIRM_PASSWORD, confirm, 2)
        self.click(self.locators.TERM_BUTTON, 2)
        self.click(self.locators.DO_REGISTRATION_BUTTON, 2)
