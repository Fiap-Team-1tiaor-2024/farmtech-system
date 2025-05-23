import streamlit as st
import requests
import plotly.graph_objects as go

st.set_page_config(layout='wide')
st.title('☁️ Simulador de ESP32')
st.markdown(
    """
    Este simulador envia dados de temperatura e umidade para o AWS SQS. 
    """
)

if st.button('Simular dados para AWS ', type='primary'):
    with st.spinner(
        '🔄 Enviando os dados para fila SQS... Por favor, aguarde.'
    ):   # Adicionado timeout
        try:
            response = requests.post(
                'http://backend:8080/v1/farmtech/simulador',
                timeout=300,
            )

            if response.status_code == 200:
                data = response.json()
                st.success('✅ Dados enviados com sucesso para a fila SQS!')
            else:
                st.error(f'❌ Erro ao enviar dados: {response.text}')
        except requests.exceptions.RequestException as e:
            st.error(f'❌ Erro de conexão: {e}')

st.markdown('---')
st.caption(
    'Clique no botão acima para simular o envio de dados de temperatura e umidade para o AWS SQS.'
)