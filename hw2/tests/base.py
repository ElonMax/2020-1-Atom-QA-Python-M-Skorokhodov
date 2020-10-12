import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.campaign_page import CampaignPage
from ui.pages.main_page import MainPage
from ui.pages.cabinet_page import CabinetPage
from ui.pages.segment_page import SegmentPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.cabinet_page: CabinetPage = request.getfixturevalue('cabinet_page')
        self.campaign_page: CampaignPage = request.getfixturevalue('campaign_page')
        self.segment_page: SegmentPage = request.getfixturevalue('segment_page')
