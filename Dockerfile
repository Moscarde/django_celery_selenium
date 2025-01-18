# Usando a imagem base oficial do Python 3.11
FROM python:3.11.11-slim

# Configuração básica
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Configurar diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    libpq-dev gcc --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Instalar dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código do projeto
COPY . /app/

# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
