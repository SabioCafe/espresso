from os import environ

from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector import errors

class MySqlDriver():
    """
    MySQL driver class
    """

    def __init__(self):
        """
        Constructor method
        """
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
            self.pool = MySQLConnectionPool(self.config)
            conn1 = self.pool.get_connection()
            print('Connected on conn1:', conn1.connection_id)
        except errors.Error as e:
            print(e)
    
    def lol_test(self):
        """lol teste"""
        print("OK")
