# tests/test_books.py
from datetime import date


def test_create_book(client):
    payload = {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "publication_date": "2008-08-01",
        "summary": "Livro sobre boas práticas de código.",
    }

    response = client.post("/api/v1/books", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["id"] > 0
    assert data["title"] == payload["title"]
    assert data["author"] == payload["author"]
    assert data["summary"] == payload["summary"]


def test_list_books_without_filters(client):
    response = client.get("/api/v1/books")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1  # já criamos um livro no teste anterior


def test_list_books_filter_by_title(client):
    payload = {
        "title": "Domain-Driven Design",
        "author": "Eric Evans",
        "publication_date": "2003-08-30",
        "summary": "Livro sobre DDD.",
    }
    client.post("/api/v1/books", json=payload)

    response = client.get("/api/v1/books", params={"title": "Domain"})
    assert response.status_code == 200

    data = response.json()
    assert any("Domain-Driven Design" in book["title"] for book in data)


def test_list_books_filter_by_author(client):
    payload = {
        "title": "Refactoring",
        "author": "Martin Fowler",
        "publication_date": "1999-07-08",
        "summary": "Melhorando o design de código existente.",
    }
    client.post("/api/v1/books", json=payload)

    response = client.get("/api/v1/books", params={"author": "Fowler"})
    assert response.status_code == 200

    data = response.json()
    assert any("Fowler" in book["author"] for book in data)


def test_get_book_by_id(client):
    payload = {
        "title": "Test-Driven Development",
        "author": "Kent Beck",
        "publication_date": "2002-05-01",
        "summary": "Introdução prática ao TDD.",
    }
    create_response = client.post("/api/v1/books", json=payload)
    assert create_response.status_code == 201
    created_book = create_response.json()

    response = client.get(f"/api/v1/books/{created_book['id']}")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == created_book["id"]
    assert data["title"] == payload["title"]


def test_get_book_not_found(client):
    response = client.get("/api/v1/books/999999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Livro não encontrado"

def test_create_and_list_books(client):
    payload = {
        "title": "Example Book",
        "author": "Author A",
        "publication_date": "2020-01-01",
        "summary": "Um exemplo de livro para teste."
    }


    r = client.post("/api/v1/books", json=payload)
    assert r.status_code in (200, 201)
    data = r.json()
    assert data["title"] == payload["title"]
    assert data["author"] == payload["author"]

 
    r_list = client.get("/api/v1/books")
    assert r_list.status_code == 200
    lista = r_list.json()
    assert any(book["title"] == "Example Book" for book in lista)

