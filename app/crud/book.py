# app/crud/book.py
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.book import Book
from app.schemas.book import BookCreate


def create_book(db: Session, book_in: BookCreate) -> Book:
    """
    Cria um novo livro.
    """
    book = Book(
        title=book_in.title.strip(),
        author=book_in.author.strip(),
        publication_date=book_in.publication_date,
        summary=book_in.summary,
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def list_books(
    db: Session,
    title: Optional[str] = None,
    author: Optional[str] = None,
) -> List[Book]:
    """
    Lista livros com filtros opcionais por título e autor (busca parcial).
    """
    query = select(Book)

    if title:
        query = query.where(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.where(Book.author.ilike(f"%{author}%"))

    return db.execute(query).scalars().all()


def get_book_by_id(db: Session, book_id: int) -> Optional[Book]:
    """
    Busca um livro pelo ID.
    """
    return db.get(Book, book_id)
