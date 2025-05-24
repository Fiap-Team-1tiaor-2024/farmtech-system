FROM python:3.13-slim

# Instalar R, dependências de compilação para pacotes R, libgl1 e limpar o cache do apt
RUN apt-get update && \
    apt-get install -y --allow-downgrades --no-install-recommends \
    r-base \
    r-base-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    libgl1-mesa-glx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalar os pacotes R necessários para o script estatistica.r
RUN R -e "install.packages(c('tidyr', 'dplyr', 'gridExtra'), repos='http://cran.rstudio.com/')"

# Copiar requirements do backend
COPY requirements.txt .
# Instalar dependências do backend com pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o conteúdo do backend para /main
COPY . /main
WORKDIR /main

# Instalar dependências do YOLOv5 com pip
RUN if [ -f yolov5/requirements.txt ]; then \
        pip install --no-cache-dir -r yolov5/requirements.txt; \
    else \
        echo "yolov5/requirements.txt não encontrado, pulando instalação de dependências do YOLOv5."; \
    fi

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]