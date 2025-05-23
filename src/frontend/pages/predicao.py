import plotly.graph_objects as go
import requests
import streamlit as st

st.set_page_config(layout='wide')
st.title('📊 Análise Preditiva')
st.markdown(
    """
    Esta página executa um script Python para gerar previsões de produção agrícola utilizando 
    algoritmos de aprendizado de máquina como Regressão Linear, KNN e Árvore de Decisão.
    """
)

# Função para criar o gráfico de dispersão Real vs. Previsto
def criar_grafico_dispersao(y_true, y_pred, title):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=y_true,
            y=y_pred,
            mode='markers',
            name='Previsões',
            marker=dict(color='blue'),
        )
    )

    # Adiciona a linha de referência (y=x), onde a predição seria perfeita
    min_val = min(min(y_true), min(y_pred))
    max_val = max(max(y_true), max(y_pred))
    fig.add_trace(
        go.Scatter(
            x=[min_val, max_val],
            y=[min_val, max_val],
            mode='lines',
            name='Linha Ideal (y=x)',
            line=dict(color='red', dash='dash'),
        )
    )
    fig.update_layout(
        title=title,
        xaxis_title='Valores Reais',
        yaxis_title='Valores Previstos',
        showlegend=True,
    )
    return fig


if st.button('Executar Predição', type='primary'):
    with st.spinner(
        '🔄 Executando Predição via backend... Por favor, aguarde.'
    ):
        try:
            response = requests.get(
                'http://backend:8080/v1/farmtech/predicao', timeout=300
            )

            if response.status_code == 200:
                data = response.json()

                if 'error' in data:
                    st.error(f"❌ Erro no backend: {data['error']}")
                else:
                    st.subheader('Resultados da Análise Preditiva (MSE)')
                    st.write(
                        f"**Linear Regression**: {data.get('mse_lr', 'N/A'):.4f}"
                    )
                    st.write(f"**KNN**: {data.get('mse_knn', 'N/A'):.4f}")
                    st.write(f"**Decision Tree**: {data.get('mse_dt', 'N/A'):.4f}")

                    st.markdown('---')
                    st.subheader('Gráficos de Dispersão (Real vs. Previsto)')

                    y_test = data.get('y_test')

                    if y_test:
                        # Gráfico Linear Regression
                        if 'y_pred_lr' in data:
                            fig_lr = criar_grafico_dispersao(
                                y_test, data['y_pred_lr'], 'Regressão Linear'
                            )
                            st.plotly_chart(fig_lr, use_container_width=True)
                        else:
                            st.warning(
                                'Dados de predição para Regressão Linear não encontrados.'
                            )

                        # Gráfico KNN
                        if 'y_pred_knn' in data:
                            fig_knn = criar_grafico_dispersao(
                                y_test,
                                data['y_pred_knn'],
                                'K-Nearest Neighbors (KNN)',
                            )
                            st.plotly_chart(fig_knn, use_container_width=True)
                        else:
                            st.warning(
                                'Dados de predição para KNN não encontrados.'
                            )

                        # Gráfico Decision Tree
                        if 'y_pred_dt' in data:
                            fig_dt = criar_grafico_dispersao(
                                y_test, data['y_pred_dt'], 'Árvore de Decisão'
                            )
                            st.plotly_chart(fig_dt, use_container_width=True)
                        else:
                            st.warning(
                                'Dados de predição para Árvore de Decisão não encontrados.'
                            )
                    else:
                        st.warning(
                            'Dados de teste (y_test) não encontrados para gerar gráficos.'
                        )
            else:
                st.error(
                    f'❌ Erro ao executar a predição. Status: {response.status_code}'
                )

        except requests.exceptions.RequestException as e:
            st.error(f'🚨 Erro de conexão ao tentar executar a predição: {e}')
            st.info(
                "Verifique se o serviço de backend está rodando e acessível em 'http://backend:8080'."
            )

st.markdown('---')
st.caption(
    'Clique no botão acima para gerar e visualizar as análises preditivas.'
)
