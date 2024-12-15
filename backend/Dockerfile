# Usar uma imagem base do Python
FROM python:3.11

# Criar e definir o diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Criar um ambiente virtual para o Python
RUN python -m venv /venv

# Ativar o ambiente virtual e instalar as dependências do Python
ENV PATH="/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código para o contêiner
COPY . .

# Expor a porta 8000
EXPOSE 8000

# Comando para rodar o servidor de desenvolvimento do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
