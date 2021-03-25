import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType

from ui.pages.base_page import BasePage
from ui.pages.cabinet_page import CabinetPage
from ui.pages.registration_page import RegistrationPage
from ui.pages.start_page import StartPage


class WrongBrowserException(Exception):
    pass


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def start_page(driver):
    return StartPage(driver=driver)


@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver=driver)


@pytest.fixture
def cabinet_page(driver):
    return CabinetPage(driver=driver)


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']
    selenoid = config['selenoid']

    if selenoid:
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "87.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False,
                "applicationContainers": ["start_app_myapp_1:myapp"],
                "additionalNetworks": ['test']
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
        raise WrongBrowserException('Wrong browser')

    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()
