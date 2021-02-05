"""app main function."""
from flask import Flask
from flask.cli import FlaskGroup
from app.core.router import urls_example
from app.core.cli import greet


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

cli.add_command(greet)


# if __name__ == "__main__":
#     cli()
