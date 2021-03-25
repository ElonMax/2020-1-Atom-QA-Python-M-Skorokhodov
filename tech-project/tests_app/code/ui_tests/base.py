import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.cabinet_page import CabinetPage
from ui.pages.registration_page import RegistrationPage
from ui.pages.start_page import StartPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.start_page: StartPage = request.getfixturevalue('start_page')
        self.registration_page: RegistrationPage = request.getfixturevalue('registration_page')
        self.cabinet_page: CabinetPage = request.getfixturevalue('cabinet_page')
