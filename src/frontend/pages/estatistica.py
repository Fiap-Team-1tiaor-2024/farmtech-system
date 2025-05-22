import pandas as pd
import requests
import streamlit as st

st.set_page_config(layout='wide')
st.title('📊 Análises Estatísticas com R')

if st.button('Executar Análise R', type='primary'):
    with st.spinner(
        '🔄 Executando script R via backend... Por favor, aguarde.'
    ):
        try:
            response = requests.post(
                'http://backend:8080/v1/farmtech/analises/r/executar',
                timeout=300,
            )   # Adicionado timeout

            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    st.success(
                        '✅ Script R executado com sucesso pelo backend!'
                    )
                    if data.get('output'):
                        with st.expander('Ver saída do script R (stdout)'):
                            st.text_area(
                                'Output',
                                value=data['output'],
                                height=200,
                                disabled=True,
                            )

                    st.markdown('---')
                    st.subheader('Resultados da Análise:')

                    arquivos_csv = [
                        'media_area.csv',
                        'media_producao.csv',
                        'media_insumo.csv',
                        'desvio_area.csv',
                        'desvio_producao.csv',
                        'desvio_insumo.csv',
                    ]

                    cols = st.columns(2)  # Exibir em 2 colunas

                    for i, arquivo in enumerate(arquivos_csv):
                        col = cols[i % 2]
                        csv_url = f'http://backend:8080/v1/farmtech/analises/r/csv/{arquivo}'
                        try:
                            df = pd.read_csv(csv_url)
                            col.subheader(
                                arquivo.replace('.csv', '')
                                .replace('_', ' ')
                                .title()
                            )
                            col.dataframe(df)
                        except Exception as e:
                            col.warning(
                                f'⚠️ Erro ao carregar ou exibir {arquivo}: {e}'
                            )
                            col.caption(f'URL tentada: {csv_url}')
                else:
                    st.error('❌ Falha ao executar script R no backend.')
                    if data.get('stdout'):
                        with st.expander('Ver saída do script R (stdout)'):
                            st.text_area(
                                'Stdout',
                                value=data['stdout'],
                                height=100,
                                disabled=True,
                            )
                    if data.get('stderr'):
                        with st.expander('Ver erro do script R (stderr)'):
                            st.text_area(
                                'Stderr',
                                value=data['stderr'],
                                height=100,
                                disabled=True,
                            )
            else:
                st.error(
                    f'🚫 Erro na comunicação com o backend ao executar o script: {response.status_code}'
                )
                try:
                    st.json(
                        response.json()
                    )   # Tenta mostrar o corpo do erro se for JSON
                except:
                    st.text(
                        response.text
                    )   # Caso contrário, mostra como texto

        except requests.exceptions.RequestException as e:
            st.error(f'🚨 Erro de conexão ao tentar executar o script R: {e}')
            st.info(
                "Verifique se o serviço de backend está rodando e acessível em 'http://backend:8080'."
            )

st.markdown('---')
st.caption(
    'Clique no botão acima para gerar e visualizar as análises estatísticas.'
)
