"""Repository Module"""
from app.core.databases import MySqlDriver


class Repository():
    """Repository Super Class"""

    def __init__(self, table: str = None):
        """Constructor"""
        self.database = MySqlDriver()
        self.table = table
