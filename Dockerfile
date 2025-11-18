# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copia arquivos de requisitos
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
