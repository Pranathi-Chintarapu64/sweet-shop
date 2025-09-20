import pytest
from fastapi.testclient import TestClient
from ..main import app
from ..database import Base, engine, SessionLocal
from .. import models, auth, crud
import os
import tempfile

TEST_DB = "sqlite:///./test_data.db"

# ensure fresh test DB
def reset_db():
    try:
        Base.metadata.drop_all(bind=engine)
    except Exception:
        pass
    Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="session")
def client():
    reset_db()
    with TestClient(app) as c:
        yield c

@pytest.fixture
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
