"""Exemple's Domain Repository Module."""
from app.core.classes import Repository


class ExempleRepository(Repository):
    """Exmple-Repository Class."""

    def __init__(self):
        """Example-Repository Constructor."""
        super().__init__(table="example_table")
