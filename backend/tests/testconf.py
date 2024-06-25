import pytest
from src import app, db
from flask_migrate import Migrate



@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    
    with app.app_context():
        db.create_all()
        migrate = Migrate(app, db)
        with app.test_client() as client:
            yield client
