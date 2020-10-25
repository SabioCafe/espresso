"""Service Module"""
from urllib import request as http


class Service():
    """Service Super Class"""

    def __init__(self):
        self._endpoint = r'https://localhost:4000'
        # todo: add headers (instance of Request class)

    def get(self, params=None):
        """GET method from Service Super Class"""
        return http.urlopen(f'{self._endpoint}{params}')