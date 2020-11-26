"""Example Domain's Router File."""
from flask import Blueprint

from app.domains import ExampleController

example_controller = ExampleController()
urls = Blueprint("router_example", __name__)


@urls.route("/main", methods=["GET"])
def main():
    """Router Main Function."""
    return example_controller.main_page()


@urls.route("/check_db", methods=["GET"])
def check_db():
    """List available databases."""
    return example_controller.check_databases()
