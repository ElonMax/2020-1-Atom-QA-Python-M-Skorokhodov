from models.models import Base, Access
from mysql_orm_client.mysql_orm_client import MysqlOrmConnection


class MysqlOrmBuilder:
    def __init__(self, connection: MysqlOrmConnection):
        self.connection = connection
        self.engine = self.connection.connection.engine

        self.create_access()

    def create_access(self):
        if not self.engine.dialect.has_table(self.engine, 'access'):
            Base.metadata.tables['access'].create(self.engine)

    def add_log(self):
        access = Access(
            ip='134.249.53.185',
            date='27/May/2016:03:32:09',
            request='POST http://almhuette-raith.at/administrator/index.php HTTP/1.1',
            status_code=200
        )

        self.connection.session.add(access)
        self.connection.session.commit()

        return access
