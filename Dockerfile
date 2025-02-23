# Usa uma imagem base oficial do Python
FROM python:3.11-slim

# Instala o Git para poder clonar repositórios
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Clona o repositório diretamente do GitHub
RUN git clone https://github.com/nltt-br/GetSampleMB.git .

# Copia o arquivo .env local para o container
COPY .env GetSampleMB/.env

# Instala as dependências, se houver um requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Especifica o comando padrão para rodar o script
ENTRYPOINT ["python", "GetSampleMB.py"]
