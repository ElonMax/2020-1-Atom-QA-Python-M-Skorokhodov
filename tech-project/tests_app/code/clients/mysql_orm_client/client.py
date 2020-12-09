import sqlalchemy
from sqlalchemy.orm import sessionmaker


class MysqlOrmConnection:

    def __init__(self, user, password, db_name):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = '127.0.0.1'
        self.port = 3306

        self.connection = self.connect()
        session = sessionmaker(bind=self.connection)
        self.session = session()

    def connect(self):
        engine = sqlalchemy.create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{db}'.format(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            db=self.db_name
        ))

        return engine.connect()
