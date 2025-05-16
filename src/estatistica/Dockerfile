FROM r-base:latest

RUN apt-get update && apt-get install -y libcurl4-openssl-dev libssl-dev libxml2-dev

RUN R -e "install.packages(c('dplyr', 'tidyr', 'gridExtra'), repos='https://cloud.r-project.org')"

WORKDIR /estatistica
COPY ./r/estatistica.r .

CMD ["Rscript", "estatistica.r"]