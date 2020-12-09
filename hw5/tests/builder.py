import os

from mysql_client.mysql_client import MysqlConnection


abspath = os.path.abspath('')
curnetpath = 'logs/access.log'
filepath = os.path.join(abspath, curnetpath)


class MysqlBuilder:

    def __init__(self, connection: MysqlConnection):
        self.connection = connection
        self.create_logs()

    def create_logs(self):
        logs = """
        CREATE TABLE IF NOT EXISTS `access`(
        `ip` char(20) NOT NULL,
        `str1` char(20) NOT NULL,
        `str2` char(20) NOT NULL,
        `date` char(30) NOT NULL,
        `gmt` char(20) NOT NULL,
        `request` varchar(1000) NOT NULL,
        `status_code` int NOT NULL,
        `bytes` int NOT NULL,
        `source` varchar(1000) NOT NULL,
        `agent` varchar(1000) NOT NULL,
        `str3` char(20) NOT NULL
        )
        """

        self.connection.execute_query(logs)

    def add_logs(self):
        insert = f"""
        LOAD DATA LOCAL INFILE 
        '{filepath}' 
        INTO TABLE access
        FIELDS TERMINATED BY ' '
        OPTIONALLY ENCLOSED BY '"'
        ESCAPED BY ''
        """
        self.connection.execute_query(insert)
        delete_column = """
        ALTER TABLE access
        DROP COLUMN `str1`,
        DROP COLUMN `str2`,
        DROP COLUMN `str3`,
        DROP COLUMN `source`,
        DROP COLUMN `agent`,
        DROP COLUMN `bytes`,
        DROP COLUMN `gmt`
        """
        self.connection.execute_query(delete_column)
        update_date = """
        UPDATE access
        SET date = REPLACE(date, '[', '')
        """
        self.connection.execute_query(update_date)
        set_index = """
        ALTER TABLE access 
        ADD COLUMN `id` int PRIMARY KEY not null auto_increment FIRST;
        """
        self.connection.execute_query(set_index)
