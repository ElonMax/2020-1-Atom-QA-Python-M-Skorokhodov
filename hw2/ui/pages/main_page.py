from ui.locators.basic_locators import MainPageLocators
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def authorization(self, login='cappukan@gmail.com', password='G456_open'):
        self.click(self.locators.GOTO_LOGIN_BUTTON, 10)
        self.entering(self.locators.EMAIL_FIELD, login, 10)
        self.entering(self.locators.PASSWORD_FIELD, password, 10)
        self.click(self.locators.LOGIN_BUTTON, 10)
