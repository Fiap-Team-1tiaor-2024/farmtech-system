FROM python:3.13-slim

RUN apt-get update && apt-get install -y r-base

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /main
WORKDIR /main

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
