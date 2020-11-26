"""Example domain Controller Module."""
from .service import ExampleService


class ExampleController:
    """Example's Domain Controller Class."""

    def __init__(self):
        """Constructor-Example Controller."""
        self.file_service = ExampleService()

    @staticmethod
    def main_page():
        """main_page function."""
        return {"status": 200, "message": "Main Success"}, 200

    def check_databases(self):
        """main_page function."""
        response = self.file_service.show_databases()
        return {"status": 200, "message": response}, 200
