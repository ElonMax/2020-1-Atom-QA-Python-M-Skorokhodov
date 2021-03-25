import allure
from allure_commons.types import AttachmentType
from faker import Faker

from clients.api_client.myapp_client import ApiClient
from clients.mysql_orm_client.builder import MysqlOrmBuilder
from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--url', default='http://0.0.0.0:7070')
    parser.addoption('--browser', default='chromium')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--selenoid')


def pytest_exception_interact(node, call, report):
    try:
        driver = node.instance.driver
        allure.attach(
            name='Screenshot',
            body=driver.get_screenshot_as_png(),
            attachment_type=AttachmentType.PNG,
        )
    except:
        pass


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    selenoid = request.config.getoption('--selenoid')

    return {'browser': browser, 'version': version, 'url': url, 'selenoid': selenoid}


@pytest.fixture(scope='function')
def fake_data():
    fake = Faker()
    return {'username': ('t_' + fake.user_name())[:16],
            'email': fake.email(),
            'password': fake.password()}


@pytest.fixture(scope='function')
def another_fake():
    a_fake = Faker()
    return {'username': ('t_' + a_fake.user_name())[:16],
            'email': a_fake.email(),
            'password': a_fake.password()}


@pytest.fixture(scope='function')
def api_client():
    return ApiClient()


@pytest.fixture(scope='function')
def autorization_api(fake_data, api_client):
    MysqlOrmBuilder().add_user(username=fake_data['username'],
                               password=fake_data['password'],
                               email=fake_data['email'])
    api_client.login(username=fake_data['username'],
                     password=fake_data['password'])

    return api_client
