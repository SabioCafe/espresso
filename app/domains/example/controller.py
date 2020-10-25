"""Example's domain Controller Module"""
from flask import jsonify
from .service import ExampleService


class ExampleController:
    """Example's Domain Controller Class"""

    def __init__(self):
        """Constructor"""
        self.file_service = ExampleService()

    @staticmethod
    def main_page():
        """main_page function"""
        return jsonify({"status": 200, "message": "Main Success"})

    def check_databases(self):
        """main_page function"""
        response = self.file_service.show_databases()
        return jsonify({"status": 200, "message": response})
