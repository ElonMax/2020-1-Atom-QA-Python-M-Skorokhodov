from ui.locators.basic_locators import CabinetPageLocators
from ui.pages.base_page import BasePage
from ui.pages.campaign_page import CampaignPage
from ui.pages.segment_page import SegmentPage


class CabinetPage(BasePage):
    locators = CabinetPageLocators()

    def goto_campaign_page(self):
        self.click(self.locators.NEW_COMPANY_BUTTON, 10)
        return CampaignPage(self.driver)

    def goto_segment_page(self):
        self.click(self.locators.NEW_SEGMENT_BUTTON, 10)
        return SegmentPage(self.driver)
