from flask import jsonify
from .Service import ExampleService


class ExampleController:
    def __init__(self):
        self._fileService = ExampleService()

    def mainPage(self):
        return jsonify({"status": 200, "message": "Main Success"})
