import requests
import streamlit as st

st.title('🌱 Farmtech')
st.caption(
    'Farmtech é uma plataforma de gestão agrícola que permite o gerenciamento de culturas, propriedades e produções.'
)

st.markdown('---')
st.caption('Clique no botão abaixo para criar uma cultura.')

st.write('**Criar uma cultura**')
cultura_nome = st.text_input(
    'Nome da Cultura',
    placeholder='Digite uma cultura (Ex: Milho)',
    key='cultura_nome_input',
)
if st.button('Criar', key='criar_cultura_btn'):
    response = requests.post(
        'http://backend:8080/v1/farmtech/cultura', json={'nome': cultura_nome}
    )
    if response.status_code == 201:
        st.success('Cultura criada com sucesso! ✅')
    else:
        st.error(f'Erro ao criar cultura. ❌ {response.text}')

st.markdown('---')
st.caption('Clique no botão abaixo para listar todas as culturas.')

st.write('**Listar todas as culturas**')
if st.button('Listar Culturas', key='listar_culturas_btn'):
    response = requests.get('http://backend:8080/v1/farmtech/cultura')
    if response.status_code == 200:
        culturas = response.json()
        if culturas:
            st.write(culturas)
        else:
            st.info('Nenhuma cultura encontrada.')
    else:
        st.error(f'Erro ao listar culturas. ❌ {response.text}')

st.markdown('---')
st.caption('Clique no botão abaixo para criar uma propriedade.')

st.write('**Criar uma propriedade**')
propriedade_nome = st.text_input(
    'Nome da Propriedade',
    placeholder='Digite o nome da propriedade',
    key='propriedade_nome_input',
)
propriedade_localizacao = st.text_input(
    'Localização da Propriedade',
    placeholder='Informe a localização da propriedade',
    key='propriedade_localizacao_input',
)
if st.button('Criar Propriedade', key='criar_propriedade_btn'):
    response = requests.post(
        'http://backend:8080/v1/farmtech/propriedade',
        json={
            'nome': propriedade_nome,
            'localizacao': propriedade_localizacao,
        },
    )
    if response.status_code == 201:
        st.success('Propriedade criada com sucesso. ✅')
    else:
        st.error(f'Erro ao criar propriedade. ❌ {response.text}')

st.markdown('---')
st.write('**Listar todas as propriedades**')

if st.button('Listar Propriedades', key='listar_propriedades_btn'):
    response = requests.get('http://backend:8080/v1/farmtech/propriedade')
    if response.status_code == 200:
        propriedades = response.json()
        if propriedades:
            st.write(propriedades)
        else:
            st.info('Nenhuma propriedade encontrada.')
    else:
        st.error(f'Erro ao listar propriedades. ❌ {response.text}')

st.markdown('---')
st.caption('Clique no botão abaixo para criar uma produção.')

st.write('**Criar uma produção**')
producao_cultura_id = st.number_input(
    'ID da Cultura para Produção',
    placeholder='Digite o ID da cultura',
    min_value=1,
    key='producao_cultura_id_input',
)
producao_propriedade_id = st.number_input(
    'ID da Propriedade para Produção',
    placeholder='Informe o ID da propriedade',
    min_value=1,
    key='producao_propriedade_id_input',
)
producao_area = st.number_input(
    'Área da Produção',
    placeholder='Digite a área da produção',
    min_value=0.0,
    format='%.2f',
    key='producao_area_input',
)
producao_custo = st.number_input(
    'Custo da Produção',
    placeholder='Digite o custo da produção',
    min_value=0.0,
    format='%.2f',
    key='producao_custo_input',
)

if st.button('Criar Produção', key='criar_producao_btn'):
    payload = {
        'id_cultura': int(producao_cultura_id),
        'id_propriedade': int(producao_propriedade_id),
        'area': float(producao_area),
        'custo_producao': float(producao_custo),
    }

    if not all(payload.values()):
        st.warning('Por favor, preencha todos os campos da produção.')
    else:
        response = requests.post(
            'http://backend:8080/v1/farmtech/producao', json=payload
        )
        if response.status_code == 201:
            st.success('Produção criada com sucesso. ✅')
        else:
            st.error(f'Erro ao criar produção. ❌ {response.text}')

st.markdown('---')

st.write('**Listar todas as produções**')
if st.button('Listar Produções', key='listar_producoes_btn'):
    response = requests.get('http://backend:8080/v1/farmtech/producao')
    if response.status_code == 200:
        producoes = response.json()
        if producoes:
            st.write(producoes)
        else:
            st.info('Nenhuma produção encontrada.')
    else:
        st.error(f'Erro ao listar produções. ❌ {response.text}')
