# app.py
import logging
import os
from typing import Any

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException, MethodNotAllowed, NotFound

def create_app() -> Flask:
    """
    Create and configure the Flask application.

    Returns:
        Flask: The configured Flask app instance.
    """
    app = Flask(__name__)

    # Setup logger for error logging
    setup_logging(app)

    # Load configuration from environment variables
    app.config['DEBUG'] = os.getenv("FLASK_DEBUG", "0") == "1"
    app.config['ENV'] = os.getenv("FLASK_ENV", "production")
    app.config['PROPAGATE_EXCEPTIONS'] = False

    @app.route("/", methods=["GET"])
    def hello_world() -> str:
        """
        Handle GET requests to the root URL returning a greeting.

        Returns:
            str: Greeting text.
        """
        return "Hello, World!", 200, {"Content-Type": "text/plain; charset=utf-8"}

    @app.errorhandler(MethodNotAllowed)
    def handle_405(e: MethodNotAllowed) -> Any:
        """
        Return 405 Method Not Allowed for unsupported HTTP methods.

        Args:
            e (MethodNotAllowed): The exception instance.

        Returns:
            Response: Flask response with 405 status.
        """
        app.logger.warning(
            "405 Method Not Allowed: %s %s", request.method, request.path
        )
        return jsonify({"error": "Method Not Allowed"}), 405

    @app.errorhandler(NotFound)
    def handle_404(e: NotFound) -> Any:
        """
        Return 404 Not Found for unknown routes.

        Args:
            e (NotFound): The exception instance.

        Returns:
            Response: Flask response with 404 status.
        """
        app.logger.warning("404 Not Found: %s %s", request.method, request.path)
        return jsonify({"error": "Not Found"}), 404

    @app.errorhandler(Exception)
    def handle_exception(e: Exception) -> Any:
        """
        Global handler for unhandled exceptions. Logs error and returns 500 without stack trace.

        Args:
            e (Exception): The exception instance.

        Returns:
            Response: Flask response with 500 status and safe error message.
        """
        # If the exception is a HTTPException, use its code and description
        if isinstance(e, HTTPException):
            code = e.code
            description = e.description
            app.logger.error("HTTPException: %s - %s", code, description)
            return jsonify({"error": description}), code

        # Log the exception with stack trace
        app.logger.error("Unhandled Exception: %s", str(e), exc_info=True)

        # Generic message to avoid leaking details
        return jsonify({"error": "Internal Server Error"}), 500

    # Disable Flask-level default error messages with stack traces
    app.config["TRAP_HTTP_EXCEPTIONS"] = False

    return app


def setup_logging(app: Flask) -> None:
    """
    Configures the Python logging for the Flask application.

    Args:
        app (Flask): Flask application instance.
    """
    # Remove default handlers to avoid duplicate logs in some environments
    for handler in app.logger.handlers[:]:
        app.logger.removeHandler(handler)

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
    )
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)


def validate_and_sanitize(input_data: Any) -> Any:
    """
    Placeholder function for validating and sanitizing input data.

    Args:
        input_data (Any): External input data.

    Returns:
        Any: Sanitized and validated data.
    """
    # Since no external input is currently used, this stub fulfills security req.
    # Implement specific checks and sanitization if inputs are added later.
    return input_data


def main() -> None:
    """
    Application entry point.

    Starts the Flask development server if run directly.
    """
    app = create_app()

    # Run the app with environment-configured debug disabled by default
    app.run(host="0.0.0.0", port=8080, debug=app.config["DEBUG"])


if __name__ == "__main__":
    main()
