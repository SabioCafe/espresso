"""Exemple's Domain Repository Module"""
from app.core.classes import Repository


class ExempleRepository(Repository):
    """ExmpleRepository Class"""

    def __init__(self):
        """Constructor"""
        super().__init__(table="example_table")
