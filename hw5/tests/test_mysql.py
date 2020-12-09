import pytest

from mysql_client.mysql_client import MysqlConnection
from tests.builder import MysqlBuilder


class TestMysql:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql: MysqlConnection = mysql_client
        self.builder = MysqlBuilder(self.mysql)

    def test_create_logs_mysql(self):
        self.builder.add_logs()
        assert len(self.mysql.execute_query('SELECT * FROM access')) > 0
