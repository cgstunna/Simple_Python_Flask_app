from flask import Flask, jsonify
from typing import Dict, Tuple


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def health() -> Tuple[Dict[str, str], int]:
        return jsonify({"status": "ok", "message": "Flask CI/CD demo"}), 200

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
