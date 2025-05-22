FROM r-base:latest

# Instala dependências do sistema (boas práticas para gráficos e manipulação)
RUN apt-get update && apt-get install -y --allow-downgrades \
    libglib2.0-0t64=2.84.1-2 \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    libfontconfig1-dev \
    libfreetype6-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libpng-dev \
    libtiff5-dev \
    libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala os pacotes necessários em uma única linha
RUN R -e "install.packages(c('dplyr', 'tidyr', 'gridExtra'), repos='https://cloud.r-project.org', lib='/usr/local/lib/R/site-library')"

# Define o diretório de trabalho no container
WORKDIR /estatistica

# Copia apenas o script necessário
COPY ./r/estatistica.r .

# Comando de execução padrão
CMD ["Rscript", "estatistica.r"]
