from ui.locators.basic_locators import CabinetPageLocators
from ui.pages.base_page import BasePage


class CabinetPage(BasePage):
    locators = CabinetPageLocators()

    def go_outside_hide(self, locator_main, locator_hide):
        self.select_to_hidden(locator_main,
                              locator_hide)
        self._switch_to_second_tab()

    def go_outside_main(self, locator):
        self.click(locator, 2)
        self._switch_to_second_tab()
