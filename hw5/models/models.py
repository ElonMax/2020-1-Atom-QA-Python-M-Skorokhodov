from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Access(Base):
    __tablename__ = 'access'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(20), nullable=False)
    date = Column(String(30), nullable=False)
    request = Column(String(1000), nullable=False)
    status_code = Column(Integer, nullable=False)
