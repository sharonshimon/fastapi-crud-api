# tests/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from fastapi.testclient import TestClient

from app.db import Base, get_db
from app.main import app

# 1) Use a single in-memory SQLite DB for the whole test suite
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,        # ← crucial: share the same DB across connections
)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

@pytest.fixture(scope="session", autouse=True)
def setup_database() -> None:
    """
    Create all tables once before any tests run, then drop them at session end.
    """
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db_session():
    """
    Start a SAVEPOINT transaction for a test and roll it back afterwards,
    ensuring a clean slate every time.
    """
    # 2) open a connection and begin a transaction
    connection = engine.connect()
    transaction = connection.begin()

    # bind a session to that connection
    session = TestingSessionLocal(bind=connection)
    try:
        yield session
    finally:
        session.close()
        transaction.rollback()  # undo everything this test did
        connection.close()

@pytest.fixture
def client(db_session):
    """
    Override FastAPI's get_db dependency so that endpoints all use our
    transactional db_session, then give back the TestClient.
    """
    def _override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _override_get_db
    return TestClient(app)
