
from flask import Blueprint, request
from flask import current_app as app


from src.Domains import ExampleController

from csv import DictReader

exampleController = ExampleController()
file_urls = Blueprint('RouterExample', __name__)


@file_urls.route('/main', methods=['GET'])
def main():
    return exampleController.mainPage()
