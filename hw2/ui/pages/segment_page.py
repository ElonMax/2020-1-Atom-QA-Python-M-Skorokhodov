from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from ui.locators.basic_locators import SegmentPageLocators
from ui.pages.base_page import BasePage


class SegmentPage(BasePage):
    locators = SegmentPageLocators()

    def create_segment(self, segment_name='create'):
        try:
            self.click(self.locators.ANOTHER_ADD_SEGMENT_BUTTON, 3)
            self.click(self.locators.ADDING_SEGMENT_ITEM, 10)
        except TimeoutException:
            self.click(self.locators.CREATE_SEGMENT, 5)
        finally:
            self.click(self.locators.CHOOSE_FLAG, 10)
            self.click(self.locators.ADD_SEGMENT_BUTTON, 10)

            self.entering(self.locators.CREATE_SEGMENT_FORM, segment_name, 10)

            self.click(self.locators.CONFIRM_SEGMENT_BUTTON, 10)

            if segment_name == 'create':
                TEMPORARY_NAME = (By.XPATH, f"//a[@title='{segment_name}']")
                self.find(TEMPORARY_NAME, 10)

    def delete_segment(self):
        self.create_segment(segment_name='delete')
        self.click(self.locators.DELETE_SEGMENT, 10)
        self.click(self.locators.CONFIRM_DELETE, 10)
