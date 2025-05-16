FROM python:3.13-slim

WORKDIR /main

COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/main
# Se o main.py está em /main, o comando abaixo está correto
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
