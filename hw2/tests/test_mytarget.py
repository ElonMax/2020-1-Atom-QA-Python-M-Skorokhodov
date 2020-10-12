import pytest

from tests.base import BaseCase


class Test(BaseCase):
    # @pytest.mark.skip
    def test_login_negative(self):
        self.main_page.authorization('test@mail.ru', '123456')

        assert 'Login attempts limit has been exceeded' in self.driver.page_source

    # @pytest.mark.skip
    def test_login_positive(self, authorization):
        self.cabinet_page.find(self.cabinet_page.locators.TITLE_EMAIL, 10)

    # @pytest.mark.skip
    def test_create_campaign(self, authorization):
        campaign_page = self.cabinet_page.goto_campaign_page()
        campaign_page.create_campaign()
        self.cabinet_page.find(self.cabinet_page.locators.CREATE_CAMPAIGN_STATUS, 10)

    # @pytest.mark.skip
    def test_create_segment(self, authorization):
        segment_page = self.cabinet_page.goto_segment_page()
        segment_page.create_segment()

    # @pytest.mark.skip
    def test_delete_segment(self, authorization):
        segment_page = self.cabinet_page.goto_segment_page()
        segment_page.delete_segment()
