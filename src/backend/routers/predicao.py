import pandas as pd
import plotly.graph_objects as go
from fastapi import APIRouter
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

router = APIRouter()

@router.get("/predict")
def predict():
    # Ler o arquivo CSV
    df = pd.read_csv('C:/Dev/Projetos/FIAP/Fase 7/farmtech-system/src/estatistica/r/csv/estrutura_tabelas.csv', delimiter=';')

    # Selecionar as features e o target
    X = df[['area_total', 'latitude_plantio', 'longitude_plantio', 'qtde_insumo_total']]
    y = df['valor_medido']

    # Dividir os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treinar o modelo Linear Regression
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    y_pred_lr = lr_model.predict(X_test)
    mse_lr = mean_squared_error(y_test, y_pred_lr)

    # Treinar o modelo KNN
    knn_model = KNeighborsRegressor(n_neighbors=5)
    knn_model.fit(X_train, y_train)
    y_pred_knn = knn_model.predict(X_test)
    mse_knn = mean_squared_error(y_test, y_pred_knn)

    # Treinar o modelo Decision Tree
    dt_model = DecisionTreeRegressor(random_state=42)
    dt_model.fit(X_train, y_train)
    y_pred_dt = dt_model.predict(X_test)
    mse_dt = mean_squared_error(y_test, y_pred_dt)

    # Retornar os resultados
    return {
        "mse_lr": mse_lr,
        "mse_knn": mse_knn,
        "mse_dt": mse_dt,
    }