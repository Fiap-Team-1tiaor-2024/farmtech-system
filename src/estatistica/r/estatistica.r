# Importação de bibliotecas
library(tidyr)
library(dplyr)
library(gridExtra)

# Caminho relativo para o diretório de dados
# Este caminho é relativo ao diretório de trabalho, que deve ser /estatistica no container
csv_path <- "r/csv/dados-planilha.csv"

# Confere se o arquivo existe
if (!file.exists(csv_path)) {
  stop(paste("❌ Arquivo não encontrado:", csv_path, " (Diretório de trabalho atual:", getwd(), ")"))
}

# Leitura do arquivo
data <- read.csv(csv_path, fileEncoding = "UTF-8", sep = ";", fill = TRUE)

# Define o diretório de saída relativo ao diretório de trabalho /estatistica
output_dir <- "r/csv"
if (!dir.exists(output_dir)) {
  dir.create(output_dir, recursive = TRUE)
}

# Calcular médias
media_area <- data %>% group_by(Cultura) %>% summarize(MEDIA_AREA = mean(Area, na.rm = TRUE))
media_producao <- data %>% group_by(Cultura) %>% summarize(MEDIA_PRODUCAO = mean(Custo.de.producao, na.rm = TRUE))
media_insumo <- data %>% group_by(Tipo.de.insumo) %>% summarize(MEDIA_INSUMO = mean(Insumo, na.rm = TRUE))

# Calcular desvios padrão
desvio_area <- data %>% group_by(Cultura) %>% summarize(DESVIO_AREA = sd(Area, na.rm = TRUE))
desvio_producao <- data %>% group_by(Cultura) %>% summarize(DESVIO_PRODUCAO = sd(Custo.de.producao, na.rm = TRUE))
desvio_insumo <- data %>% group_by(Tipo.de.insumo) %>% summarize(DESVIO_INSUMO = sd(Insumo, na.rm = TRUE))

# Exportar CSVs para o diretório de saída especificado
write.csv(media_area, file.path(output_dir, "media_area.csv"), row.names = FALSE)
write.csv(media_producao, file.path(output_dir, "media_producao.csv"), row.names = FALSE)
write.csv(media_insumo, file.path(output_dir, "media_insumo.csv"), row.names = FALSE)
write.csv(desvio_area, file.path(output_dir, "desvio_area.csv"), row.names = FALSE)
write.csv(desvio_producao, file.path(output_dir, "desvio_producao.csv"), row.names = FALSE)
write.csv(desvio_insumo, file.path(output_dir, "desvio_insumo.csv"), row.names = FALSE)

print(paste("Arquivos CSV gerados com sucesso em:", file.path(getwd(), output_dir)))