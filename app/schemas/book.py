# app/schemas/book.py
from datetime import date
from pydantic import BaseModel, Field


class BookBase(BaseModel):
    title: str = Field(..., example="Clean Code")
    author: str = Field(..., example="Robert C. Martin")
    publication_date: date = Field(..., example="2008-08-01")
    summary: str | None = Field(
        None,
        example="Um guia para escrever código limpo.",
    )


class BookCreate(BookBase):
    pass


class BookRead(BookBase):
    id: int

    class Config:
        orm_mode = True
