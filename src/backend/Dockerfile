FROM python:3.13-slim

# Instalar R, dependências de compilação para pacotes R e limpar o cache do apt
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    r-base \
    r-base-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalar os pacotes R necessários para o script estatistica.r
RUN R -e "install.packages(c('tidyr', 'dplyr', 'gridExtra'), repos='http://cran.rstudio.com/')"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /main
WORKDIR /main

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]