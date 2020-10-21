import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType

from ui.pages.base_page import BasePage
from ui.pages.cabinet_page import CabinetPage
from ui.pages.campaign_page import CampaignPage
from ui.pages.main_page import MainPage
from ui.pages.segment_page import SegmentPage


class WrongBrowserException(Exception):
    pass


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def cabinet_page(driver):
    return CabinetPage(driver=driver)


@pytest.fixture
def campaign_page(driver):
    return CampaignPage(driver=driver)


@pytest.fixture
def segment_page(driver):
    return SegmentPage(driver=driver)


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']
    selenoid = config['selenoid']

    if selenoid:
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "80.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }

        driver = webdriver.Remote(
            command_executor="http://" + selenoid + "/wd/hub",
            desired_capabilities=capabilities)

    elif browser == 'chrome':
        manager = ChromeDriverManager()
        driver = webdriver.Chrome(executable_path=manager.install())

    elif browser == 'firefox':
        manager = GeckoDriverManager()
        driver = webdriver.Firefox(executable_path=manager.install())

    elif browser == 'chromium':
        manager = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM)
        driver = webdriver.Chrome(executable_path=manager.install())

    else:
        raise WrongBrowserException('Неправльный браузер')

    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def authorization(driver):
    MainPage(driver).authorization()
