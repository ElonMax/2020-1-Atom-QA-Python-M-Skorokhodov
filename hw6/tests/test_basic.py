import pytest

from clients.socket_http_client import SocketClient
from mocks.mock_http_server import MyHTTPServer
from my_app import my_app


class TestApplication:

    @pytest.fixture(scope='class', autouse=True)
    def setup(self):
        my_app.run_app()
        my_mock = MyHTTPServer('127.0.0.1', 1052)
        my_mock.start()
        close_func = SocketClient('127.0.0.1', 1050)
        yield
        close_func.get('/shutdown')
        my_mock.stop()

    @pytest.fixture(scope='function', autouse=True)
    def client(self):
        self.client = SocketClient('127.0.0.1', 1050)

    def test_status_get(self):
        assert self.client.get('/')['status_code'] == 200

    def test_ok(self):
        self.client.put('/data_put', 'name=max')
        assert self.client.post('/data_post', 'name=max')['body'] == 'OK'

    def test_dont_ok(self):
        assert self.client.post('/data_post', 'name=oleg')['body'] == 'DONT OK'

    def test_put(self):
        self.client.put('/data_put', 'name=dima')
        assert 'dima' in self.client.get('/')['body']

    def test_not_found(self):
        assert self.client.get('/fake')['status_code'] == 404

    def test_mock_500(self):
        assert self.client.get('/500')['status_code'] == 424
