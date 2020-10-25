"""Example's domain Service Module"""
from urllib.error import HTTPError
from app.core.classes import Service
from .repository import ExempleRepository


class ExampleService(Service):
    """Example's Domain Service Class"""
    def __init__(self):
        self.repository = ExempleRepository()

    def get_request(self, params=None):
        """get_request function"""
        try:
            return self.get(f'{params}')

        except HTTPError as err:
            if err.code == 404:
                return None
    
    def check_conn(self):
        """check database connection"""
        return self.repository.check_conn()
