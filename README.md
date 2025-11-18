# 📚 Biblioteca Virtual API

API REST para cadastro e consulta de livros, desenvolvida com **FastAPI**, **SQLAlchemy**, **SQLite** e **Pytest**. Este projeto foi estruturado para garantir clareza, modularidade e testabilidade.

## 🚀 Objetivo do Projeto

A API permite que usuários:

*   Cadastrem livros
*   Consultem todos os livros
*   Façam busca filtrando por título ou autor
*   Consultem um livro específico pelo ID

O projeto inclui:

*   Arquitetura limpa
*   Separação de camadas (API, Schemas, Models, CRUD, BD)
*   Banco de testes isolado
*   Suite completa de testes automatizados com Pytest
*   Suporte a Docker e Docker Compose

Qualquer pessoa consegue instalar e rodar a API com poucos comandos.

## 📁 Estrutura de Pastas

```
biblioteca_api/
├─ app/
│  ├─ api/
│  │  └─ v1/endpoints/books.py     → Endpoints da API
│  ├─ crud/book.py                 → Lógica de acesso ao banco
│  ├─ db/                          → Engine, sessão, Base
│  ├─ models/book.py               → Modelo ORM
│  ├─ schemas/book.py              → Schemas Pydantic
│  └─ main.py                      → Inicialização da aplicação
├─ tests/
│  ├─ conftest.py                  → Setup do banco de testes
│  └─ test_books.py                → Testes automatizados
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
└─ README.md
```

## 🧱 Arquitetura

A aplicação segue uma estrutura modular inspirada em boas práticas de **Clean Architecture**:

*   **API Layer** → rotas e validação inicial
*   **Schemas (DTOs)** → entrada e saída de dados
*   **CRUD Layer (Repository)** → acesso ao banco
*   **Models (ORM)** → definição das tabelas
*   **DB Layer** → engine, sessão e configuração

O objetivo é manter **baixo acoplamento** e **alta testabilidade**.

## ⚙️ Instalação e Execução (Modo Simples)

### 1. Instale o Python (recomendado 3.14)

[https://www.python.org/downloads/](https://www.python.org/downloads/)

> Marque: "Add Python to PATH"

### 2. Crie o ambiente virtual

Na pasta do projeto:

```bash
python -m venv venv
```

Ative o ambiente:

**Windows:**
```bash
.\venv\Scripts\activate
```

**Mac / Linux:**
```bash
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

ou:

```bash
pip install fastapi "uvicorn[standard]" sqlalchemy pytest httpx
```

### 4. Rode a API

```bash
uvicorn app.main:app --reload
```

Acesse:

*   **Swagger:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
*   **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## ▶️ Exemplos de Uso

### Criar livro – `POST /api/v1/books`

```json
{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "publication_date": "2008-08-01",
  "summary": "Um guia para escrever código limpo."
}
```

### Listar livros – `GET /api/v1/books`

Filtro por título:
```
/api/v1/books?title=clean
```

### Buscar por ID

```
/api/v1/books/1
```

## 🐳 Modo Docker

Se preferir rodar sem instalar Python:

```bash
docker-compose up --build
```

A API ficará disponível em:

[http://localhost:8000](http://localhost:8000)

## 🧪 Testes Automatizados

O projeto vem com uma suíte de testes completa usando **Pytest**, incluindo:

*   Criação de livros
*   Listagem
*   Filtros por título e autor
*   Busca por ID
*   Cenários de erro
*   Banco de testes isolado (`test.db`)

Para rodar:

```bash
python -m pytest -v
```

### 🧭 Como funciona o banco de testes?

*   O `conftest.py` cria um SQLite chamado `test.db` só para testes
*   O arquivo é removido **ANTES** dos testes para começar sempre limpo
*   O *engine* é isolado e não interfere no banco real
*   O cliente de testes usa *override* da dependência `get_db`

Isso garante que os testes sejam **repetíveis**, **independentes** e **confiáveis**.

## 📌 Considerações Finais

Este projeto foi desenvolvido seguindo boas práticas de engenharia:

*   Arquitetura modular
*   Testes automatizados
*   Separação de camadas
*   Docker-friendly
*   Código simples e legível
*   Facilmente extensível
