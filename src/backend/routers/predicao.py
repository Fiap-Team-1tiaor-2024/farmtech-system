import pandas as pd
from fastapi import APIRouter
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

router = APIRouter()

# Caminho para o arquivo CSV dentro do container do backend
# Assumindo que o volume ./src:/app está montado e o arquivo está em src/estatistica/r/csv/
CSV_FILE_PATH = '/app/estatistica/r/csv/estrutura_tabelas.csv'


@router.get('/predicao')
def predicao():
    try:
        df = pd.read_csv(CSV_FILE_PATH, delimiter=';')
    except Exception as e:
        return {'error': f'Erro ao ler o arquivo CSV: {str(e)}'}

    # Verificar se as colunas necessárias existem
    required_columns = [
        'area_total',
        'latitude_plantio',
        'longitude_plantio',
        'qtde_insumo_total',
        'valor_medido',
    ]

    if not all(col in df.columns for col in required_columns):
        return {
            'error': f'Colunas necessárias não encontradas no CSV. Necessário: {required_columns}'
        }

    df.dropna(subset=required_columns, inplace=True)

    if df.empty:
        return {
            'error': 'Não há dados suficientes após remover NaNs para realizar a predição.'
        }

    X = df[
        [
            'area_total',
            'latitude_plantio',
            'longitude_plantio',
            'qtde_insumo_total',
        ]
    ]
    y = df['valor_medido']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    y_pred_lr = lr_model.predict(X_test)
    mse_lr = mean_squared_error(y_test, y_pred_lr)

    knn_model = KNeighborsRegressor()
    knn_model.fit(X_train, y_train)
    y_pred_knn = knn_model.predict(X_test)
    mse_knn = mean_squared_error(y_test, y_pred_knn)

    dt_model = DecisionTreeRegressor(random_state=42)
    dt_model.fit(X_train, y_train)
    y_pred_dt = dt_model.predict(X_test)
    mse_dt = mean_squared_error(y_test, y_pred_dt)

    return {
        'mse_lr': mse_lr,
        'mse_knn': mse_knn,
        'mse_dt': mse_dt,
        'y_test': y_test.tolist(),  # Converter para lista para serialização JSON
        'y_pred_lr': y_pred_lr.tolist(),
        'y_pred_knn': y_pred_knn.tolist(),
        'y_pred_dt': y_pred_dt.tolist(),
    }
