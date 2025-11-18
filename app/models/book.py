# app/models/book.py
from sqlalchemy import Column, Integer, String, Date

from app.db.base import Base


class Book(Base):
    """
    Entidade de domínio que representa um livro na biblioteca.
    """

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, index=True, nullable=False)
    publication_date = Column(Date, nullable=False)
    summary = Column(String, nullable=True)
