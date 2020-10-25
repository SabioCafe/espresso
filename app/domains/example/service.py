"""Example's domain Service Module"""
from urllib.error import HTTPError
from app.core.classes import Service


class ExampleService(Service):
    """Example's Domain Service Class"""

    def get_request(self, params=None):
        """get_request function"""
        try:
            return self.get(f'{params}')

        except HTTPError as err:
            if err.code == 404:
                return None
