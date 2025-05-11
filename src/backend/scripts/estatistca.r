# Instalação de pacotes
install.packages("tidyr")
install.packages("dplyr")
install.packages("gridExtra")

# Importação de bibliotecas
library(tidyr)
library(dplyr)
library(gridExtra)

# Adaptar de acordo com o caminho do arquivo do usuário
setwd("C:/Dev/Projetos/FarmTech/src/farm-tech/csv")

# Leitura do arquivo
data <- read.csv("dados-planilha.csv", fileEncoding = "UTF-8", sep = ";", fill = TRUE)

# Visualização dos dados e calculo da média
media_area <- data %>%  group_by(Cultura) %>% summarize(MEDIA_AREA = mean(Area))
media_producao <- data %>%  group_by(Cultura) %>% summarize(MEDIA_PRODUCAO = mean(Custo.de.producao))
media_insumo <- data %>%  group_by(Tipo.de.insumo) %>% summarize(MEDIA_INSUMO = mean(Insumo))

# Visualização dos dados na tabela
grid.table(media_area)
print(media_area)

grid.table(media_producao)
print(media_producao)

grid.table(media_insumo)
print(media_insumo)

# Visualização dos dados e calculo do desvio padrão
desvio_area <- data %>%  group_by(Cultura) %>% summarize(DESVIO_AREA = sd(Area))
desvio_producao <- data %>%  group_by(Cultura) %>% summarize(DESVIO_PRODUCAO = sd(Custo.de.producao))
desvio_insumo <- data %>%  group_by(Tipo.de.insumo) %>% summarize(DESVIO_INSUMO = sd(Insumo))

# Visualização dos dados na tabela
grid.table(desvio_area)
print(desvio_area)

grid.table(desvio_producao)
print(desvio_producao)

grid.table(desvio_insumo)
print(desvio_insumo)
