import pytest

from models.models import Access
from mysql_orm_client.mysql_orm_client import MysqlOrmConnection
from tests.builder_orm import MysqlOrmBuilder


class TestMysqlOrm:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_client):
        self.mysql_orm: MysqlOrmConnection = mysql_orm_client
        self.builder_orm: MysqlOrmBuilder = MysqlOrmBuilder(connection=self.mysql_orm)

    def test_mysql_orm(self):
        self.builder_orm.add_log()
        assert len(self.mysql_orm.session.query(Access).all()) > 0
