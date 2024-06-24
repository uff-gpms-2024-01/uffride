import pytest
from src import app, db


@pytest.fixture
def app():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    with app.test_app() as app:
        with app.app_context():
            db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()