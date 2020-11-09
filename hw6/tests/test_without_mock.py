import time

import pytest

from clients.socket_http_client import SocketClient
from my_app import my_app


class TestWithoutMock:

    @pytest.fixture(scope='class', autouse=True)
    def setup(self):
        my_app.run_app()
        close_func = SocketClient('127.0.0.1', 1050)
        yield
        close_func.get('/shutdown')

    @pytest.fixture(scope='function', autouse=True)
    def client(self):
        self.client = SocketClient('127.0.0.1', 1050)

    def test_status_get(self):
        time.sleep(1)
        assert self.client.get('/')['body'] == 'Mock is down'
