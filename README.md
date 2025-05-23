# Farmtech System 🌱

Farmtech é uma plataforma de gestão agrícola que permite o gerenciamento de culturas, propriedades, produções, além de fornecer análises estatísticas e preditivas sobre dados agrícolas. O sistema também inclui um simulador de dispositivo ESP32 para envio de dados de sensores para uma fila AWS SQS.

Este projeto foi desenvolvido na última fase do ano letivo, sendo uma junção de tudo que foi realizado durante o primeiro ano da graduação de Inteligência Artificial na FIAP.

## 🛠️ Funcionalidades Principais

*   **Gestão de Entidades Agrícolas:**
    *   CRUD (Criar, Ler, Atualizar, Deletar - *Atualizar e Deletar podem não estar implementados no frontend ainda*) para Culturas.
    *   CRUD para Propriedades.
    *   CRUD para Produções, associando culturas e propriedades.
    *   CRUD para Insumos (associados a produções - *schema definido, implementação de CRUD pode variar*).
*   **Análises Estatísticas:**
    *   Execução de scripts R para calcular médias e desvios padrão de dados de produção (área, custo, insumos).
    *   Visualização dos resultados em formato CSV através do frontend.
*   **Análise Preditiva:**
    *   Treinamento de modelos de Regressão Linear, K-Nearest Neighbors (KNN) e Árvore de Decisão.
    *   Cálculo do Mean Squared Error (MSE) para cada modelo.
    *   Visualização de gráficos de dispersão (Valores Reais vs. Previstos) para cada modelo.
*   **Simulador ESP32:**
    *   Simulação de envio de dados de sensores (temperatura, umidade) para uma fila AWS SQS.
*   **Interface Web Interativa:**
    *   Frontend desenvolvido com Streamlit para fácil interação com as funcionalidades do backend.

## 💻 Tecnologias Utilizadas
*   **Gerenciamento de Pacotes:**
    * UV: Gerenciador de pacotes e ambientes virtuais Python.

*   **Organização do Código e Padrão PEP 8:**
    *   **PEP 8:** É o guia de estilo oficial para código Python, que define convenções para escrita de código Python legível e consistente. Aderir à PEP 8 melhora a colaboração e a manutenção do código.
    *   **Blue:** Um formatador de código Python intransigente e opinativo. Ele reformata automaticamente o código Python para garantir um estilo consistente, seguindo as diretrizes da PEP 8, mas com algumas de suas próprias convenções para simplificar a formatação.
    *   **Isort:** Uma utilidade Python para organizar as importações (imports) alfabeticamente e separá-las automaticamente em seções e por tipo. Isso ajuda a manter os imports limpos, consistentes e fáceis de ler, também em conformidade com as diretrizes da PEP 8.

*   **Backend:**
    *   Python 3.13
    *   FastAPI: Para construção de APIs RESTful.
    *   SQLAlchemy: ORM para interação com o banco de dados.
    *   Pydantic: Para validação de dados.
    *   Uvicorn: Servidor ASGI.
*   **Frontend:**
    *   Streamlit: Para criação da interface web interativa.
    *   Requests: Para comunicação com a API do backend.
    *   Pandas: Para manipulação de dados.
    *   Plotly: Para visualização de gráficos.
*   **Análise Estatística:**
    *   R
    *   Pacotes R: `dplyr`, `tidyr`, `gridExtra`.
*   **Banco de Dados:**
    *   PostgreSQL 16
*   **Simulador e Mensageria:**
    *   AWS SQS (Simple Queue Service)
    *   Boto3 (AWS SDK para Python)
*   **Conteinerização:**
    *   Docker
    *   Docker Compose
    *   A conteinerização com **Docker** e **Docker Compose** foi escolhida para integrar os diversos serviços do projeto (backend, frontend, banco de dados, serviço de estatística R) em um ambiente coeso e isolado. Isso simplifica a configuração, o deploy e garante que cada componente execute de forma consistente em diferentes máquinas, facilitando a gestão do ciclo de vida da aplicação como um todo.


## 📂 Estrutura do Projeto

O projeto está organizado da seguinte forma dentro do diretório `src/`:

```
src/
├── backend/        # Lógica do backend (API    FastAPI, modelos, schemas, roteadores)
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   ├── models/
│   ├── routers/
│   └── schemas/
├── estatistica/    # Serviço de análise estatística com R
│   ├── Dockerfile
│   └── r/
│       ├── estatistica.r
│       └── csv/          # Dados de entrada e saída para o script R
├── frontend/       # Interface do usuário com Streamlit
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   └── pages/          # Páginas adicionais do Streamlit (estatistica, predicao)
├── infra/          # Configurações de infraestrutura
│   ├── .env            # Arquivo de variáveis de ambiente (deve ser criado localmente)
│   ├── database/       # Configuração da conexão com o banco de dados
│   ├── ddl/            # Scripts DDL para criação do esquema do banco
│   └── setup/          # Scripts para setup inicial (ex: criação de tabelas)
└── ...
```

