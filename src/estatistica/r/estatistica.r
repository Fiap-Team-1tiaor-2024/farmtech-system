# Instalação de pacotes
install.packages("tidyr", repos = "https://cloud.r-project.org")
install.packages("dplyr", repos = "https://cloud.r-project.org")
install.packages("gridExtra", repos = "https://cloud.r-project.org")

# Importação de bibliotecas
library(tidyr)
library(dplyr)
library(gridExtra)

# Caminho relativo para o diretório de dados
setwd("./r/csv")

# Leitura do arquivo
data <- read.csv("dados-planilha.csv", fileEncoding = "UTF-8", sep = ";", fill = TRUE)

# Calcular médias
media_area <- data %>% group_by(Cultura) %>% summarize(MEDIA_AREA = mean(Area))
media_producao <- data %>% group_by(Cultura) %>% summarize(MEDIA_PRODUCAO = mean(Custo.de.producao))
media_insumo <- data %>% group_by(Tipo.de.insumo) %>% summarize(MEDIA_INSUMO = mean(Insumo))

# Calcular desvios padrão
desvio_area <- data %>% group_by(Cultura) %>% summarize(DESVIO_AREA = sd(Area))
desvio_producao <- data %>% group_by(Cultura) %>% summarize(DESVIO_PRODUCAO = sd(Custo.de.producao))
desvio_insumo <- data %>% group_by(Tipo.de.insumo) %>% summarize(DESVIO_INSUMO = sd(Insumo))

# Exportar CSVs
write.csv(media_area, "media_area.csv", row.names = FALSE)
write.csv(media_producao, "media_producao.csv", row.names = FALSE)
write.csv(media_insumo, "media_insumo.csv", row.names = FALSE)
write.csv(desvio_area, "desvio_area.csv", row.names = FALSE)
write.csv(desvio_producao, "desvio_producao.csv", row.names = FALSE)
write.csv(desvio_insumo, "desvio_insumo.csv", row.names = FALSE)
