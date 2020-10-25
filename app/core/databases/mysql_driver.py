"""
MySQL Driver

Docs: https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnectionpool.html
"""
from os import environ

from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector import errors


class MySqlDriver():
    """MySQL driver class"""

    def __init__(self):
        """Constructor"""
        self.config = {
            "host": 'database' if environ.get('APP_ENV') == 'development' else environ.get('MYSQL_HOST'),
            "database": environ.get('MYSQL_DATABASE', 'espresso_db'),
            "user": environ.get('MYSQL_USER', 'root'),
            "password": environ.get('MYSQL_ROOT_PASSWORD', 'strawberry'),
            "port": int(environ.get('MYSQL_PORT', 3306)),
            "pool_name": "mysql_pool",
            "pool_size": 5,
            "pool_reset_session": True,
        }
        try:
            self.cnxpool = MySQLConnectionPool(**self.config)
        except errors.Error as err:
            print(err)

    def check_conn(self):
        """Check database connection"""
        try:
            database = self.cnxpool.get_connection()
            cursor = database.cursor(dictionary=True)
            cursor.execute("SHOW DATABASES;")

            rows = []
            for row in cursor:
                rows.append(row)
            
            return rows
        except errors.Error as err:
            print(err)
            return False
