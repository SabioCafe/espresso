from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)
    #app.config.from_object('config')

    with app.app_context():
        from src.app.Router import file_urls
        app.register_blueprint(file_urls)

    @app.route('/', methods=['GET'])
    def _index():
        return jsonify({"status": 200, "message": "espresso v1.0"})

    return app
