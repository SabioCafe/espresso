from flask import jsonify
from .Service import FileService


class FileController:
    def __init__(self):
        self._fileService = FileService()

    def mainPage(self):
        return jsonify({"status": 200, "message": "Main Success"})
