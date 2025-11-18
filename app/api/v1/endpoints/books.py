# app/api/v1/endpoints/books.py
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.crud import book as book_crud
from app.schemas.book import BookCreate, BookRead  # ⬅ IMPORT CERTO AQUI

router = APIRouter(tags=["Books"], prefix="/books")


@router.post(
    "",
    response_model=BookRead,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar um novo livro",
)
def create_book(
    book_in: BookCreate,
    db: Session = Depends(get_db),
) -> BookRead:
    book = book_crud.create_book(db, book_in)
    return book


@router.get(
    "",
    response_model=List[BookRead],
    summary="Listar livros com filtros opcionais",
)
def list_books(
    title: Optional[str] = Query(
        None, description="Filtro parcial por título (case-insensitive)"
    ),
    author: Optional[str] = Query(
        None, description="Filtro parcial por autor (case-insensitive)"
    ),
    db: Session = Depends(get_db),
) -> List[BookRead]:
    books = book_crud.list_books(db, title=title, author=author)
    return books


@router.get(
    "/{book_id}",
    response_model=BookRead,
    summary="Obter detalhes de um livro pelo ID",
)
def get_book(
    book_id: int,
    db: Session = Depends(get_db),
) -> BookRead:
    book = book_crud.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Livro não encontrado",
        )
    return book
