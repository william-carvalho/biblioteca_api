# tests/conftest.py
import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.db.base import Base
from app.db.session import get_db
from app.main import create_app
from app.models import book  # noqa: F401


SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"

engine_test = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine_test,
)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """
    Cria o schema no banco de testes antes da suíte.
    Remove o arquivo apenas ANTES de criar, para evitar erro de lock no Windows.
    """
    if os.path.exists("test.db"):
        os.remove("test.db")

    Base.metadata.create_all(bind=engine_test)
    yield

    # Libera conexões do engine; se quiser, pode remover o arquivo depois disso.
    engine_test.dispose()
    # Se quiser muito apagar o arquivo:
    # if os.path.exists("test.db"):
    #     os.remove("test.db")


@pytest.fixture()
def app():
    application = create_app()
    application.dependency_overrides[get_db] = override_get_db
    return application


@pytest.fixture()
def client(app):
    return TestClient(app)
