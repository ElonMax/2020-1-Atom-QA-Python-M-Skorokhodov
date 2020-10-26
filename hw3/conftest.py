import pytest

from api.mytarget_client import ApiClient


@pytest.fixture(scope='function')
def api_client():
    user = 'cappukan@gmail.com'
    password = 'G456_open'

    return ApiClient(user, password)
