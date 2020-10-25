"""Example's domain Controller Module"""
from flask import jsonify
from .service import ExampleService


class ExampleController:
    """Example's Domain Controller Class"""
    def __init__(self):
        """Constructor"""
        self.file_service = ExampleService()

    def main_page(self):
        """main_page function"""
        return jsonify({"status": 200, "message": "Main Success"})

    def check_conn(self):
        """main_page function"""
        response = self.file_service.check_conn()
        return jsonify({"status": 200, "message": response})