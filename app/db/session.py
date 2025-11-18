# app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    """
    Dependency do FastAPI para injetar uma sessão de banco por request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
