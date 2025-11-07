from typing import Generator

import pytest
from flask import Flask
from flask.testing import FlaskClient

from app import create_app
from config import TestConfig


@pytest.fixture
def app() -> Generator[FlaskClient, None, None]:
    """
    Create and configure a new app instance for each test.

    Returns:
        Flask: The Flask application instance.
    """
    app: Flask = create_app(TestConfig)
    app.config["WTF_CSRF_ENABLED"] = False  # Disable CSRF for testing
    with app.test_client() as client:
        yield client


def test_register_name_required(app: FlaskClient) -> None:
    """
    Test that a register has been given a name on creation

    Args:
        client (FlaskClient): The test client for the Flask application.
    """
    pass
