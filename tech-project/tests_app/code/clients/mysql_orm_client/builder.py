from clients.mysql_orm_client.client import MysqlOrmConnection
from clients.mysql_orm_client.models import TestUsers
from sqlalchemy.sql import select


class MysqlOrmBuilder:

    def __init__(self):
        self.connection = MysqlOrmConnection(user='root', password='pass', db_name='test')

    def add_user(self, username, password, email, access=1):
        test_users = TestUsers(
            username=username,
            password=password,
            email=email,
            access=access
        )

        self.connection.session.add(test_users)
        self.connection.session.commit()

        return test_users

    def select_from_table(self, username):
        return self.connection.session.query(TestUsers).filter(TestUsers.username == username).first()

    def drop_access(self, username):
       user = self.connection.session.query(TestUsers).filter(TestUsers.username == username).first()
       user.access = 0
       self.connection.session.commit()