## ⚙️ Configuração e Instalação

### Pré-requisitos

*   Docker: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
*   Docker Compose: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

### Variáveis de Ambiente

1.  Crie um arquivo `.env` na pasta `src/infra/` baseado no exemplo abaixo.
2.  Preencha com as suas credenciais e configurações.

    ```env
    # src/infra/.env
    DB_USER=seuusuario
    DB_PASSWORD=suasenha
    DB_URL=farmtech-db # Nome do serviço do banco de dados no docker-compose
    DB_NAME=farmtech
    DB_PORT=5432

    # AWS Credentials (para o simulador ESP32 e SQS)
    AWS_ACCESS_KEY_ID=SEU_AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY=SEU_AWS_SECRET_ACCESS_KEY
    AWS_REGION=sua-regiao-aws # ex: us-east-1
    AWS_SQS_QUEUE_URL=URL_DA_SUA_FILA_SQS
    ```

### 🚀 Executando o Projeto

1.  Clone o repositório:
    ```bash
    git clone <url-do-seu-repositorio>
    cd farmtech-system
    ```

2.  Construa e inicie os containers Docker:
    ```bash
    docker-compose up --build -d
    ```
    O `-d` executa os containers em modo detached (background).

3.  Após os containers estarem rodando:
    *   O **Frontend (Streamlit)** estará acessível em: `http://localhost:8501`
    *   A **API Backend (FastAPI)** estará acessível em: `http://localhost:8080`
    *   A documentação interativa da API (Swagger UI) estará em: `http://localhost:8080/docs`
    *   O **Banco de Dados PostgreSQL** estará acessível na porta `5432` (para ferramentas de DB externas, se necessário).

4.  O serviço `db-setup` tentará criar as tabelas no banco de dados automaticamente após o serviço `db` estar pronto.

## 🔗 Principais Endpoints da API (Backend)

Localizados em `http://localhost:8080/v1/farmtech/`:

*   **Culturas:**
    *   `POST /cultura`: Cria uma nova cultura.
    *   `GET /cultura`: Lista todas as culturas.
*   **Propriedades:**
    *   `POST /propriedade`: Cria uma nova propriedade.
    *   `GET /propriedade`: Lista todas as propriedades.
*   **Produções:**
    *   `POST /producao`: Cria uma nova produção.
    *   `GET /producao`: Lista todas as produções.
*   **Análises Estatísticas com R:**
    *   `POST /analises/r/executar`: Executa o script R de estatísticas.
    *   `GET /analises/r/csv/{filename}`: Obtém um arquivo CSV gerado pelo script R.
*   **Análise Preditiva:**
    *   `GET /predicao`: Executa os modelos preditivos e retorna MSEs e dados para gráficos.
*   **Simulador ESP32:**
    *   `POST /simulador`: Inicia o simulador para enviar dados para a fila SQS.

## 🖥️ Páginas do Frontend

Acesse `http://localhost:8501`:

*   **Página Principal (`main.py`):**
    *   Gerenciamento de Culturas (Criar, Listar).
    *   Gerenciamento de Propriedades (Criar, Listar).
    *   Gerenciamento de Produções (Criar, Listar).
*   **Página de Estatísticas (`pages/estatistica.py`):**
    *   Botão para executar as análises estatísticas via script R.
    *   Exibição dos resultados (arquivos CSV gerados).
*   **Página de Predição (`pages/predicao.py`):**
    *   Botão para executar os modelos de análise preditiva.
    *   Exibição dos MSEs e gráficos de dispersão (Real vs. Previsto).
*   **Página do Simulador ESP32 (`pages/esp32.py`):**
    *   Botão para iniciar a simulação de envio de dados de sensores (temperatura, umidade) para uma fila AWS SQS.

## 🗄️ Banco de Dados

O sistema utiliza PostgreSQL como banco de dados. O esquema é definido pelos modelos SQLAlchemy em `src/backend/models/models.py` e pode ser visualizado no arquivo DDL em `src/infra/ddl/sql-generator-farmtech.ddl`.

As tabelas são criadas automaticamente ao iniciar os containers pelo serviço `db-setup` que executa `src/infra/setup/setup_db.py`.

## 🛑 Para Parar a Aplicação

```bash
docker-compose down
```
Para remover os volumes (incluindo os dados do banco de dados):
```bash
docker-compose down -v
```

## 👨‍💻 Autores
- Gabrielle Barao Halasc Frateschi - RM560147@fiap.com.br
- Gabriela da Cunha Rocha - RM561041@fiap.com.br
- Gustavo Segantini Rossignolli - RM560111@fiap.com.br
- Vitor Lopes Romão - RM559858@fiap.com.br