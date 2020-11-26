"""app main function."""
from os import environ
import click

from flask import Flask
from flask.cli import FlaskGroup
from app.core.router import urls_example


def create_app():
    """create_app function."""
    app = Flask(__name__)
    # app.config.from_object('config')

    @app.shell_context_processor
    def _shell_context():
        return {"app": app}

    with app.app_context():
        app.register_blueprint(urls_example)

    @app.route("/", methods=["GET"])
    def _index():
        return {"status": 200, "message": "espresso v1.0"}, 200

    return app


cli = FlaskGroup(create_app=create_app)


@cli.command("hello")
@click.option("--name", default="you", help="Your name.")
def custom_command(name):
    """A greet function."""
    print(f"Hello {name}, welcome! I'm {environ.get('APP_QUEUE', 'espresso')}.")


if __name__ == "__main__":
    cli()
