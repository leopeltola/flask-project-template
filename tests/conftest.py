from os import environ

import pytest

from app import create_app


class TestConfig:
    SECRET_KEY = environ.get("SECRET_KEY") or "super-secret-key"
    TESTING = True


@pytest.fixture
def client():
    app = create_app(TestConfig)

    with app.test_client() as client:
        with app.app_context():
            pass
        yield client
