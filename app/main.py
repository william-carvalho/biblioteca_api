# app/main.py
from fastapi import FastAPI

from app.api.v1.endpoints.books import router as books_router
from app.db.base import Base
from app.db.session import engine


def create_app() -> FastAPI:
    """
    Cria e configura a aplicação FastAPI.
    """
    Base.metadata.create_all(bind=engine)

    app = FastAPI(
        title="Biblioteca Virtual API",
        version="1.0.0",
        description=(
            "API para cadastro e consulta de livros em uma biblioteca virtual.\n\n"
            "Permite cadastrar livros e consultar por título ou autor."
        ),
    )

    app.include_router(books_router, prefix="/api/v1")

    return app


app = create_app()
