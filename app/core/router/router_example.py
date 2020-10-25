"""Example Domain's Router File"""
from flask import Blueprint
from app.domains import ExampleController

example_controller = ExampleController()
file_urls = Blueprint('router_example', __name__)


@file_urls.route('/main', methods=['GET'])
def main():
    """Main Function"""
    return example_controller.main_page()
