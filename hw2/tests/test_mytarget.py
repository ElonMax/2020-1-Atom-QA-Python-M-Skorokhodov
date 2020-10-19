import pytest

from tests.base import BaseCase
from ui.locators.basic_locators import DELETE


class Test(BaseCase):
    def test_login_negative(self):
        self.main_page.authorization('test@mail.ru', '123456')

        assert 'Login attempts limit has been exceeded' in self.driver.page_source or 'Invalid login or password' in self.driver.page_source

    def test_login_positive(self, authorization):
        self.cabinet_page.find(self.cabinet_page.locators.TITLE_EMAIL, 10)

    def test_create_campaign(self, authorization):
        campaign_page = self.cabinet_page.goto_campaign_page()
        campaign_page.create_campaign()
        self.cabinet_page.find(self.cabinet_page.locators.CREATE_CAMPAIGN_STATUS, 10)

    def test_create_segment(self, authorization):
        segment_page = self.cabinet_page.goto_segment_page()
        segment_page.create_segment()

    def test_delete_segment(self, authorization):
        segment_page = self.cabinet_page.goto_segment_page()
        segment_page.create_segment(segment_name=DELETE)
        segment_page.delete_segment()
