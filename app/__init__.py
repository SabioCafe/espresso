"""app main function"""
from flask import Flask, jsonify

from app.core.router import file_urls


def create_app():
    """create_app function"""
    app = Flask(__name__)
    #app.config.from_object('config')

    with app.app_context():
        app.register_blueprint(file_urls)

    @app.route('/', methods=['GET'])
    def _index():
        return jsonify({"status": 200, "message": "espresso v1.0"})

    return app
