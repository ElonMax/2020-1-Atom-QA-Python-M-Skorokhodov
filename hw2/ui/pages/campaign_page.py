import os

from ui.locators.basic_locators import CampaignPageLocators
from ui.pages.base_page import BasePage


class CampaignPage(BasePage):
    locators = CampaignPageLocators()

    def create_campaign(self):
        trace = os.path.abspath('')
        new_trace = os.path.join(trace, 'images/933-300x500.jpg')

        self.click(self.locators.TRAFFIC, 10)
        self.entering(self.locators.SITE_FIELD, 'https://steamcommunity.com', 10)
        self.click(self.locators.BANNER, 10)
        self.entering(self.locators.UPLOAD_FILE, new_trace, 10)
        self.click(self.locators.SAVE_IMAGE, 10)
        self.find(self.locators.LOAD_STATUS, 10)
        self.click(self.locators.CREATE_CAMPAIGN, 10)
